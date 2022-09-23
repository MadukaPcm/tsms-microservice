import pika,json

params = pika.URLParameters('amqps://joqrdpub:oL0eQS_SteqMZCb6PWcEPxn7fuwqffb8@stingray.rmq.cloudamqp.com/joqrdpub')

connection = pika.BlockingConnection(params)

channel = connection.channel()

# def publish(method,body):
#     properties = pika.BasicProperties(method)
#     channel.basic_publish(exchange='',routing_key='training',body=json.dumps(body),properties=properties)
def publish():
    channel.basic_publish(exchange='',routing_key='training',body='Hello Training')