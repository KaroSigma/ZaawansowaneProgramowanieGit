import csv

QUEUE_FILE = 'queue.csv'

def add_task(task_id):
    with open(QUEUE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task_id, 'pending'])
    print(f"Dodano zadanie {task_id} do kolejki.")

if __name__ == "__main__":
    with open(QUEUE_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        
    for i in range(1, 101):
        add_task(f"Zadanie_{i}")
