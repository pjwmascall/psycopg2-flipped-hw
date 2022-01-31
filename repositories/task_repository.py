import psycopg2

def connect_to_database():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="task_manager"
        )
        cursor = connection.cursor()
        print("Opening connection to database...")
        return cursor, connection
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to database", error)

def execute_sql_statement(statement):
    try:
        cursor, connection = connect_to_database()
        cursor.execute(statement)
        return cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to database", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Database connection is closed")

def select(target, table):
    return f"SELECT {target} FROM {table}"

def delete(table, target, value):
    return f"DELETE FROM {table} WHERE {target} = '{value}'"

first_query = select("description", "tasks")

output = execute_sql_statement(first_query)
print(output)