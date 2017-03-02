#encoding=utf-8
__author__ = 'lizitai'
from blog import blog
from flask import  render_template

@blog.route('/')
def index():
    return render_template('index.html',name=u"李飞扬")

@blog.route('/wife')
def wife():
    return render_template('index.html',name=u'聂立立')