import psycopg2

# Define the connection parameters
dbname = "postgres"
user = "postgres"
password = "test"
host = "postgresql"  # Replace with your service name and namespace
port = "5432"

# Establish the connection
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

# Create a cursor object using the connection
cursor = conn.cursor()

# Execute SQL queries using the cursor
cursor.execute("""CREATE TABLE IF NOT EXISTS historiske_personer (
               id SERIAL PRIMARY KEY,
               navn VARCHAR(100),
               nationalitet VARCHAR(20)
                );""")

conn.commit()

#Add some persons
# cursor.execute("""INSERT INTO historiske_personer (navn, nationalitet) VALUES
#                ('Dagmar Overby', 'Danmark'),
#                ('Alfred Nobel', 'Sverige'),
#                ('Edvard Munch', 'Norge'),
#                ('Carl Gustaf Mannerheim', 'Finland'),
#                ('Otto Von Bismarck', 'Det Tyske Kejserrige'),
#                ('Kemal Atatürk', 'Tyrkiet'),
#                ('Mary Shelly', 'England'),
#                ('Kong Leopold II', 'Belgien'),
#                ('Vjatjeslav Molotov', 'Sovjetunionen'),
#                ('Ed Gein', 'USA'),
#                ('Benito Mussolini', 'Italien'),
#                ('Kleopatra VII', 'Ægypten'),
#                ('Pedro López', 'Colombia'),
#                ('Josef Stalin', 'Georgien'),
#                ('Ikke nogen', 'Island')
#                """)

# conn.commit()



#hent data

cursor.execute("""SELECT * FROM historiske_personer""")
personer = cursor.fetchall()

print(personer)

# Close communication with the database
cursor.close()
conn.close()