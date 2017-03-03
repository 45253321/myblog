__author__ = 'fly.li'

from blog import db


class Author(db.Model):

    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(120), unique=True)
    passwd = db.Column(db.String(120))
    article = db.relationship('Article',
                              backref='author', lazy='dynamic')

    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd



    def __repr__(self):
        return '<User:%r>'%(self.name)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


class Article(db.Model):

    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return '<title:%r author:%r>'%(self.title, self.author_id)