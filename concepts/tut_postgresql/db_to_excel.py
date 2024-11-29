import pandas as pd
from sqlalchemy import create_engine
import psycopg2

# Database connection details
DB_CONFIG = {
    "user": "postgres",
    "password": "123",
    "host": "localhost",
    "port": "5432",
    "database": "practice"
}

# List of tables to export
tables_to_export = ["departments", "employee_project", "employees"]

def create_db_connection():
    # Create a connection to the PostgreSQL database
    conn = psycopg2.connect(
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
        database=DB_CONFIG["database"]
    )
    return conn

def export_tables_to_excel(tables, output_file):
    conn = create_db_connection()
    cursor = conn.cursor()
    
    # Open an Excel writer to write multiple sheets
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        for table in tables:
            try:
                # Fetch all rows from the table
                cursor.execute(f"SELECT * FROM {table}")
                rows = cursor.fetchall()

                # Get column names from cursor description
                columns = [desc[0] for desc in cursor.description]

                # Convert rows to Pandas DataFrame
                df = pd.DataFrame(rows, columns=columns)

                # Write DataFrame to Excel sheet
                df.to_excel(writer, sheet_name=table, index=False)
                print(f"Exported table '{table}' to Excel.")
            except Exception as e:
                print(f"Failed to export table '{table}': {e}")

    # Close cursor and connection
    cursor.close()
    conn.close()
    print(f"Data successfully exported to {output_file}")

if __name__ == "__main__":
    output_file = "postgres_tables.xlsx"
    export_tables_to_excel(tables_to_export, output_file)
