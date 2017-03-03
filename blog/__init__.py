__author__ = 'lizitai'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

blog = Flask(__name__)

blog.config.from_pyfile('config.py')

db = SQLAlchemy(blog)
bootstrap = Bootstrap(blog)
login_manager = LoginManager(blog)

from blog.views import *
