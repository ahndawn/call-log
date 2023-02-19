from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, FloatField, SelectField, PasswordField, SubmitField, EmailField, TextAreaField, FieldList, FormField, IntegerField, DateField, TimeField, BooleanField
from wtforms.validators import InputRequired, length, optional, email, DataRequired
from datetime import datetime

class CallForm(FlaskForm):
    date = DateField("Date", validators=[DataRequired()])
    time = TimeField("Time", validators=[DataRequired()])
    customer_name = StringField("Customer Name", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    community = StringField("Community", validators=[DataRequired()])
    area = StringField("Area", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    customer_type = SelectField("Customer Type", choices=[('existing'),('new')], validators=[DataRequired()])
    call_type = SelectField("Call Type", choices=[('schedule'),('complaint'), ('payment'), ('estimate')], validators=[DataRequired()])
    comments = StringField("Comments")
    received_type = SelectField("Received Type", choices=[('msg'), ('call'), ('rollover')],validators=[DataRequired()])
    response = StringField("Response")
    card = StringField("Card")
    database = StringField("Database")
    resolved = StringField("Resolved")
    booked = StringField("Booked")

