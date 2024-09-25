"""
Fixture parameters allow you to pass arguments into a fixture, enabling you to run the same setup logic with different configurations or inputs. 
This is particularly useful when you want to test multiple scenarios with slight variations in the setup.

In this example, we will:

Simulate setting up different types of database connections (e.g., SQLite, PostgreSQL).
Use fixture parameters to modify the behavior of the db_connection fixture based on the database type.
Demonstrate how different test cases can reuse the same fixture but with different parameters to simulate various configurations.
How Fixture Parameters Work:
You use the pytest.mark.parametrize decorator or pass parameters to a fixture using the request object.
The fixture reads the parameters and adjusts the setup accordingly.

In advance Version we will test multiple aspects of your application by passing more complex parameters, such as database credentials, configurations, or different sets of data.
Simulate setting up different database connections with more detailed configurations.
"""
# conftest.py
# conftest.py
import pytest

# Fixture to simulate setting up a database connection with parameters
@pytest.fixture
def db_connection(request):
    # Access the parameter passed to the fixture
    config = request.param
    db_type = config["db_type"]
    user = config.get("user", None)  # user may not be present in basic tests
    password = config.get("password", None)

    # Setup based on the database type
    if db_type == "sqlite":
        print(f"Setting up SQLite connection" + (f" for user: {user}" if user else ""))
        connection = {"db_type": "sqlite", "connected": True, "user": user}
    elif db_type == "postgresql":
        print(f"Setting up PostgreSQL connection" + (f" for user: {user}" if user else ""))
        connection = {"db_type": "postgresql", "connected": True, "user": user}
    else:
        raise ValueError(f"Unsupported database type: {db_type}")

    # Yield the connection to the test function
    yield connection

    # Teardown: Close the database connection after the test
    print(f"Tearing down {db_type} connection" + (f" for user: {user}" if user else ""))
    connection["connected"] = False
