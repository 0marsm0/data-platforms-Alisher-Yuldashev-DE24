from pathlib import Path
import json
from pprint import pprint

data_path = Path(__file__).parents[1] / "data"  # path to json file

with open(data_path / "jokes.json", "r") as file:  # read json file
    jokes = json.load(file)  # save data from json in jokes

pprint(jokes)
