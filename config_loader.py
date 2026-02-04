import os
from dotenv import load_dotenv
import yaml

# Load environment variables from .env file
def load_env():
    load_dotenv()
    return {
        'type': os.getenv('DB_TYPE'),
        'dsn': os.getenv('DB_DSN')
    }

# Load general config from config.yaml
def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)
