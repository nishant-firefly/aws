# test_another_database.py
def test_another_db_session_active(db_session):
    # This test module gets its own db_session and db_connection
    assert db_session["session_active"] is True
    assert db_session["db_connection"]["connected"] is True
    print("Test: Another module - Database session is active")

def test_another_db_operation(db_session):
    # Another database operation in this module
    assert db_session["session_active"] is True
    assert db_session["db_connection"]["connected"] is True
    print("Test: Another module - Database operation executed")
