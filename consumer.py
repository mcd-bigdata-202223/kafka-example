from kafka import KafkaConsumer

consumer = KafkaConsumer('my-topic', bootstrap_servers=['localhost:9092'])

for message in consumer:
    print(message.key)
    print(message.value)
    print(message.timestamp)
