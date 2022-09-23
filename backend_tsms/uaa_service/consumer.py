import pika

params = pika.URLParameters('amqps://joqrdpub:oL0eQS_SteqMZCb6PWcEPxn7fuwqffb8@stingray.rmq.cloudamqp.com/joqrdpub')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch,method,properties,body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin',on_message_callback=callback,auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()