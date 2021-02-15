import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# ------------------------------------------------------ Configuration

app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

# ------------------------------------------------------ Homepage


@app.route("/")
@app.route("/index")
def index():
    recipes = mongo.db.recipes.find().limit(6)
    return render_template("index.html", recipes=recipes)


# ------------------------------------------------------ User
# ---------------------------------------- Register


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    # Keep user on profile upon sign up if use back button
    if "user" in session:
        return redirect(url_for("profile", username=session["user"]))

    if request.method == "POST":
        # Check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("sign_up"))
        # Dictionary of new users entered details
        sign_up = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "confirm-password": generate_password_hash(
                request.form.get("confirm-password"))
        }
        mongo.db.users.insert_one(sign_up)

        # Put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Account Created...Welcome!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# ---------------------------------------- Login


@app.route("/login", methods=("GET", "POST"))
def login():
    # Keep user on profile upon login if use back button
    if "user" in session:
        return redirect(url_for("profile", username=session["user"]))

    if request.method == "POST":
        # Check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password entered", "error")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password entered", "error")
            return redirect(url_for("login"))

    return render_template("login.html")


# ---------------------------------------- Profile


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Get session user's recipes from the database ordered by most recent
    recipes = mongo.db.recipes.find({
        "$query": {
                "created_by": session["user"]
            },
        "$orderby": {
                "date_added": -1
            }
        })

    # Get session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes)
    # Send user to login if not logged in
    return redirect(url_for("login"))


# ---------------------------------------- Logout


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ------------------------------------------------------ Recipes
# ---------------------------------------- Recipe page


@app.route("/recipe/<recipe_id>")
def get_recipe(recipe_id):
    # Find recipe from the database
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template("recipe.html", recipe=recipe)


# ---------------------------------------- Search bar


@app.route("/search", methods=["GET", "POST"])
def search():
    # Search for recipes in database by keywords
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))

    return render_template("search.html", recipes=recipes)

# ---------------------------------------- Recipe category page


@app.route("/recipe_category/<category>")
def recipe_category(category):
    # Find and populate recipes by category
    if category == "all":
        recipes = list(
            mongo.db.recipes.find({
                "$query": {},
                "$orderby": {
                        "date_added": -1
                    }
            })
        )
    elif category == "starters":
        recipes = list(
            mongo.db.recipes.find({
                "$query": {
                    "category_name": "Starters"
                    },
                "$orderby": {
                        "date_added": -1
                    }
            })
        )
    elif category == "mains":
        recipes = list(
            mongo.db.recipes.find({
                "$query": {
                    "category_name": "Mains"
                    },
                "$orderby": {
                    "date_added": -1
                    }
            })
        )
    elif category == "desserts":
        recipes = list(
            mongo.db.recipes.find({
                "$query": {
                    "category_name": "Desserts"
                    },
                "$orderby": {
                    "date_added": -1
                    }
            })
        )

    return render_template(
        "recipes.html", category_name=category, recipes=recipes)


# ---------------------------------------- Add Recipe


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # Add recipe to the database
    if request.method == "POST":
        is_vegetarian = "on" if request.form.get("is_vegetarian") else "off"
        is_gluten_free = "on" if request.form.get("is_gluten_free") else "off"
        # Dictionary of recipe details
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_title": request.form.get("recipe_title"),
            "recipe_description": request.form.get("recipe_description"),
            "image_url": request.form.get("image_url"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "serves": request.form.get("serves"),
            "difficulty": request.form.get("difficulty"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "is_vegetarian": is_vegetarian,
            "is_gluten_free": is_gluten_free,
            "date_added": datetime.today().strftime("%d %B %Y @ %X"),
            "created_by": session["user"]
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")

        return redirect(url_for("profile", username=session["user"]))

    # Find the categories from the database
    categories = mongo.db.categories.find()

    return render_template("add_recipe.html", categories=categories)


# ---------------------------------------- Edit Recipe


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    # Edit a recipe from the database
    if request.method == "POST":
        is_vegetarian = "on" if request.form.get("is_vegetarian") else "off"
        is_gluten_free = "on" if request.form.get("is_gluten_free") else "off"
        # Dicitonary of edited recipe details
        rec_update = {"$set": {
            "category_name": request.form.get("category_name"),
            "recipe_title": request.form.get("recipe_title"),
            "recipe_description": request.form.get("recipe_description"),
            "image_url": request.form.get("image_url"),
            "prep_time": request.form.get("prep_time"),
            "cooking_time": request.form.get("cooking_time"),
            "serves": request.form.get("serves"),
            "difficulty": request.form.get("difficulty"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "is_vegetarian": is_vegetarian,
            "is_gluten_free": is_gluten_free,
        }}

        mongo.db.recipes.update_many(recipe, rec_update)
        flash("Recipe Successfully Updated")
        return redirect(url_for("profile", username=session["user"]))

    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# ---------------------------------------- Delete Recipe


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # Delete a recipe from the database
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")

    return redirect(url_for("profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=int(os.getenv("PORT")),
            debug=False)
