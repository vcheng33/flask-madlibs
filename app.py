from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

# silly_story is a new instance of Stories. It has text and story
from stories import all_stories, all_stories_names

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def display_story_options():
    """ Returns drop down to select a story """
    return render_template("story_selection.html", stories=all_stories_names)

@app.get("/questions")
def display_homepage():
    """ Returns homepage """
    chosen_story = request.form.get("name")
    return chosen_story
    # return render_template("questions.html", words=story_template.prompts)
    #words probably not best name

# @app.get("/story")
# def return_story(story_template):
#     """generates story text and renders HTML"""
#     story_text = story_template.generate(request.args)
#     return render_template("story.html", content=story_text)
