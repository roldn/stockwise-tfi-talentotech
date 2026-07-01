import sqlite3
from contextlib import contextmanager
from ..config import DB_PATH

@contextmanager
def conexion():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()