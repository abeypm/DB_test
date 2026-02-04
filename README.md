# Generic Database Interface in Python

This project provides a generic, extensible database interface in Python, supporting multiple backends such as SQLite and PostgreSQL. It uses abstraction layers and adapters to enable seamless switching between databases, and implements standard CRUD operations for easy data management.

## Features
- Abstract base class for database operations
- Adapters for SQLite and PostgreSQL
- Factory for dynamic adapter selection
- Example test script for CRUD operations
- Easily extendable to other databases

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <your-repo-url>
   cd DB_test
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   - Copy `.env.example` to `.env` and edit as needed for your environment:
     ```
     cp .env.example .env
     # Edit .env to set DB_TYPE and DB_DSN
     ```

4. **(Optional) Start a local PostgreSQL instance with Docker:**
   ```
   docker run --name local-postgres -e POSTGRES_PASSWORD=yourpassword -p 5432:5432 -d postgres
   ```

5. **Prepare test JSON files:**
   - Edit `input.json`, `update.json`, and `delete.json` to test insert, update, and delete operations.

6. **Run the test script:**
   ```
   python test_db.py
   ```
   - The script will perform CRUD operations using the JSON files and print results as JSON.

## Integration in Another Application

1. **Import the DB interface and factory:**
   ```python
   from db_factory import get_db_adapter
   from config_loader import load_env
   config = load_env()
   db = get_db_adapter(config)
   db.connect()
   # Use db.create, db.read, db.update, db.delete as needed
   db.close()
   ```

2. **Use Python dictionaries for data:**
   - Pass dictionaries for insert/update data and criteria.
   - Example:
     ```python
     db.create('certificates', {
         'name': 'PE003-SW',
         'department': 'Software',
         # ... other fields ...
     })
     db.read('certificates', {'user_id': 'joe123'})
     ```

3. **(Optional) Build a Web API:**
   - You can wrap the DB interface in a Flask or FastAPI app to provide HTTP/JSON endpoints for integration with a WebUI or other services.

## Notes
- Do not commit your `.env` file or any sensitive credentials to version control.
- The adapters and interface are designed to be easily extended for other databases.
- For production, use a migration tool for schema changes.

## Example JSON Files

- `input.json` (for insert):
  ```json
  {
    "name": "PE003-SW",
    "department": "Software",
    "certification_date": "2026-02-04",
    "trainer": "Jane Smith",
    "section": "A",
    "bu": "R&D",
    "email_id": "joe@example.com",
    "user_id": "joe123"
  }
  ```
- `update.json` (for update):
  ```json
  {
    "criteria": {"name": "PE003-SW", "user_id": "joe123"},
    "data": {"trainer": "John Doe"}
  }
  ```
- `delete.json` (for delete):
  ```json
  {
    "name": "PE003-SW",
    "user_id": "joe123"
  }
  ```
