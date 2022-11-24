
# Apache Kafka

  

This tutorial pretends to give an example of how to create an Apache Kafka cluster and run a producer and a consumer tasks.

  

# Create an Apache Kafka cluster

  

## Option #1: With Docker

The first option to install Apache Kafka on your computer is to download Docker and create a container based on the [bitnami/kafka image](https://hub.docker.com/r/bitnami/kafka).

  

1. First, install and run **[Docker](https://www.docker.com)**

  

2. Then, create a file named **docker-compose.yml** with the following content

```

version: "3"

services:

zookeeper:

image: 'bitnami/zookeeper:latest'

ports:

- '2181:2181'

environment:

- ALLOW_ANONYMOUS_LOGIN=yes

kafka:

image: 'bitnami/kafka:latest'

ports:

- '9092:9092'

environment:

- KAFKA_BROKER_ID=1

- KAFKA_CFG_LISTENERS=PLAINTEXT://:9092

- KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://127.0.0.1:9092

- KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181

- ALLOW_PLAINTEXT_LISTENER=yes

depends_on:

- zookeeper

```

3. Finally, run the command:

```

$ docker-compose up -d

```

*Apache Kafka* server is now accessible on **localhost:9092**

  

4. To stop the server, run the command:

```

$ docker-compose down

```

  

## Option #2: With CloudKarafka

  

[CloudKarafka](https://www.cloudkarafka.com) offers a free plan (**Developer Duck**), that allows to create an Apache Kafka instance on the cloud.

  

1. Create an account on [CloudKarafka](https://www.cloudkarafka.com/) with the **Developer Duck** plan

2. You can register an account or sign in with Google e-mail

3. Input a **Team Name** (it can be your name/student number)

4. Create a new instance with the button **+ Create New Instance**

5. Give a name for the instance, select the Developer Duck (Free) plan

6. Select the data center (EU-West-1 Ireland)

7.  **Confirm**

8. Click on the instance name

  

On **Details** pane, the website presents your instance configuration parameters.

  

Save the connection details with the **following template** on a **text document** (the repository includes this template in the file *.env.example*; you are free to edit it and save it as *.env*):
```

export CLOUDKARAFKA_BROKERS="server1:9094,server2:9094,server3:9094"

export CLOUDKARAFKA_USERNAME="username"

export CLOUDKARAFKA_PASSWORD="password"

export CLOUDKARAFKA_TOPIC="username-default"

```

  

Now we can follow the official **Python** example from **CloudKarafka**: [https://github.com/CloudKarafka/python-kafka-example](https://github.com/CloudKarafka/python-kafka-example)

  

### Running the consumer

1. Open a new terminal

2. Run the configuration commands, previously saved on the text document

3. Run the following commands

```

git clone https://github.com/CloudKarafka/python-kafka-example.git

cd python-kafka-example

pip3 install confluent_kafka

python3 consumer.py

```

  

### Running the producer

1. Open a new terminal

2. Run the configuration commands, previously saved on the text document

3. Run the following commands

```

cd python-kafka-example

python3 producer.py

```

### Send events

Now you can **type** on the **producer terminal**, press Enter, and you will see the events on the consumer terminal. Besides, you can also monitor the topic on the **Browser** pane (select it on CloudKarafka left menu).
