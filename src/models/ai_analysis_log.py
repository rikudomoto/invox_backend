from flask_marshmallow import Marshmallow

from src.database import db


ma = Marshmallow()


class AiAnaLogModel(db.Model):
  __tablename__ = 'ai_analysis_log'

  id	= db.Column(db.Integer, autoincrement=True, primary_key=True)
  image_path	= db.Column(db.VARCHAR(255), default= None)
  success	= db.Column(db.Boolean)
  message	= db.Column(db.VARCHAR(255), default= None)
  class_label	= db.Column(db.Integer, default= None)
  confidence	= db.Column(db.Numeric(5,4), default= None)
  request_timestamp	= db.Column(db.DateTime(6), default= None)
  response_timestamp	= db.Column(db.DateTime(6), default= None)

  @classmethod
  def insert(cls, insert_data):
    insert_model = AiAnaLogModel()
    insert_model.image_path = insert_data.image_path
    insert_model.success = insert_data.success
    insert_model.message = insert_data.message
    insert_model.class_label = insert_data.class_label
    insert_model.confidence = insert_data.confidence
    insert_model.request_timestamp = insert_data.request_timestamp
    insert_model.response_timestamp = insert_data.response_timestamp
    db.session.add(insert_model)
    db.session.commit()