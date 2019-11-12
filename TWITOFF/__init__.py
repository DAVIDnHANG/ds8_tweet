"""Entry point for our twitoff falsk app"""
from .app import create_app
#App is global variable
APP = create_app()

#run this in terminal with FLASK_app=twitcg off
