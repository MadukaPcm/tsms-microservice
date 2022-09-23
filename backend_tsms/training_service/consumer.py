import pika,json

params = pika.URLParameters('amqps://joqrdpub:oL0eQS_SteqMZCb6PWcEPxn7fuwqffb8@stingray.rmq.cloudamqp.com/joqrdpub')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='training')

def callback(ch,method,properties,body):
    print('Received in training')
    print(body)
    # data = json.loads(body)
    # print(data)

channel.basic_consume(queue='training',on_message_callback=callback,auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()