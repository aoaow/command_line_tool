"""
This file creates basic operations for an internal database using sqlite
"""
import sqlite3

def connect_db(db_name='database.db'):
    """
    Connect to the SQLite database.

    Parameters:
        db_name (str): The name of the database file.

    Returns:
        sqlite3.Connection: A connection object to the SQLite database.
    """
    conn = sqlite3.connect(db_name)
    return conn

def create_table():
    """
    Create the 'records' table in the database if it doesn't exist.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            value TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_record(name, value):
    """
    Add a new record to the database.

    Parameters:
        name (str): The name of the record.
        value (str): The value of the record.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO records (name, value) VALUES (?, ?)', (name, value))
    conn.commit()
    conn.close()

def view_records():
    """
    Retrieve all records from the database.

    Returns:
        list: A list of tuples containing record data.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM records')
    results = cursor.fetchall()
    conn.close()
    return results

def update_record(record_id, name, value):
    """
    Update an existing record in the database.

    Parameters:
        record_id (int): The ID of the record to update.
        name (str): The new name of the record.
        value (str): The new value of the record.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE records SET name = ?, value = ? WHERE id = ?', (name, value, record_id))
    conn.commit()
    conn.close()

def delete_record(record_id):
    """
    Delete a record from the database.

    Parameters:
        record_id (int): The ID of the record to delete.
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM records WHERE id = ?', (record_id,))
    conn.commit()
    conn.close()
