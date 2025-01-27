from functools import lru_cache
import json
import os


config_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    "config.json"
)

@lru_cache(maxsize=1)
def get_config():
    with open(config_path, "r", encoding="utf8") as config:
        data = json.load(config)
    return data
