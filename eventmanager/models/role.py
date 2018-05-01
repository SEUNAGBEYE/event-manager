from eventmanager import db
from .basemodel import BaseModel

class Role(db.Model, BaseModel):
  description = db.Column(db.String(80), nullable=False)