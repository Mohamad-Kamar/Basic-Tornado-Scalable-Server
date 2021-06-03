#!/usr/bin/env python
import pika


def execute(msg):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body=msg)
    print(f" [x] Sent {msg}")
    connection.close()