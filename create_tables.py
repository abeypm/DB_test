import json
from db_factory import get_db_adapter
from config_loader import load_env

def json_schema_to_sql(schema_json):
    table = schema_json["table"]
    columns = schema_json["columns"]
    columns_sql = ",\n    ".join([f"{col['name']} {col['type']}" for col in columns])
    return f"CREATE TABLE IF NOT EXISTS {table} (\n    {columns_sql}\n);"

def main():
    config = load_env()
    db = get_db_adapter(config)
    db.connect()

    # Load all table schemas from schema.json and create tables
    try:
        with open('schema.json') as f:
            schemas = json.load(f)
        for schema in schemas:
            sql = json_schema_to_sql(schema)
            db.execute(sql)
            print(json.dumps({"status": f"{schema['table']} table created or already exists"}))
    except Exception as e:
        print(json.dumps({"error": f"Table creation error: {e}"}))
    finally:
        db.close()

if __name__ == "__main__":
    main()