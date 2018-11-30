import sqlite3

conn = sqlite3.connect('us.py')

c = conn.cursor()
c.execute("drop table users")

#USERS TABLE
c.execute('''
          CREATE TABLE users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          user_id INTEGER,
          login TEXT,
          user_name TEXT,
          gender TEXT,
          preferences TEXT
          FOREIGN KEY(city_id) REFERENCES cities(id)
          FOREIGN KEY(group_id) REFERENCES groups(id)
)
''')


#QUEST TABLE
c.execute('''
          CREATE TABLE quests (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          quest_id INTEGER,
          city TEXT,
          subway TEXT,
          features TEXT,
)
''')

#GROUPS TABLE
c.execute('''
          CREATE TABLE groups (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          group_id INTEGER,
          group_name TEXT,
          group_members TEXT,
          FOREIGN KEY(group_id) REFERENCES groups(id),
          FOREIGN KEY(quest_id) REFERENCES quest(id),
          FOREIGN KEY(user_id) REFERENCES user(id)
)
''')

c.execute('''
          CREATE TABLE cities (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          cities_id INTEGER,
          city_name TEXT
)
''')

conn.commit()

c.execute('''
          INSERT INTO users (name, gender, city, preferences
          VALUES
          ("Owl", "Postman", "Hogwards", "Wine")
''')

c.execute("INSERT INTO users VALUES (1, 1)")
conn.commit()
c.execute("INSERT INTO users VALUES (3, 1)")
conn.commit()

for user in _users:
    c.execute("INSERT INTO users"
              "(name, gender, city, preferences)"
              "VALUES"
              "('{name}','{gender},'{city}','[preferences]')".format(**user))

    conn.commit()


