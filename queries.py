from models import Call

# counts number of unresolved calls
def count_unresolved_calls():
    unresolved_calls = Call.query.filter_by(resolved="no").count()
    return unresolved_calls

def count_response_calls():
    response_calls = Call.query.filter_by(response="no").count()
    return response_calls