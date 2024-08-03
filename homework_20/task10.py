def make_config(key, value):
    def config():
        return {key: value}

    return config

db_config = make_config("database", "mongodb")
api_config = make_config("56394", "api_key")

print(db_config())
print(api_config())
