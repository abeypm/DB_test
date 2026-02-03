from sqlite_adapter import SQLiteAdapter
from postgres_adapter import PostgresAdapter

def get_db_adapter(config):
    db_type = config.get('type')
    if db_type == 'sqlite':
        return SQLiteAdapter(config['db_path'])
    elif db_type == 'postgres':
        return PostgresAdapter(config['dsn'])
    raise ValueError(f"Unsupported DB type: {db_type}")