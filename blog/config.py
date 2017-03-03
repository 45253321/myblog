__author__ = 'fly.li'
import os
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/fly.li/test.db'
SECRET_KEY = os.urandom(24)
