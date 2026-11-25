import pika

QUEUE_NAME = 'tasks_queue'


def add_task(channel, task_id):
    channel.basic_publish(
        exchange='',
        routing_key=QUEUE_NAME,
        body=task_id,
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        )
    )
    print(f"Dodano zadanie {task_id}")


if __name__ == "__main__":
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters(
        host='localhost',
        port=8081,
        credentials=credentials
    )

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    for i in range(1, 101):
        add_task(channel, f"Zadanie_{i}")

    connection.close()