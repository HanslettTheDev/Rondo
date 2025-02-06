from functools import lru_cache
import json
import os


config_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    "config.json"
)

db_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    "rondo.db"
)

@lru_cache(maxsize=1)
def get_config() -> dict:
    with open(config_path, "r", encoding="utf8") as config:
        data = json.load(config)
    return data

def get_env(key: str) -> str:
    """ 
    Gets the environments variables for the configs
    It checks if the exists a config.json file locally or on the server
    And if all fails, it reverts to the OS environment variables
    """
    try:
        config = get_config().get("config")
    except FileNotFoundError:
        return os.environ.get(key)
    
    if key == "SQLALCHEMY_DATABASE_URI":
        return f"sqlite:///{db_path}"
    
    try:
        return config.get(key)
    except KeyError:
        return ""