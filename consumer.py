import csv
import time
import os

QUEUE_FILE = 'queue.csv'

def get_pending_task_and_update():
    if not os.path.exists(QUEUE_FILE):
        return None

    tasks = []
    with open(QUEUE_FILE, mode='r') as file:
        reader = csv.reader(file)
        tasks = list(reader)

    task_to_do = None
    for row in tasks:
        if len(row) == 2 and row[1] == 'pending':
            task_to_do = row[0]
            row[1] = 'in_progress'
            break

    if task_to_do:
        with open(QUEUE_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(tasks)
            
    return task_to_do

def mark_task_as_done(task_id):
    tasks = []
    with open(QUEUE_FILE, mode='r') as file:
        reader = csv.reader(file)
        tasks = list(reader)

    for row in tasks:
        if row[0] == task_id:
            row[1] = 'done'
            break

    with open(QUEUE_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

if __name__ == "__main__":
    print("Uruchamianie konsumenta...")
    while True:
        task = get_pending_task_and_update()
        
        if task:
            print(f"Konsumuje zadanie: {task}. Zmieniono status na 'in_progress'.")
            time.sleep(30) # Symulacja wykonania pracy trwającej 30s[cite: 6]
            
            mark_task_as_done(task)
            print(f"Zakończono {task}. Zmieniono status na 'done'.")
        else:
            print("Brak pracy. Sprawdzam ponownie za 5s...")
            time.sleep(5)
