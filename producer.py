import sqlite3

DB_FILE = 'queue.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            status TEXT
        )
    ''')
    cursor.execute('DELETE FROM tasks') 
    conn.commit()
    conn.close()

def add_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (id, status) VALUES (?, ?)", (task_id, 'pending'))
    conn.commit()
    conn.close()
    print(f"Dodano zadanie {task_id} do kolejki.")

if __name__ == "__main__":
    init_db()
    for i in range(1, 101):
        add_task(f"Zadanie_{i}")
