from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import config
from env import env
from eventmanager import create_app, db
from eventmanager.models import User, Center, Event, Facility, Role

app = create_app(env['ENV'] or 'development')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def seed_test_user():
    with app.app_context():
      user = User(first_name='Seun', last_name='Agbeye', email=env['EMAIL'],\
      password='mother1234')
      user.hash_password()
      db.session.add(user)
      db.session.commit()

if __name__ == '__main__':
  manager.run()

