from lib.db.connection import CONN, CURSOR

with open("lib/db/schema.sql") as f:
    CURSOR.executescript(f.read())
    CONN.commit()
    print("Database schema created.")