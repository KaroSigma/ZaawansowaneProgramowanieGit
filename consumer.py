import sqlite3
import time

DB_FILE = 'queue.db'

def get_pending_task_and_update():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tasks WHERE status = 'pending' LIMIT 1")
    row = cursor.fetchone()
    
    if row:
        task_id = row[0]
        cursor.execute("UPDATE tasks SET status = 'in_progress' WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        return task_id
        
    conn.close()
    return None

def mark_task_as_done(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'done' WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Uruchamianie konsumenta (SQLite)...")
    while True:
        task = get_pending_task_and_update()
        
        if task:
            print(f"Konsumuje zadanie: {task}. Zmieniono status na 'in_progress'.")
            time.sleep(30)
            
            mark_task_as_done(task)
            print(f"Zakończono {task}. Zmieniono status na 'done'.")
        else:
            print("Brak pracy. Sprawdzam ponownie za 5s...")
            time.sleep(5)
