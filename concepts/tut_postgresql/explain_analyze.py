import psycopg2
import pandas as pd
from tabulate import tabulate  # For printing tables
db_config = {
    "dbname": "practice",
    "user": "postgres",
    "password": "123",
    "host": "localhost",
    "port": "5432"
}
def run_explain_analyze(connection, queries):
    """
    Executes EXPLAIN ANALYZE for each query and captures execution details.
    """
    results = []
    cursor = connection.cursor()
    
    for query_name, query in queries.items():
        print(f"\nAnalyzing Query: {query_name}\n{'=' * 50}")
        explain_query = f"EXPLAIN ANALYZE {query}"
        
        try:
            cursor.execute(explain_query)
            explain_output = cursor.fetchall()
            execution_details = "\n".join([row[0] for row in explain_output])

            # Parse key metrics
            execution_time = [
                line for line in execution_details.split("\n") if "Execution Time" in line
            ]
            planning_time = [
                line for line in execution_details.split("\n") if "Planning Time" in line
            ]
            total_cost = [
                line for line in execution_details.split("\n") if "cost=" in line
            ]

            exec_time = float(execution_time[0].split(":")[1].strip().split(" ")[0]) if execution_time else None
            plan_time = float(planning_time[0].split(":")[1].strip().split(" ")[0]) if planning_time else None
            cost_range = total_cost[0].split("cost=")[1].split(" ")[0] if total_cost else "N/A"

            # Save the results, including the query text
            results.append({
                "Query Name": query_name,
                "Query Text": query.strip(),
                "Execution Time (ms)": exec_time,
                "Planning Time (ms)": plan_time,
                "Total Cost": cost_range
            })

        except Exception as e:
            print(f"Error analyzing query {query_name}: {e}")
            results.append({
                "Query Name": query_name,
                "Query Text": query.strip(),
                "Execution Time (ms)": None,
                "Planning Time (ms)": None,
                "Total Cost": "N/A"
            })

    cursor.close()
    return results


def print_table(results):
    """
    Print the query comparison results as a formatted table and return JSON with headers.
    """
    if not results:
        print("\nNo results to display.")
        return {"headers": [], "data": []}

    df = pd.DataFrame(results)
    
    if df.empty:
        print("\nNo data to display in the table.")
        return {"headers": [], "data": []}
    else:
        # Convert DataFrame to tabular format
        table = tabulate(df, headers="keys", tablefmt="grid", showindex=False)
        print("\nQuery Comparison Table:")
        print(table)

        # Convert DataFrame to JSON
        json_result = {
            "headers": df.columns.tolist(),
            "data": df.to_dict(orient="records")
        }

        return json_result



def explain_analyze(queries):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**db_config)
        # Run EXPLAIN ANALYZE and compare queries
        results = run_explain_analyze(connection, queries)
        return print_table(results)
    except Exception as e:
        print(f"Database connection error: {e}")
    
    finally:
        # Ensure always connection closes
        if connection:
            connection.close()

if __name__ == "__main__":
    # Define valid PostgreSQL queries to analyze
    from queries import query_salary_more_than_avg
    print(explain_analyze(query_salary_more_than_avg))
