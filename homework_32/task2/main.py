import yaml
import json


with open("data.yaml", "r") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

with open("data.json", "w") as json_file:
    json.dump(yaml_data, json_file, indent=4)
