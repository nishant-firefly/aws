"""
Top-level permissions.
Foreign key permissions for SQLAlchemy.
Nested field permissions for Elasticsearch.
"""
class PermissionError(Exception):
    """Exception raised for permission-related errors."""
    pass


class MasterSource:
    def __init__(self, user, master_permissions):
        self.user = user
        self.master_permissions = master_permissions

    def check_permissions(self, entity_name, action, columns, foreign_keys=None, nested_fields=None):
        """
        Check if the user has permissions for the specified action and columns on the entity.
        
        :param entity_name: Name of the entity (e.g., "User").
        :param action: The action to check (e.g., "select", "write").
        :param columns: List of columns being accessed.
        :param foreign_keys: Optional dictionary for foreign key permissions.
        :param nested_fields: Optional dictionary for nested field permissions.
        :raises PermissionError: If the user does not have permission to access any of the columns.
        """
        # Check permissions for top-level columns
        user_permissions = self.master_permissions.get(self.user, {}).get(entity_name, {}).get("permissions", {}).get(action, [])
        for column in columns:
            if column not in user_permissions:
                raise PermissionError(f"User '{self.user}' is not allowed to perform '{action}' on column '{column}' in entity '{entity_name}'.")

        # Check foreign key permissions if applicable
        if foreign_keys:
            foreign_key_permissions = self.master_permissions.get(self.user, {}).get(entity_name, {}).get("permissions", {}).get("foreign_keys", {})
            for fk_table, fk_columns in foreign_keys.items():
                allowed_fk_columns = foreign_key_permissions.get(fk_table, {}).get(action, [])
                for fk_column in fk_columns:
                    if fk_column not in allowed_fk_columns:
                        raise PermissionError(f"User '{self.user}' is not allowed to perform '{action}' on foreign key column '{fk_column}' in table '{fk_table}'.")

        # Check nested field permissions if applicable
        if nested_fields:
            nested_permissions = self.master_permissions.get(self.user, {}).get(entity_name, {}).get("permissions", {}).get("nested", {})
            for nested_table, nested_columns in nested_fields.items():
                allowed_nested_columns = nested_permissions.get(nested_table, {}).get(action, [])
                for nested_column in nested_columns:
                    if nested_column not in allowed_nested_columns:
                        raise PermissionError(f"User '{self.user}' is not allowed to perform '{action}' on nested field '{nested_column}' in nested table '{nested_table}'.")
