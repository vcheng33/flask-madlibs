from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

# silly_story is a new instance of Stories. It has text and story
from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def index():
    """ Returns homepage """
    return render_template("questions.html", words=silly_story.prompts)
    #words probably not best name

@app.get("/story")
def return_story():
    """generates story text and renders HTML"""
    story_text = silly_story.generate(request.args)
    return render_template("story.html", content=story_text)
