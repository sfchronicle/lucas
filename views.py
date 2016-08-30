from flask import render_template, redirect, url_for, request

from app import app, db, freezer
from models import *


# Project Title
app.config['PROJ_TITLE'] = 'An exclusive first look at the collection of the Lucas Museum of Narrative Art'

# Site Path/Slug
app.config['PATH'] = 'lucas-art'

# Project Category for Omniture 
app.config['CATEGORY'] = 'Arts & Entertainment'

# Project Hashtag
app.config['HASHTAG'] = ''

"""
slug completes:
- twitter:url
- og:image/Facebook image preview
- Twitter/Facebook share url
- url for email body

title:
- Page title
- og:title/Facebook headline
- email subject
- twitter:title

description:
- meta description
- og:description/Facebook description

twitter_text:
- text that appears on tweet

"""

@app.route('/')
def index():
    return render_template('index.html',
    	slug='',
    	title="An exclusive first look at the collection of the Lucas Museum of Narrative Art",
    	description="Charles Desmarais: It seems almost everyone has an opinion about filmmaker George Lucas' collection, but no journalist, critic or casual art fan has seen it - until now.",
    	twitter_text="Art of Storytelling: An exclusive first look into the Lucas Museum of Narrative Art.")
