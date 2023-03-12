from models import Call

# counts number of unresolved calls
def count_unresolved_calls():
    unresolved_calls = Call.query.filter_by(resolved="no").count()
    return unresolved_calls

# counts number of calls needing response
def count_response_calls():
    response_calls = Call.query.filter_by(response="no").count()
    return response_calls

# count the total number of calls in the database
def count_calls():
    total_calls = Call.query.count() 
    return total_calls
