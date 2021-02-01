import json
import pika
import pymongo


def receiver(collection: pymongo.collection.Collection, queue='hello'):
    """

    :type collection: pymongo.collection.Collection
    :param collection: db collection
    :param queue: Name of Message queue
    """

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue)

    def callback(ch, method, properties, body):

        try:
            print(f"[x] Converted to JSON {json.loads(body.decode())}")
            json_data = json.loads(body.decode('utf-8'))
            print(json_data)

            # Insert Data Into Collection
            collection.insert_one(json_data)

        except ValueError as e:
            # Ignore error
            print(" [x] Received %r" % body.decode())
            pass

        connection.close()

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
