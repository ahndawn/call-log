from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, FloatField, SelectField, PasswordField, SubmitField, EmailField, TextAreaField, FieldList, FormField, IntegerField, DateField, TimeField, BooleanField
from wtforms.validators import InputRequired, length, optional, email, DataRequired, Email
from datetime import datetime

class CallForm(FlaskForm):
    date = DateField("Date", validators=[DataRequired()])
    time = TimeField("Time", validators=[DataRequired()])
    customer_name = StringField("Customer Name", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    community = SelectField("Community", choices= [(''), ("Hunter's Run"), ("Ibis"), ("PGA Nat")])
    area = SelectField("Area", choices=[(''), ('north'), ('northwest'), ('northeast'), ('central-west'), ('central'), ('central-east'), ('southeast'), ('south'), ('southwest'), ('ocean')], validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    customer_type = SelectField("Customer Type", choices=[('existing'),('new')], validators=[DataRequired()])
    call_type = SelectField("Call Type", choices=[('schedule'),('complaint'), ('payment'), ('estimate')], validators=[DataRequired()])
    comments = StringField("Comments")
    received_type = SelectField("Received Type", choices=[('msg'), ('call'), ('rollover')],validators=[DataRequired()])
    response = SelectField("Response", choices=[('yes'), ('no')])
    card = SelectField("Card", choices=[('yes'), ('no')])
    database = SelectField("Database", choices=[('yes'), ('no')])
    resolved = SelectField("Resolved", choices=[('yes'), ('no')])

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


class CustomerForm(FlaskForm):
    last_name = StringField('Last Name', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    email_address = StringField('Email Address', validators=[DataRequired(), Email()])
    notes = TextAreaField('Notes')
    address1 = StringField('Address 1', validators=[DataRequired()])
    address2 = StringField('Address 2')
    community = StringField('Community', validators=[DataRequired()])
    area = StringField('Area', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])