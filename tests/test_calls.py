import unittest
from app import app, db
from models import Call
from datetime import date, time, datetime

class CallsTests(unittest.TestCase):
    
    def setUp(self):
        """Stuff to do before every test."""
        
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///calls-test'
        db.create_all()
        
    def tearDown(self):
        """Stuff to do after each test."""
        
        db.session.rollback()
        db.drop_all()
        
    def test_calls_get(self):
        """Test that the calls page loads."""
        
        response = self.client.get('/calls')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Calls Log', response.data)
        
    def test_calls_post(self):
        """Test adding a new call."""
        
        data = {
            'date': '2022-02-20',
            'time': '12:00',
            'customer_name': 'John Smith',
            'phone_number': '555-555-5555',
            'community': 'Community A',
            'area': 'Area 1',
            'address': '123 Main St.',
            'customer_type': 'Residential',
            'call_type': 'Complaint',
            'comments': 'Noisy neighbors',
            'received_type': 'Phone',
            'response': 'Sent officer to check',
            'card': 'ABC123',
            'database': 'COPsync',
            'resolved': False
        }
        response = self.client.post('/calls', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Smith', response.data)
        
        call = Call.query.filter_by(customer_name='John Smith').one()
        self.assertIsNotNone(call)
        self.assertEqual(call.customer_name, 'John Smith')
        
    def test_calls_post_invalid(self):
        """Test adding a new call with invalid data."""
        
        data = {
            'date': '2022-02-20',
            'time': '12:00',
            'customer_name': '',
            'phone_number': '555-555-5555',
            'community': 'Community A',
            'area': 'Area 1',
            'address': '123 Main St.',
            'customer_type': 'Residential',
            'call_type': 'Complaint',
            'comments': 'Noisy neighbors',
            'received_type': 'Phone',
            'response': 'Sent officer to check',
            'card': 'ABC123',
            'database': 'COPsync',
            'resolved': False
        }
        response = self.client.post('/calls', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This field is required.', response.data)
        
        calls = Call.query.all()
        self.assertEqual(len(calls), 0)


    def test_delete_call(client, auth, call_factory):
        # create a user and login
        auth.login()

        # create a call
        call = call_factory()

        # delete the call
        response = client.get(f'/calls/delete/{call.id}')

        # check that the call was deleted
        assert response.status_code == 302
        assert Call.query.get(call.id) is None

    def test_edit_call(client, auth, call_factory):
        # create a user and login
        auth.login()

        # create a call
        call = call_factory()

        # submit the form to edit the call
        response = client.post(f'/edit-call/{call.id}', data={
            'date': '2022-02-20',
            'time': '12:00',
            'customer_name': 'John Doe',
            'phone_number': '555-555-5555',
            'community': 'Community',
            'area': 'Area',
            'address': '123 Main St',
            'customer_type': 'Residential',
            'call_type': 'Type',
            'comments': 'Comments',
            'received_type': 'Phone',
            'response': 'Response',
            'card': 'Card',
            'database': 'Database',
            'resolved': True
        })

        # check that the call was updated
        assert response.status_code == 302
        assert call.date == datetime.date(2022, 2, 20)
        assert call.time == datetime.time(12, 0)
        assert call.customer_name == 'John Doe'
        assert call.phone_number == '555-555-5555'
        assert call.community == 'Community'
        assert call.area == 'Area'
        assert call.address == '123 Main St'
        assert call.customer_type == 'Residential'
        assert call.call_type == 'Type'
        assert call.comments == 'Comments'
        assert call.received_type == 'Phone'
        assert call.response == 'Response'
        assert call.card == 'Card'
        assert call.database == 'Database'
        assert call.resolved == True

if __name__ == '__main__':
    unittest.main()