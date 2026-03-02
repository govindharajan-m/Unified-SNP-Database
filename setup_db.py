import sqlite3
import os

def setup_database():
    # Define paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'genomics.db')
    schema_path = os.path.join(base_dir, 'schema.sql')
    
    # Check if schema exists
    if not os.path.exists(schema_path):
        print(f"Error: Schema file not found at {schema_path}")
        return

    # Connect to SQLite (this creates the file if it doesn't exist)
    print(f"Connecting to database at {db_path}...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON")
    
    # Read and execute the schema
    print("Executing schema...")
    with open(schema_path, 'r') as file:
        schema_script = file.read()
        
    try:
        cursor.executescript(schema_script)
        conn.commit()
        print("Database schema successfully created!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    setup_database()
