"""
Fixture with yield: Setup and Teardown in Pytest
When testing with pytest, there are often situations where you need to set up a resource before running a test and clean up (or tear down) the resource after the test finishes. You can handle this using yield in a pytest fixture.

The code before yield is the setup step, and the code after yield is the teardown step. This is useful when you're working with things like:

Database connections
Temporary files or directories
External services
Network connections, etc.
How It Works:
Setup: The code before yield is executed before the test is run.
Yield: The value yielded is passed to the test function, allowing the test to use the resource.
Teardown: After the test completes, the code after yield is executed, which handles any necessary cleanup.

"""

# conftest.py
import pytest
import os

# Fixture to simulate setting up and tearing down a database connection
@pytest.fixture
def db_connection():
    # Setup: Establish database connection (simulated)
    print("Setting up database connection")
    connection = {"connected": True}
    
    # Yield the connection to the test function
    yield connection
    
    # Teardown: Close the connection after the test finishes
    print("Tearing down database connection")
    connection["connected"] = False

# Fixture to create and delete a temporary file
@pytest.fixture
def temp_file(tmp_path):
    # Setup: Create a temporary file
    file_path = tmp_path / "test_file.txt"
    print(f"Creating temporary file at: {file_path}")
    with open(file_path, "w") as f:
        f.write("Temporary data")

    # Yield the file path to the test function
    yield file_path

    # Teardown: Delete the temporary file after the test finishes
    print(f"Deleting temporary file at: {file_path}")
    if os.path.exists(file_path):
        os.remove(file_path)
