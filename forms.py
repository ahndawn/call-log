from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, FloatField, SelectField, PasswordField, SubmitField, EmailField, TextAreaField, FieldList, FormField, IntegerField, DateField, TimeField, BooleanField
from wtforms.validators import InputRequired, length, optional, email, DataRequired, Email
from datetime import datetime

class CallForm(FlaskForm):
    date = DateField("Date", validators=[DataRequired()])
    time = TimeField("Time", validators=[DataRequired()])
    customer_name = StringField("Customer Name", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    community = StringField("Community")
    area = SelectField("Area", choices=[(''), ('north'), ('northwest'), ('northeast'), ('central-west'), ('central'), ('central-east'), ('southeast'), ('south'), ('southwest'), ('ocean north'), ('ocean'), ('ocean south')])
    address = StringField("Address", validators=[DataRequired()])
    customer_type = SelectField("Customer Type", choices=[('existing'),('new'), ('?')], validators=[DataRequired()])
    call_type = SelectField("Call Type", choices=[('schedule'),('complaint'), ('payment'), ('estimate'), ('call out'), ('?')], validators=[DataRequired()])
    comments = StringField("Comments", validators=[DataRequired()])
    received_type = SelectField("Received Type", choices=[('msg'), ('call'), ('RO')],validators=[DataRequired()])
    response = SelectField("Response", choices=[('yes'), ('no')])
    card = SelectField("Card", choices=[('yes'), ('no')])
    database = SelectField("Database", choices=[('yes'), ('no')])
    resolved = SelectField("Resolved", choices=[('yes'), ('no')])

# Search Forms
class PhoneSearchForm(FlaskForm):
    phone_number = StringField('PHONE NUMBER:', validators=[DataRequired()])

class ResolvedSearchForm(FlaskForm):
    resolved = SelectField('RESOLVED:', choices=[('no'),('yes')], validators=[DataRequired()])

class NameSearchForm(FlaskForm):
    customer_name = StringField('CUSTOMER NAME:', validators=[DataRequired()])

class ResponseSearchForm(FlaskForm):
    response = SelectField('RESPONSE:', choices=[('no'),('yes')], validators=[DataRequired()])

class CommunitySearchForm(FlaskForm):
    community = StringField('COMMUNITY:', validators=[DataRequired()])

class AreaSearchForm(FlaskForm):
    area = StringField('AREA:', validators=[DataRequired()])

class TypeSearchForm(FlaskForm):
    call_type = SelectField('CALL TYPE:', choices=[('schedule'),('complaint'), ('payment'), ('estimate'), ('call out')], validators=[DataRequired()])
