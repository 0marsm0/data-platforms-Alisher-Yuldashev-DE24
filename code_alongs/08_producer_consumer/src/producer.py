from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

data_path = Path(__file__).parents[1] / "data"  # path to json file

with open(data_path / "jokes.json", "r") as file:  # read json file
    jokes = json.load(file)  # save data from json in jokes

# pprint(jokes)

# form of entry point for interacting with Kafka, localhost:9092 is a poet mapped to broker container
app = Application(broker_address="localhost:9092", consumer_group="text-splitter")

jokes_topic = app.topic(name="jokes", value_serializer="json")

# print(jokes_topic)


def main():
    with app.get_producer() as producer:
        # print(producer)

        for joke in jokes:
            kafka_msg = jokes_topic.serialize(key=joke["joke_id"], value=joke)
            print(f"Produced message: key = {kafka_msg.key} value = {kafka_msg.value}")

            producer.produce(
                topic="jokes", key=str(kafka_msg.key), value=kafka_msg.value
            )


if __name__ == "__main__":
    main()
