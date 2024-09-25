import os
# test_app.py
def test_db_connection(db_connection):
    # Test: Use the database connection fixture
    assert db_connection["connected"] is True
    print("Test: Database connection is active")

def test_temp_file_creation(temp_file):
    # Test: Use the temporary file fixture
    assert os.path.exists(temp_file)
    with open(temp_file, "r") as f:
        content = f.read()
    
    assert content == "Temporary data"
    print(f"Test: Temporary file content: {content}")

def test_db_and_temp_file(db_connection, temp_file):
    # Test: Use both the database connection and the temporary file
    assert db_connection["connected"] is True
    assert os.path.exists(temp_file)

    # Modify the temporary file
    with open(temp_file, "a") as f:
        f.write("\nAdditional data")
    
    # Verify that both the file and database connection are functioning
    with open(temp_file, "r") as f:
        content = f.read()

    assert "Additional data" in content
    print(f"Test: Modified temporary file content: {content}")
    print("Test: Database connection is still active")
