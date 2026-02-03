from db_factory import get_db_adapter

# Uncomment and configure for SQLite
# config = {
#     'type': 'sqlite',
#     'db_path': 'test.db'
# }

# Uncomment and configure for PostgreSQL
# Example DSN: "dbname=test user=postgres password=secret host=localhost port=5432"
config = {
    'type': 'postgres',
    'dsn': 'your_postgres_dsn_here'
}

db = get_db_adapter(config)
db.connect()

# Create a test table
try:
    db.execute('''CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT,
        age INTEGER
    )''')
except Exception as e:
    print(f"Table creation error: {e}")

# Test CREATE
user_id = db.create('users', {'name': 'Alice', 'age': 30})
print(f"Inserted user with id: {user_id}")

# Test READ
users = db.read('users')
print("Users:", users)

# Test UPDATE
updated = db.update('users', {'id': user_id}, {'age': 31})
print(f"Rows updated: {updated}")

# Test DELETE
deleted = db.delete('users', {'id': user_id})
print(f"Rows deleted: {deleted}")

db.close()