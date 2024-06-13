from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import psycopg2

app = FastAPI()

# Define the connection parameters
dbname = "postgres"
user = "postgres"
password = "test"
host = "postgresql"  # Replace with your service name and namespace
port = "5432"

# Establish the connection
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = conn.cursor()

def make_db():
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    # Execute SQL queries using the cursor
    cursor.execute("""CREATE TABLE IF NOT EXISTS historiske_personer (
                id SERIAL PRIMARY KEY,
                navn VARCHAR(100),
                nationalitet VARCHAR(20)
                    );""")

    conn.commit()
    cursor.close()
    conn.close()

def add_all_persons():
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    #Add some persons
    cursor.execute("""INSERT INTO historiske_personer (navn, nationalitet) VALUES
                   ('Dagmar Overby', 'Danmark'),
                   ('Alfred Nobel', 'Sverige'),
                   ('Edvard Munch', 'Norge'),
                   ('Carl Gustaf Mannerheim', 'Finland'),
                   ('Otto Von Bismarck', 'Det Tyske Kejserrige'),
                   ('Kemal Atatürk', 'Tyrkiet'),
                   ('Mary Shelly', 'England'),
                   ('Kong Leopold II', 'Belgien'),
                   ('Vjatjeslav Molotov', 'Sovjetunionen'),
                   ('Ed Gein', 'USA'),
                   ('Benito Mussolini', 'Italien'),
                   ('Kleopatra VII', 'Ægypten'),
                   ('Pedro López', 'Colombia'),
                   ('Josef Stalin', 'Georgien'),
                   ('Björk Guðmundsdóttir', 'Island'),
                   ('Ikke nogen', 'Moldova')
                   """)

    conn.commit()
    cursor.close()
    conn.close()



def hent_data():
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    #hent data

    cursor.execute("""SELECT * FROM historiske_personer""")
    personer = cursor.fetchall()

    # Close communication with the database
    cursor.close()
    conn.close()

    
    personer = [{"id": item[0], "navn": item[1], "nationalitet": item[2]} for item in personer]

    return personer

def add_person(navn, nationalitet):
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    #Add some persons
    cursor.execute(f"""INSERT INTO historiske_personer (navn, nationalitet) VALUES ('{navn}', '{nationalitet}')""")
    conn.commit()

    cursor.close()
    conn.close()


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url='/docs')

@app.get("/historiske-personer")
def root():
    return hent_data()

@app.post('/add-historisk-person')
def add_person_route(navn, nationalitet):
    add_person(navn, nationalitet)
    return hent_data()
