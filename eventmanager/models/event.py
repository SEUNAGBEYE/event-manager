from eventmanager import db
from .basemodel import BaseModel

class Event(db.Model, BaseModel):
  center_id = db.Column(db.Integer, db.ForeignKey('center.id'))
  center = db.relationship('Center', backref=db.backref('events', lazy='dynamic'))
  status = db.Column(db.Boolean(), default=False)
