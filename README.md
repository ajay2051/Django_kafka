# Download Kafka:
https://kafka.apache.org/downloads

# Extract the downloaded file
tar -xzf kafka_2.13-3.5.0.tgz
cd kafka_2.13-3.5.0

# To Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

# Go To
nano config/server.properties

# Ensure these
listeners=PLAINTEXT://localhost:9092
advertised.listeners=PLAINTEXT://localhost:9092

# Open a new terminal window and run
bin/kafka-server-start.sh config/server.properties

# Open another terminal window and create the topic you'll be using
bin/kafka-topics.sh --create --topic face.embed.data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# Verify the topic was created
bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# Then Run this command in different terminal
python manage.py runserver
python dj_kafka/kafka_producer.py
python manage.py consume_kafka
