import sqlite3


def task_5():
    with sqlite3.connect('task22_5.db') as conn:
        conn: sqlite3.Connection
        cur = conn.cursor()
        cur: sqlite3.Cursor
        cur.execute("""
        CREATE TABLE IF NOT EXISTS table_1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        col2 TEXT,
        col3 TEXT
        )
        """)
        cur.execute(
            """
            INSERT INTO table_1 (col2,col3)
            VALUES(?,?)
            """
            , ['hello1', 'world1'])
        cur.execute(
            """
            INSERT INTO table_1 (col2,col3)
            VALUES(?,?)
            """
            , ['hello2', 'world2'])
        cur.execute(
            """
            INSERT INTO table_1 (col2,col3)
            VALUES(?,?)
            """
            , ['hello3', 'world3'])
        cur.execute("""
        DELETE FROM table_1 WHERE id=2
        """)
        cur.execute("""
        UPDATE table_1 SET col2='hello',col3='world' WHERE id=3
        """)
        with open('task5.txt', 'w') as f:
            for d in cur.fetchall():
                f.write(f'{d[0]}{d[0]}')


def hw():
    random_data = [
        1, 642, 94269426, -426, 6429, 462, '462', 'asomdoamds', 'ofmmwefomfwomfwomfwm'
    ]
    with sqlite3.connect('hw22.db') as conn:
        conn: sqlite3.Connection
        cur = conn.cursor()
        cur: sqlite3.Cursor
        cur.execute("""
        CREATE TABLE IF NOT EXISTS numbers
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        i INTEGER
        )
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS words(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        w TEXT
        )
        """)
        for i in random_data:
            if type(i) == int:
                cur.execute('INSERT INTO numbers(i) VALUES(?)', [i])
                if i % 2:
                    cur.execute('INSERT INTO words(w) VALUES(?)', ['Odd'])
            elif type(i) == str:
                word_len = len(i)
                cur.execute('INSERT INTO numbers(i) VALUES(?)', [i])
                cur.execute('INSERT INTO words(w) VALUES(?)', [word_len])
        cur.execute('SELECT COUNT(*) FROM numbers')
        items_count = cur.fetchone()[0]
        if items_count > 5:
            cur.execute("""
            DELETE FROM words WHERE id=1
            """)
        else:
            cur.execute("""
            UPDATE words SET w='hello' WHERE id=1
            """)


if __name__ == "__main__":
    task_5()
    hw()
