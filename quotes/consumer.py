from os import environ
from sys import path
import json
import pika
import django

# Your path to settings.py file
path.append('/home/anusikh/Documents/rabbit-mq-django/quotes/quotes/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')
django.setup()

from quote.models import QuoteTable

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='quote')


def callback(ch, method, properties, body):
    print("Received in quotes...")
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'add_like':
        quote = QuoteTable.objects.get(id=data)
        quote.likes += 1
        quote.save()
        print("liked!!!!")


channel.basic_consume(
    queue='quote', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()
