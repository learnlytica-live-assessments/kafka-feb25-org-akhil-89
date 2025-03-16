# kafka-assignment
kafka assignment 

1. Student Assignment Overview
Assignment Description:
Students are asked to implement a simple Kafka application that includes two functions:

produce_messages(kafka_config, topic, messages)

Input: A dictionary with Kafka configuration (e.g. bootstrap servers), a topic name, and a list of messages (strings).
Action: Connect to Kafka and send the provided messages to the specified topic.
consume_messages(kafka_config, topic, num_messages)

Input: A dictionary with Kafka configuration, a topic name, and the expected number of messages to consume.
Output: A list of messages consumed from the topic.
They should also include a main block that optionally demonstrates these functions
