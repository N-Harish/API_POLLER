import pika


def send(body, queue='hello'):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=queue)

    channel.basic_publish(exchange='', routing_key='hello', body=body)
    print(" [x] Message Sent ")
    connection.close()

# sender(body="{'key':'val'}", queue='hello')
