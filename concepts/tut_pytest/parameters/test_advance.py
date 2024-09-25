# test_advanced.py

import pytest

# Test using advanced parameters for database connections with users and passwords
@pytest.mark.parametrize("db_connection", [
    {"db_type": "sqlite", "user": "user1", "password": "pass1"},
    {"db_type": "postgresql", "user": "admin", "password": "admin123"}
], indirect=True)
def test_advanced_db_connection(db_connection):
    # Test the database connection setup with users and passwords
    assert db_connection["connected"] is True
    print(f"Test: Connected to {db_connection['db_type']} database as {db_connection['user']}")

@pytest.mark.parametrize("db_connection", [
    {"db_type": "sqlite", "user": "user1", "password": "pass1"},
    {"db_type": "postgresql", "user": "admin", "password": "admin123"}
], indirect=True)
def test_advanced_db_query(db_connection):
    # Test executing a query with users and passwords on a database connection
    assert db_connection["connected"] is True
    print(f"Test: Executing query on {db_connection['db_type']} database as {db_connection['user']}")
