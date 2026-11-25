import time
import pika

QUEUE_NAME = 'tasks_queue'


def callback(ch, method, properties, body):
    task_id = body.decode('utf-8')
    print(f"{task_id}. Zmieniono status na 'in_progress'.")
    time.sleep(30)

    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f"Zakończono {task_id}. Zmieniono status na 'done'.")


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
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    print("Oczekiwanie na zadania. Naciśnij CTRL+C, aby zakończyć.")
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Zatrzymano konsumenta.")
    finally:
        if connection.is_open:
            connection.close()