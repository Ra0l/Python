import sqlite3

with sqlite3.connect("Python-Course/sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
    CREATE TABLE if not exists usuarios 
    (id INTEGER primary key, nombre VARCHAR(50));
    """
    )
