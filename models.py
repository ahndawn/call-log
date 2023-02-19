from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, time, date

db = SQLAlchemy()

class Call(db.Model):
    __tablename__='call'
    id = db.Column(db.Integer, primary_key=True)
    date= db.Column(db.Date, nullable =False)
    time = db.Column(db.Time, nullable=False)
    customer_name = db.Column(db.String(20), nullable = False)
    phone_number = db.Column(db.String(20), nullable = False)
    community = db.Column(db.String(64), nullable=True)
    area = db.Column(db.String(64), nullable=True)
    address = db.Column(db.String(256), nullable=False)
    customer_type = db.Column(db.String(64), nullable=False)
    call_type = db.Column(db.String(64), nullable=False)
    comments = db.Column(db.String(64), nullable=False)
    received_type = db.Column(db.String(64), nullable=False)
    response = db.Column(db.String(3), nullable=True, default=False)
    card = db.Column(db.String(3), nullable=True, default=False)
    database = db.Column(db.String(3), nullable=True, default=False)
    resolved = db.Column(db.String(3), nullable=True, default=False)
    booked = db.Column(db.String(3), nullable=True, default=False)

    # @classmethod
    # def get_checkbox_value(cls, checkbox_input_value):
    #     return checkbox_input_value == 'on'
    
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)