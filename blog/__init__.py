__author__ = 'lizitai'

from flask import Flask
from flask_bootstrap import Bootstrap

blog = Flask(__name__)

bootstrap = Bootstrap(blog)

from blog.views import *