# Generic Database Interface in Python

This project provides a generic, extensible database interface in Python, supporting multiple backends such as SQLite and PostgreSQL. It uses abstraction layers and adapters to enable seamless switching between databases, and implements standard CRUD operations for easy data management.

## Features
- Abstract base class for database operations
- Adapters for SQLite and PostgreSQL
- Factory for dynamic adapter selection
- Example test script for CRUD operations
- Easily extendable to other databases

## Usage
Configure your database in the test script and run it to perform create, read, update, and delete operations using a unified interface.