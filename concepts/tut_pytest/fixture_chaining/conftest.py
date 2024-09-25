# conftest.py
import pytest

# Fixture to simulate setting up and tearing down a database connection
@pytest.fixture(scope="module")
def db_connection():
    # Setup: Establish a database connection
    print("Setting up database connection")
    connection = {"connected": True}
    
    # Yield the connection to the dependent fixture or test function
    yield connection
    
    # Teardown: Close the database connection after all module tests are done
    print("Tearing down database connection")
    connection["connected"] = False

# Fixture that depends on db_connection to create a session
@pytest.fixture(scope="module")
def db_session(db_connection):
    # Setup: Initialize a session using the active database connection
    print("Setting up database session")
    session = {"session_active": True, "db_connection": db_connection}
    
    # Yield the session to the test function
    yield session
    
    # Teardown: Close the session after all module tests are done
    print("Tearing down database session")
    session["session_active"] = False
