import os
from datetime import datetime, timedelta
from io import StringIO

import pytest
from flask import url_for
from app import connect_db, db, app
from models import Call


@pytest.fixture
def app():
    app = connect_db()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


def test_archive_calls_get(client):
    response = client.get(url_for('archive_calls'))
    assert response.status_code == 200
    assert b'Archive Calls' in response.data


def test_archive_calls_post(client):
    # Create a call to be archived
    call = Call(
        date=datetime.now().date(),
        time=datetime.now().time(),
        customer_name='Test Customer',
        phone_number='123-456-7890',
        community='Test Community',
        area='Test Area',
        address='Test Address',
        customer_type='Test Customer Type',
        call_type='Test Call Type',
        comments='Test Comments',
        received_type='Test Received Type',
        response='Test Response',
        card='Test Card',
        database='Test Database',
        resolved='Test Resolved'
    )
    db.session.add(call)
    db.session.commit()

    # Post to archive the call
    start_date = datetime.now().date() - timedelta(days=1)
    end_date = datetime.now().date()
    response = client.post(
        url_for('archive_calls'),
        data={
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d')
        }
    )
    assert response.status_code == 302

    # Check that the call was archived
    calls = Call.query.all()
    assert not calls

    # Check that the archive file was created and contains the call
    archive_dir = os.path.join(client.application.root_path, 'archive')
    archive_filename = f'calls_{start_date.strftime("%Y-%m-%d")}_to_{end_date.strftime("%Y-%m-%d")}.csv'
    archive_path = os.path.join(archive_dir, archive_filename)
    assert os.path.isfile(archive_path)
    with open(archive_path, 'r') as f:
        csv_data = f.read()
        assert 'Test Customer' in csv_data