import sqlite3 as sql


def createDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()


def createTable():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS streamers
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name text,
                  followers integer,
                  subs integer
                  )"""
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # createDB()
    createTable()
