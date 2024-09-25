# conftest.py
import pytest

# Function-scoped fixture (default)
@pytest.fixture
def function_fixture():
    print("Setting up function-scoped fixture")
    return {"counter": 0}

# Class-scoped fixture
@pytest.fixture(scope="class")
def class_fixture():
    print("Setting up class-scoped fixture")
    return {"counter": 0}

# Module-scoped fixture
@pytest.fixture(scope="module")
def module_fixture():
    print("Setting up module-scoped fixture")
    return {"counter": 0}

# Session-scoped fixture
@pytest.fixture(scope="session")
def session_fixture():
    print("Setting up session-scoped fixture")
    return {"counter": 0}
