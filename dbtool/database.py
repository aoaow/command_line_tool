'''
This file creates basic operations for an internal database using sqlite
'''
import sqlite3

def connect_db(db_name='database.db'):
    conn = sqlite3.connect(db_name)
    return conn

def create_table():
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
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO records (name, value) VALUES (?, ?)', (name, value))
    conn.commit()
    conn.close()

def view_records():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM records')
    results = cursor.fetchall()
    conn.close()
    return results

def update_record(record_id, name, value):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE records SET name = ?, value = ? WHERE id = ?', (name, value, record_id))
    conn.commit()
    conn.close()

def delete_record(record_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM records WHERE id = ?', (record_id,))
    conn.commit()
    conn.close()
