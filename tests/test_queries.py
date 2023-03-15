import unittest
from flask import url_for
from app import app, db, connect_db
from models import Call
from queries import count_unresolved_calls, count_response_calls, count_calls

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = connect_db('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_count_unresolved_calls(app, db):
        with app.app_context():
            # create two calls, one resolved and one unresolved
            call1 = Call(customer_name='John Doe', phone_number='1234567890', community='Test', area='Test', address='Test', customer_type='Residential', call_type='Test', comments='Test', received_type='Phone', response='yes', card='Test', database='Test', resolved='yes')
            call2 = Call(customer_name='Jane Doe', phone_number='0987654321', community='Test', area='Test', address='Test', customer_type='Residential', call_type='Test', comments='Test', received_type='Phone', response='no', card='Test', database='Test', resolved='no')
            db.session.add(call1)
            db.session.add(call2)
            db.session.commit()

            # check the number of unresolved calls
            unresolved_calls = count_unresolved_calls()
            assert unresolved_calls == 1


    def test_count_response_calls(app, db):
        with app.app_context():
            # create two calls, one needing response and one not needing response
            call1 = Call(customer_name='John Doe', phone_number='1234567890', community='Test', area='Test', address='Test', customer_type='Residential', call_type='Test', comments='Test', received_type='Phone', response='yes', card='Test', database='Test', resolved='yes')
            call2 = Call(customer_name='Jane Doe', phone_number='0987654321', community='Test', area='Test', address='Test', customer_type='Residential', call_type='Test', comments='Test', received_type='Phone', response='no', card='Test', database='Test', resolved='no')
            db.session.add(call1)
            db.session.add(call2)
            db.session.commit()

            # check the number of calls needing response
            response_calls = count_response_calls()
            assert response_calls == 1


    def test_count_calls(app, db):
        with app.app_context():
            # create two calls
            call1 = Call(customer_name='John Doe', phone_number='1234567890', community='Test', area='Test', address='Test', customer_type='Residential', call_type='Test', comments='Test', received_type='Phone', response='yes', card='Test', database='Test', resolved='yes')
            call2 = Call(customer_name='Jane Doe', phone_number='0987654321', community='Test', area='Test', address='Test', customer_type='Residential', call_type='Test', comments='Test', received_type='Phone', response='no', card='Test', database='Test', resolved='no')
            db.session.add(call1)
            db.session.add(call2)
            db.session.commit()

            # check the total number of calls
            total_calls = count_calls()
            assert total_calls == 2

if __name__ == '__main__':
    unittest.main()