from eventmanager import db
from .basemodel import BaseModel

facilities_centers = db.Table('facilities_centers', 
  db.Column('id', db.Integer(), primary_key = True),
  db.Column('facility_id', db.Integer(), db.ForeignKey('facility.id')),
  db.Column('center_id', db.Integer(), db.ForeignKey('center.id')))

class Facility(db.Model, BaseModel):
  centers = db.relationship('Center', secondary=facilities_centers,
                            backref=db.backref('facilities', lazy='dynamic'))
