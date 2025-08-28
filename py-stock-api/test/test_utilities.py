from utilities.query_exception import QueryException


def test_query_exception():
    e = QueryException(code="123", message="Test Error Message")
    print(e.code)
    print(e)
    print(e.message)