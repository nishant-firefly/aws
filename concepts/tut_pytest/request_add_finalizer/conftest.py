"""
More control than a yield
How request.addfinalizer Works
    Setup: You perform setup tasks (e.g., opening a database connection).
    Finalizer registration: You use request.addfinalizer() to register one or more teardown functions.
    Teardown: After the test or fixture completes, the finalizer is called to perform the necessary cleanup.

    
How the Test Workflow Operates:
    The expensive resource is set up before the test (e.g., initializing a database connection).
    The test runs, using the resource.
    The finalizer registered with request.addfinalizer() is executed to clean up the resource (e.g., closing the database connection).


Setting up expensive resource: This is the setup code within the fixture.
Test is running with expensive resource: This is the test logic being executed.
Tearing down expensive resource: This is the finalizer registered by request.addfinalizer being called after the test completes.

"""

import pytest

# Fixture that simulates setting up and tearing down an expensive resource
@pytest.fixture
def setup_expensive_resource(request):
    # Setup: Initialize the expensive resource (e.g., database connection)
    resource = {"resource_active": True}
    print("Setting up expensive resource")

    # Define the finalizer function for cleanup
    def finalizer():
        print("Tearing down expensive resource")
        resource["resource_active"] = False

    # Register the finalizer using request.addfinalizer
    request.addfinalizer(finalizer)

    # Return the resource to the test
    return resource
