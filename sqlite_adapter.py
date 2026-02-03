import sqlite3
from typing import Any, Dict, List, Optional
from db_interface import DatabaseInterface

class SQLiteAdapter(DatabaseInterface):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def create(self, table: str, data: Dict[str, Any]) -> Any:
        keys = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        sql = f"INSERT INTO {table} ({keys}) VALUES ({placeholders})"
        self.cursor.execute(sql, tuple(data.values()))
        self.conn.commit()
        return self.cursor.lastrowid

    def read(self, table: str, criteria: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        sql = f"SELECT * FROM {table}"
        params = []
        if criteria:
            where = ' AND '.join([f"{k}=?" for k in criteria])
            sql += f" WHERE {where}"
            params = list(criteria.values())
        self.cursor.execute(sql, params)
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def update(self, table: str, criteria: Dict[str, Any], data: Dict[str, Any]) -> int:
        set_clause = ', '.join([f"{k}=?" for k in data])
        where_clause = ' AND '.join([f"{k}=?" for k in criteria])
        sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        params = list(data.values()) + list(criteria.values())
        self.cursor.execute(sql, params)
        self.conn.commit()
        return self.cursor.rowcount

    def delete(self, table: str, criteria: Dict[str, Any]) -> int:
        where_clause = ' AND '.join([f"{k}=?" for k in criteria])
        sql = f"DELETE FROM {table} WHERE {where_clause}"
        params = list(criteria.values())
        self.cursor.execute(sql, params)
        self.conn.commit()
        return self.cursor.rowcount

    def close(self):
        self.conn.close()
