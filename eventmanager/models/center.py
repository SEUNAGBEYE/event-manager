from eventmanager import db
from .basemodel import BaseModel

class Center(db.Model, BaseModel):
  user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
  user = db.relationship('User', backref=db.backref('centers', lazy='dynamic'))
  location = db.Column(db.String(80), nullable=False)
