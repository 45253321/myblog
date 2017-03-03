__author__ = 'fly.li'

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired


class AuthorForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    passwd = PasswordField('passwd', validators=[DataRequired()])

