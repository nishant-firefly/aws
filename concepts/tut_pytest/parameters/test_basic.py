# test_basic.py

import pytest

# Test using simple parameters for basic database connections (without user/password)
@pytest.mark.parametrize("db_connection", [
    {"db_type": "sqlite"},
    {"db_type": "postgresql"}
], indirect=True)
def test_basic_db_connection(db_connection):
    # Test the basic database connection setup
    assert db_connection["connected"] is True
    print(f"Test: Connected to {db_connection['db_type']} database")

@pytest.mark.parametrize("db_connection", [
    {"db_type": "sqlite"},
    {"db_type": "postgresql"}
], indirect=True)
def test_basic_db_query(db_connection):
    # Test executing a query on a basic database connection
    assert db_connection["connected"] is True
    print(f"Test: Executing query on {db_connection['db_type']} database")
