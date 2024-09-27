import pytest
from source import MasterSource, PermissionError

# Define the permissions data structure
master_permissions = {
    "User1": {
        "User": {
            "permissions": {
                "select": ["name", "email", "password"],  # Ensure "password" is included for top-level access
                "foreign_keys": {
                    "orders": {
                        "select": ["order_id", "order_date", "order_status"]  # Add "order_status" for foreign key access
                    }
                }
            }
        },
        "Document": {
            "permissions": {
                "select": ["title"],
                "nested": {
                    "comments": {
                        "select": ["comment_text", "commenter", "likes"]  # Add "likes" for nested field access
                    }
                }
            }
        }
    }
}

def test_master_source_top_level_permissions():
    source = MasterSource("User1", master_permissions)

    # Top-level permissions should pass
    source.check_permissions("User", "select", ["name", "email", "password"])

    # Test that accessing unauthorized column raises PermissionError
    with pytest.raises(PermissionError):
        source.check_permissions("User", "select", ["unknown_column"])


def test_master_source_foreign_key_permissions():
    source = MasterSource("User1", master_permissions)

    # Foreign key permissions should pass
    source.check_permissions("User", "select", ["name"], foreign_keys={"orders": ["order_id", "order_date", "order_status"]})

    # Test that accessing unauthorized foreign key column raises PermissionError
    with pytest.raises(PermissionError):
        source.check_permissions("User", "select", ["name"], foreign_keys={"orders": ["invalid_column"]})


def test_master_source_nested_field_permissions():
    source = MasterSource("User1", master_permissions)

    # Nested field permissions should pass
    source.check_permissions("Document", "select", ["title"], nested_fields={"comments": ["comment_text", "commenter", "likes"]})

    # Test that accessing unauthorized nested field raises PermissionError
    with pytest.raises(PermissionError):
        source.check_permissions("Document", "select", ["title"], nested_fields={"comments": ["invalid_field"]})
