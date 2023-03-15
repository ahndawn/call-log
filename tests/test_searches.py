import unittest
from datetime import datetime, timedelta
from flask import Flask, url_for
from flask_testing import TestCase
from app import app, db, Call

class TestSearchRoutes(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def setUp(self):
        db.create_all()

        # Add test calls to database
        call1 = Call(date=datetime.now(), time=datetime.now().time(), customer_name='Test Customer 1', phone_number='123-456-7890', community='Test Community 1', area='Test Area 1', address='Test Address 1', customer_type='Test Customer Type 1', call_type='Test Call Type 1', comments='Test Comments 1', received_type='Test Received Type 1', response='Test Response 1', card='Test Card 1', database='Test Database 1', resolved='Test Resolved 1')
        call2 = Call(date=datetime.now(), time=datetime.now().time(), customer_name='Test Customer 2', phone_number='234-567-8901', community='Test Community 2', area='Test Area 2', address='Test Address 2', customer_type='Test Customer Type 2', call_type='Test Call Type 2', comments='Test Comments 2', received_type='Test Received Type 2', response='Test Response 2', card='Test Card 2', database='Test Database 2', resolved='Test Resolved 2')
        call3 = Call(date=datetime.now(), time=datetime.now().time(), customer_name='Test Customer 3', phone_number='345-678-9012', community='Test Community 3', area='Test Area 3', address='Test Address 3', customer_type='Test Customer Type 3', call_type='Test Call Type 3', comments='Test Comments 3', received_type='Test Received Type 3', response='Test Response 3', card='Test Card 3', database='Test Database 3', resolved='Test Resolved 3')
        db.session.add_all([call1, call2, call3])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_type_search(self):
        response = self.client.post('/type_search', data={'call_type': 'Call Type 1'})
        self.assert200(response)
        self.assertIn(b'Test Customer 1', response.data)
        self.assertIn(b'Test Customer 2', response.data)
        self.assertNotIn(b'Test Customer 3', response.data)

    def test_response_search(self):
        response = self.client.post('/response_search', data={'response': 'Response 1'})
        self.assert200(response)
        self.assertIn(b'Test Customer 1', response.data)
        self.assertNotIn(b'Test Customer 2', response.data)
        self.assertNotIn(b'Test Customer 3', response.data)

    def test_phone_search(self):
        response = self.client.post('/phone_search', data={'phone_number': '123-456-7890'})
        self.assert200(response)
        self.assertIn(b'Test Customer 1', response.data)
        self.assertNotIn(b'Test Customer 2', response.data)
        self.assertNotIn(b'Test Customer 3', response.data)

    def test_resolved_search(self):
        response = self.client.post(url_for('resolved_search'), data={'resolved': 'Yes'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Smith', response.data)
        self.assertNotIn(b'Jane Doe', response.data)
        self.assertIn(b'Bob Johnson', response.data)
        
    def test_name_search(self):
        response = self.client.post(url_for('name_search'), data={'customer_name': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Smith', response.data)
        self.assertNotIn(b'Jane Doe', response.data)
        self.assertNotIn(b'Bob Johnson', response.data)
        
    def test_community_search(self):
        response = self.client.post(url_for('community_search'), data={'community': 'Oakland'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Smith', response.data)
        self.assertNotIn(b'Jane Doe', response.data)
        self.assertNotIn(b'Bob Johnson', response.data)
        
    def test_area_search(self):
        response = self.client.post(url_for('area_search'), data={'area': 'East Bay'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Smith', response.data)
        self.assertNotIn(b'Jane Doe', response.data)
        self.assertIn(b'Bob Johnson', response.data)

if __name__ == '__main__':
    unittest.main()