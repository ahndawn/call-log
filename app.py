from flask import Flask, flash, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, time
from models import db, connect_db, Call
from forms import CallForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = '2mtikn$u'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

with app.test_request_context():    
    connect_db(app)
    db.create_all()

########################
#HOME
@app.route('/')
def home():
    """Shows Home page"""
    
    return render_template("base.html")

#######################
#Call Log routes
@app.route('/calls', methods=["GET", "POST"])
def calls():
    form = CallForm()
    if request.method == "POST" and form.validate():
        call = Call(date=form.date.data, 
                    time=form.time.data,
                    customer_name=form.customer_name.data,
                    phone_number=form.phone_number.data,
                    community=form.community.data,
                    area=form.area.data,
                    address=form.address.data,
                    customer_type=form.customer_type.data,
                    call_type=form.call_type.data,
                    comments=form.comments.data,
                    received_type=form.received_type.data,
                    response=form.response.data,
                    card=form.card.data,
                    database=form.database.data,
                    resolved=form.resolved.data,
                    booked=form.booked.data)
        db.session.add(call)
        db.session.commit()
        return redirect(url_for('calls'))
    calls = Call.query.all()
    return render_template('calls.html', form=form, calls=calls)

@app.route('/edit-call/<int:id>', methods=['GET', 'POST'])
def edit_call(id):
    call = Call.query.get_or_404(id)
    form = CallForm(obj=call)
    if form.validate_on_submit():
        form.populate_obj(call)
        edited_call = Call(date=form.date.data, 
                    time=form.time.data,
                    customer_name=form.customer_name.data,
                    phone_number=form.phone_number.data,
                    community=form.community.data,
                    area=form.area.data,
                    address=form.address.data,
                    customer_type=form.customer_type.data,
                    call_type=form.call_type.data,
                    comments=form.comments.data,
                    received_type=form.received_type.data,
                    response=form.response.data,
                    card=form.card.data,
                    database=form.database.data,
                    resolved=form.resolved.data,
                    booked=form.booked.data)
        edited_call=call
        db.session.add(edited_call)
        db.session.commit()
        flash('Call updated successfully', 'success')
        return redirect(url_for('calls'))
    return render_template('calls.html', call=call, form=form)

@app.route('/call', methods=['GET', 'POST'])
@app.route('/call/<int:id>', methods=['GET', 'POST'])
def call(id=None):
    if id:
        call = Call.query.get_or_404(id)
    else:
        call = Call()

    if request.method == 'POST':
        call.date = request.form['date']
        call.time = request.form['time']
        call.customer_name = request.form['customer_name']
        call.phone_number = request.form['phone_number']
        call.community = request.form['community']
        call.area = request.form['area']
        call.address = request.form['address']
        call.customer_type = request.form['customer_type']
        call.call_type = request.form['call_type']
        call.comments = request.form['comments']
        call.received_type = request.form['received_type']
        call.response = request.form['response']
        call.card = request.form['card']
        call.database = request.form['database']
        call.resolved = request.form['resolved']
        call.booked = request.form['booked']

        db.session.add(call)
        db.session.commit()

        return redirect(url_for('calls'))

    return render_template('call.html', call=call)