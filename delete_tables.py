import json
from db_factory import get_db_adapter
from config_loader import load_env

def main():
    config = load_env()
    db = get_db_adapter(config)
    db.connect()

    # Specify the table(s) to drop
    tables_to_drop = ["certificates"]  # Add more table names as needed

    for table in tables_to_drop:
        try:
            db.execute(f"DROP TABLE IF EXISTS {table};")
            print(json.dumps({"status": f"{table} table dropped (if it existed)"}))
        except Exception as e:
            print(json.dumps({"error": f"Error dropping {table}: {e}"}))

    db.close()

if __name__ == "__main__":
    main()
