from eventmanager import db
from werkzeug.security import generate_password_hash, check_password_hash

roles_users = db.Table('roles_users', 
  db.Column('id', db.Integer(), primary_key = True),
  db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
  db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(120))
  last_name = db.Column(db.String(120))
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.Text(), nullable=False)
  roles = db.relationship('Role', secondary=roles_users, 
                          backref=db.backref('users', lazy='dynamic'))
  
  def hash_password(self):
    self.password = generate_password_hash(self.password)
  

  def is_admin(self):
    return 'admin' in self.roles


  # def __repr__(self):
  #     return '<User {first_name} {last_name}>'\
  #     .format(self.first_name, self.last_name)