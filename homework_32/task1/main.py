import yaml


with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

config["server"]["port"] = 9090

with open("config.yaml", "w") as file:
    yaml.safe_dump(config, file)
