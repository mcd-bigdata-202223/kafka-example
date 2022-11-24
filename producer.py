from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

producer.send('my-topic', b'raw_bytes')

producer.flush()