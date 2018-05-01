from eventmanager import db

class BaseModel():
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), unique=True, nullable=False)

  def __repr__(self):
      return '<Center %r>' % self.name