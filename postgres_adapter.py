import psycopg2
from typing import Any, Dict, List, Optional
from db_interface import DatabaseInterface

class PostgresAdapter(DatabaseInterface):
    def __init__(self, dsn: str):
        self.dsn = dsn
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = psycopg2.connect(self.dsn)
        self.cursor = self.conn.cursor()

    def create(self, table: str, data: Dict[str, Any]) -> Any:
        keys = ', '.join(data.keys())
        placeholders = ', '.join(['%s' for _ in data])
        sql = f"INSERT INTO {table} ({keys}) VALUES ({placeholders}) RETURNING id"
        self.cursor.execute(sql, tuple(data.values()))
        self.conn.commit()
        return self.cursor.fetchone()[0]

    def read(self, table: str, criteria: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        sql = f"SELECT * FROM {table}"
        params = []
        if criteria:
            where = ' AND '.join([f"{k}=%s" for k in criteria])
            sql += f" WHERE {where}"
            params = list(criteria.values())
        self.cursor.execute(sql, params)
        columns = [desc[0] for desc in self.cursor.description]
        rows = self.cursor.fetchall()
        return [dict(zip(columns, row)) for row in rows]

    def update(self, table: str, criteria: Dict[str, Any], data: Dict[str, Any]) -> int:
        set_clause = ', '.join([f"{k}=%s" for k in data])
        where_clause = ' AND '.join([f"{k}=%s" for k in criteria])
        sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        params = list(data.values()) + list(criteria.values())
        self.cursor.execute(sql, params)
        self.conn.commit()
        return self.cursor.rowcount

    def delete(self, table: str, criteria: Dict[str, Any]) -> int:
        where_clause = ' AND '.join([f"{k}=%s" for k in criteria])
        sql = f"DELETE FROM {table} WHERE {where_clause}"
        params = list(criteria.values())
        self.cursor.execute(sql, params)
        self.conn.commit()
        return self.cursor.rowcount

    def close(self):
        self.conn.close()
