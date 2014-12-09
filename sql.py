import sqlite3

with sqlite3.connect("sample.db") as connnection:
    c = connnection.cursor()
    c.execute("DROP TABLE posts")
    c.execute("CREATE TABLE posts(title TEXT, description TEXT)")
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Bad", "I\'m unwell.")')
