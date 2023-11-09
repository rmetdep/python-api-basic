import sqlite3

# db initializer
conn = sqlite3.connect('data.db')
print("Opened database successfully")

# raw data
driver = ['Valtteri Bottas', 'Guanyu Zhou', 'Pierre Gasly', 'Yuki Tsunoda', 'Fernando Alonso', 'Esteban Ocon', 'Sebastian Vettel', 'Lance Stroll', 'Charles Leclerc', 'Carlos Sainz Jr.', 'Mick Schumacher', 'Kevin Magnussen', 'Daniel Ricciardo', 'Lando Norris', 'Lewis Hamilton', 'George Russell', 'Max Verstappen', 'Sergio Pérez', 'Alex Albon', 'Nicholas Latifi']
team = ['Alfa Romeo Racing', 'AlphaTauri', 'Alpine', 'Aston Martin', 'Ferrari', 'Haas', 'McLaren', 'Mercedes', 'Red Bull Racing', 'Williams']
circuits = ['Abu Dhabi', 'Azerbaijan', 'Bahrain', 'Barcelona', 'Budapest', 'Imola', 'Istanbul', 'Jeddah', 'Monaco', 'Montreal', 'Portimao', 'Silverstone', 'Sochi', 'Suzuka']

# create tables
conn.execute("CREATE TABLE driver (driverId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, driverName TEXT);")
conn.execute("CREATE TABLE team (teamId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, teamName TEXT);")
conn.execute("CREATE TABLE circuits (circuitId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, circuitName TEXT);")
print("Created tables successfully")

# insert data
for x in driver:
    conn.execute("INSERT INTO driver (driverName) VALUES ('" + x + "');")

for x in team:
    conn.execute("INSERT INTO team (teamName) VALUES ('" + x + "');")

for x in circuits:
    conn.execute("INSERT INTO circuits (circuitName) VALUES ('" + x + "');")

print("Inserted data successfully")

# commit all changes to the database, otherwise they will be lost
conn.commit()

# close the connection
conn.close()
print("Database created successfully")