

from flask_script import Manager
from blog import blog

manager = Manager(blog)

@manager.command
def blog():
    blog.run(debug=True)

@manager.command
def hello():
    print "hello world"

if __name__ == '__main__':
    blo