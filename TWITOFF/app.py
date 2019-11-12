from flask import Flask
from .models import DB
#now we make an app factory

def create_app():
    app = Flask(__name__)

    #add out config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    #now have the database know about the app
    #we want the database know about the app
    DB.init_app(app)


    @app.route('/')
    def root():
        return 'Welcome to Twitoff'
    return app


#set flask_app = TWITOFF:APP
#setflask run

#from TWITOFF.models import *
#u1=User(name='austen')
#t1=Tweet(text='wheee!!!!')
#db.session.add(u1)#
#db.session.add(t1)
#DB.session.committ()
