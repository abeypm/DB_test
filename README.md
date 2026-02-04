# Project Status: Generic Database Interface in Python

## Overview
This project implements a generic, extensible database interface in Python, supporting both SQLite and PostgreSQL. It uses abstraction layers and adapters for seamless backend switching, and supports standard CRUD operations. The project is now structured for easy integration, testing, and future extension (including WebUI/API compatibility).

## Current Features
- Abstract base class for database operations
- Adapters for SQLite and PostgreSQL
- Factory for dynamic adapter selection
- JSON-based test script for CRUD operations
- Environment-based configuration (.env, config.yaml)
- Schema definition in JSON (schema.json)
- Table creation and deletion scripts (create_tables.py, delete_table.py)
- Example JSON files for insert, update, and delete
- Comprehensive setup and usage documentation

## Setup & Usage
- Clone the repository and install dependencies from requirements.txt
- Configure your environment using .env (see .env.example)
- Define your database schema in schema.json (supports multiple tables)
- Run create_tables.py to create all tables
- Use test_db.py with input.json, update.json, and delete.json for CRUD testing
- Use delete_table.py to drop tables as needed

## Integration Guidance
- Import the DB interface and factory in your application:
  ```python
  from db_factory import get_db_adapter
  from config_loader import load_env
  config = load_env()
  db = get_db_adapter(config)
  db.connect()
  # Use db.create, db.read, db.update, db.delete
  db.close()