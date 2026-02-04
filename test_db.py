import json
from db_factory import get_db_adapter
from config_loader import load_env

def main():
    # Load DB config from environment variables
    config = load_env()
    db = get_db_adapter(config)
    db.connect()

    # Read certificate data from a JSON file (input.json) if it exists
    try:
        with open('input.json', 'r') as f:
            certificate_data = json.load(f)
        cert_id = db.create('certificates', certificate_data)
        print(json.dumps({"inserted": certificate_data}))
    except FileNotFoundError:
        print(json.dumps({"info": "No input.json file found. Skipping insert."}))
    except Exception as e:
        print(json.dumps({"error": f"Insert error: {e}"}))

    # Read all certificate records and output as JSON
    try:
        certs = db.read('certificates')
        print(json.dumps({"certificates": certs}, default=str))
    except Exception as e:
        print(json.dumps({"error": f"Read error: {e}"}))

    # Example: Update a certificate record from update.json if it exists
    try:
        with open('update.json', 'r') as f:
            update_info = json.load(f)
        db.update('certificates', update_info['criteria'], update_info['data'])
        print(json.dumps({"updated": update_info}))
    except FileNotFoundError:
        print(json.dumps({"info": "No update.json file found. Skipping update."}))
    except Exception as e:
        print(json.dumps({"error": f"Update error: {e}"}))

    # Example: Delete a certificate record from delete.json if it exists
    try:
        with open('delete.json', 'r') as f:
            delete_criteria = json.load(f)
        db.delete('certificates', delete_criteria)
        print(json.dumps({"deleted": delete_criteria}))
    except FileNotFoundError:
        print(json.dumps({"info": "No delete.json file found. Skipping delete."}))
    except Exception as e:
        print(json.dumps({"error": f"Delete error: {e}"}))

    db.close()

if __name__ == "__main__":
    main()