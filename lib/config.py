import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()
# Assuming you've already connected to the database and created a cursor
CURSOR.execute("PRAGMA table_info(songs)")
table_info = CURSOR.fetchall()
print(table_info)

songs = CURSOR.execute('SELECT * FROM songs')
[row for row in songs]