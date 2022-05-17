import sqlite3

connection = sqlite3.connect('cinema.db')
cursor = connection.cursor()

rows = cursor.execute("SELECT id, ticket_code, ticket_type, ticket_used, buyer, showing FROM tickets").fetchall()
print(rows)

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

for record in rows:
    print(record)
    cursor.execute("INSERT INTO movie_ticketing_ticket VALUES (?, ?, ?, ?, ?, ?)", record)

connection.commit()

