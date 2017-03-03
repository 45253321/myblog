
from flask_script import Manager
from blog import blog

manager = Manager(blog)

@manager.command
def hello():
    print "hello world"

from blog.models import *
from flask_migrate import Migrate, MigrateCommand
migrate = Migrate(blog, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()