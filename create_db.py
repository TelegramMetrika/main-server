import sqlite3

db = sqlite3.connect('database.db')
sql = db.cursor()

logs = """
CREATE TABLE "bots" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"token" TEXT,
	"users" TEXT,
	PRIMARY KEY("id")
);
"""

sql.execute(logs)

db.commit()