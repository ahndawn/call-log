from flask import Flask, flash, render_template, request, redirect, url_for, Response, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, time
from models import db, connect_db, Call
from forms import CallForm, PhoneSearchForm, ResponseSearchForm, ResolvedSearchForm, NameSearchForm, CommunitySearchForm, AreaSearchForm, TypeSearchForm
from queries import count_unresolved_calls, count_response_calls, count_calls
import csv
import os

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
    
    return render_template("home.html")

#######################
#Call Log routes
@app.route('/calls', methods=["GET", "POST"])
def calls():
    form = CallForm()
    count_unresolved = count_unresolved_calls()
    count_response = count_response_calls()
    count_call = count_calls()
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
                    resolved=form.resolved.data)
        db.session.add(call)
        db.session.commit()
        return redirect(url_for('calls'))
    calls = Call.query.all()
    return render_template('calls.html', form=form, calls=calls, count_unresolved=count_unresolved, count_response=count_response, count_call=count_call)

@app.route('/edit-call/<int:id>', methods=['GET', 'POST'])
def edit_call(id):
    call = Call.query.get_or_404(id)
    form = CallForm(obj=call)
    if form.validate_on_submit():
        form.populate_obj(call)
        db.session.commit()
        return redirect(url_for('calls'))
    return render_template('call.html', call=call, form=form)

@app.route('/calls/delete/<int:id>')
def delete_call(id):
    # retrieve the call from the database using the id parameter
    call = Call.query.get_or_404(id)

    # delete the call from the database
    db.session.delete(call)
    db.session.commit()

    # redirect to the calls page
    return redirect('/calls')

######################
# Search routes
@app.route('/type_search', methods=['GET', 'POST'])
def type_search():
    form = TypeSearchForm(request.form)
    calls = []
    if request.method == 'POST' and form.validate():
        call_type = form.call_type.data
        calls = Call.query.filter(Call.call_type.like(f'%{call_type}%')).all()
    return render_template('type_search.html', form=form, calls=calls)

@app.route('/response_search', methods=['GET', 'POST'])
def response_search():
    form = ResponseSearchForm(request.form)
    calls = []
    if request.method == 'POST' and form.validate():
        response = form.response.data
        calls = Call.query.filter(Call.response.like(f'%{response}%')).all()
    return render_template('response_search.html', form=form, calls=calls)

@app.route('/phone_search', methods=['GET', 'POST'])
def phone_search():
    form = PhoneSearchForm(request.form)
    calls = []
    if request.method == 'POST' and form.validate():
        phone_number = form.phone_number.data
        calls = Call.query.filter(Call.phone_number.like(f'%{phone_number}%')).all()
    return render_template('phone_search.html', form=form, calls=calls)

@app.route('/resolved_search', methods=['GET', 'POST'])
def resolved_search():
    form = ResolvedSearchForm(request.form)
    calls = []
    if request.method == 'POST' and form.validate():
        resolved = form.resolved.data
        calls = Call.query.filter(Call.resolved.like(f'%{resolved}%')).all()
    return render_template('resolved_search.html', form=form, calls=calls)

@app.route('/name_search', methods=['GET', 'POST'])
def name_search():
    form = NameSearchForm(request.form)
    calls = []
    if request.method == 'POST' and form.validate():
        customer_name = form.customer_name.data
        calls = Call.query.filter(Call.customer_name.like(f'%{customer_name}%')).all()
    return render_template('name_search.html', form=form, calls=calls)

@app.route('/community_search', methods=['GET', 'POST'])
def community_search():
    form = CommunitySearchForm(request.form)
    calls = []
    if request.method == 'POST' and form.validate():
        community = form.community.data
        calls = Call.query.filter(Call.community.like(f'%{community}%')).all()
    return render_template('community_search.html', form=form, calls=calls)

@app.route('/area_search', methods=['GET', 'POST'])
def area_search():
    form = AreaSearchForm(request.form)
    calls = []
    if request.method == 'POST' and form.validate():
        area = form.area.data
        calls = Call.query.filter(Call.area.like(f'%{area}%')).all()
    return render_template('area_search.html', form=form, calls=calls)


##########################
# archive calls to csv file
@app.route("/archive_calls", methods=["GET", "POST"])
def archive_calls():
    if request.method == 'POST':
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        calls = Call.query.filter(Call.date.between(start_date, end_date)).all()

        if not calls:
            flash('No calls found in selected date range.')
            return redirect(url_for('archive_calls'))

        archive_dir = os.path.join(app.root_path, 'archive')
        if not os.path.exists(archive_dir):
            os.makedirs(archive_dir)

        archive_filename = f'calls_{start_date.strftime("%Y-%m-%d")}_to_{end_date.strftime("%Y-%m-%d")}.csv'
        archive_path = os.path.join(archive_dir, archive_filename)

        with open(archive_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Time', 'Customer Name', 'Phone Number', 'Community', 'Area', 'Address', 'Customer Type', 'Call Type', 'Comments', 'Received Type', 'Response', 'Card', 'Database', 'Resolved'])
            for call in calls:
                writer.writerow([call.date.strftime('%Y-%m-%d'), call.time.strftime('%H:%M:%S'), call.customer_name, call.phone_number, call.community, call.area, call.address, call.customer_type, call.call_type, call.comments, call.received_type, call.response, call.card, call.database, call.resolved])

        Call.query.filter(Call.date.between(start_date, end_date)).delete()
        db.session.commit()

        flash(f'Calls successfully archived and removed. Archive file: {archive_filename}', 'success')
        return redirect(url_for('archive_calls'))

    return render_template('archive.html')