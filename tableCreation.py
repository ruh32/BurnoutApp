import sqlite3

# Connect to the database and create a cursor
conn = sqlite3.connect('userDataTable.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    first_name TEXT,
    last_name TEXT,
    admin_flag NUMBER(1),
    age int,
    ethnicity TEXT,
    gender TEXT,
    occupation TEXT,
    active_ind NUMBER(1)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    user_id INTEGER PRIMARY KEY,
    date TEXT,
    question_responses TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS journal_entries (
    user_id INTEGER PRIMARY KEY,
    date TEXT,
    entry TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS responses (
    user_id INTEGER PRIMARY KEY,
    date TEXT,
    entry TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS user_resources (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    url TEXT,
    logo TEXT,
    description TEXT,
    active_ind NUMBER(1)
)
''')


conn.commit()
conn.close()
