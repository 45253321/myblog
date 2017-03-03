#encoding=utf-8
__author__ = 'lizitai'
from blog import blog,models,db
from flask import render_template, request, session, redirect, abort ,flash, url_for,g
from forms import AuthorForm
from blog import login_manager
from flask_login import login_required,login_user,logout_user,current_user
login_manager.login_view = 'login'

@blog.route('/')
@login_required
def index():
    return render_template('index.html',name=u"李飞扬")

@blog.route('/wife')
@login_required
def wife():
    return render_template('index.html',name=u'聂立立')

@blog.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@blog.before_request
def before_request():
    g.user = current_user

@blog.route('/login', methods=['GET','POST'])
def login():
    af = AuthorForm()
    if af.validate_on_submit():
        user =  models.Author.query.filter_by(name=af.name.data, passwd=af.passwd.data).first()
        if not user:
            user = models.Author(af.name.data, af.passwd.data)
            db.session.add(user)
            db.session.commit()
        login_user(user)
        flash("User successful login")
        return redirect(request.args.get('next') or url_for('index'))
    else:
        return render_template('login.html', aform = af)



@login_manager.user_loader

def load_user(id):
    return models.Author.query.get(int(id))

