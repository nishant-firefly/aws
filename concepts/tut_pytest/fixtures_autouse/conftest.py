"""
Autouse fixtures in pytest are fixtures that are automatically applied to every test function in a module,
class, or session without explicitly requesting them. They are useful when you want to ensure that a fixture's 
setup and teardown logic is always applied without needing to specify it in each test.

However, autouse fixtures can sometimes obscure test dependencies because they run automatically, 
which can make tests harder to understand and debug. Thus, they should be used cautiously and only when 
it makes sense to apply setup and teardown logic to every test in a module, class, or session.

Should We Use Autouse Fixtures?
Pros:
    Convenience: Automatically applied to all tests without needing to be specified.
    Less boilerplate: Useful when you need a common setup for all tests and want to avoid repeating it.
Cons:
    Reduced test clarity: It's not always obvious when a fixture is being applied because it is not explicitly used in the test.
    Harder to debug: If an autouse fixture causes issues, it can be less clear which fixture is responsible, especially in large test suites.

Recommendation:
    Use autouse fixtures for things that are fundamental to every test in a module or session, such as setting environment variables or ensuring certain preconditions are met.
    Avoid using autouse for complex or optional setups that only some tests require.
"""
# conftest.py
import pytest

# Autouse fixture that logs the start and end of every test
@pytest.fixture(autouse=True)
def log_test_start_end():
    print("\n[LOG] Starting test")
    yield
    print("[LOG] Finished test")

# Autouse fixture that simulates setting up a database connection for every test
@pytest.fixture(autouse=True)
def db_connection():
    # Setup: Simulate establishing a database connection
    print("[DB] Setting up database connection")
    connection = {"connected": True}
    yield connection
    # Teardown: Simulate closing the database connection
    print("[DB] Tearing down database connection")
    connection["connected"] = False

"""Explanation 
Explanation of Autouse Fixtures in conftest.py:
log_test_start_end:
Logs a message at the start and end of each test.
The autouse=True means this fixture is automatically applied to every test in the test session 
without needing to be explicitly mentioned.
db_connection:
Simulates a database connection setup and teardown.
The autouse=True means this fixture will automatically run before and after every test, 
simulating the connection establishment and closure for each test without being explicitly requested in 
the test functions.
"""
