from kafka import KafkaProducer, KafkaConsumer
import json
import time

def produce_messages(kafka_config, topic, messages):
    """
    Produce messages to the specified Kafka topic.
    """
    producer = KafkaProducer(bootstrap_servers=kafka_config["bootstrap.servers"],
                             value_serializer=lambda v: v.encode('utf-8'))
    for msg in messages:
        producer.send(topic, value=msg)
    producer.flush()
    producer.close()
    return True

def consume_messages(kafka_config, topic, num_messages):
    """
    Consume a specified number of messages from the given Kafka topic.
    Returns a list of consumed messages.
    """
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=kafka_config["bootstrap.servers"],
        auto_offset_reset='earliest',
        group_id='test-group',
        value_deserializer=lambda v: v.decode('utf-8'),
        consumer_timeout_ms=10000  # stops if no messages in 10s
    )
    messages = []
    for msg in consumer:
        messages.append(msg.value)
        if len(messages) >= num_messages:
            break
    consumer.close()
    return messages

if __name__ == "__main__":
    # Example usage
    config = {"bootstrap.servers": "localhost:9092"}
    topic = "my-test-topic"
    msgs = ["Hello", "Kafka", "World"]
    produce_messages(config, topic, msgs)
    # Sleep a few seconds to let messages propagate (in a real scenario)
    time.sleep(5)
    received = consume_messages(config, topic, len(msgs))
    print("Received messages:", received)
