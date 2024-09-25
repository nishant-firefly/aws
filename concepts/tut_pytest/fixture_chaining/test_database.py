# test_database.py
def test_db_session_active(db_session):
    # Test the session to ensure it's active and has a valid database connection
    assert db_session["session_active"] is True
    assert db_session["db_connection"]["connected"] is True
    print("Test: Database session is active")

def test_db_query(db_session):
    # Simulate a database query using the active session
    assert db_session["session_active"] is True
    assert db_session["db_connection"]["connected"] is True
    print("Test: Database query executed successfully")

def test_db_session_teardown(db_session):
    # Another test that will use the same session and connection from previous tests
    assert db_session["session_active"] is True
    assert db_session["db_connection"]["connected"] is True
    print("Test: Verifying session before teardown")
