from flask import Flask, render_template
from neo4j import GraphDatabase

app = Flask(__name__)

# Conexión a la base de datos Neo4j
user = "neo4j"
password = "Z9YriNGt_vOu9m3_Awg-Om4PWOtOXWEAv_yzfgOx7Rk"
uri = "neo4j+s://e117892e.databases.neo4j.io"

driver = GraphDatabase.driver(uri=uri, auth=(user, password))
session = driver.session()

app = Flask(__name__)
#############################################

# Conexión a la base de datos Neo4j
driver = GraphDatabase.driver(uri, auth=(user, password))

# Consulta 1: Obtener todas las personas con sus relaciones
with driver.session() as session:
    result = session.run("""
    MATCH (p:Persona)-[r]->(c)
    RETURN p, type(r), c
    """)
    for record in result:
        print(record)

# Consulta 2: Encontrar todas las personas casadas
with driver.session() as session:
    result = session.run("""
    MATCH (p:Persona)-[:Casado_con]->()
    RETURN p
    """)
    for record in result:
        print(record)

# Consulta 3: Encontrar todas las personas que son padres
with driver.session() as session:
    result = session.run("""
    MATCH (p:Persona)-[:Padre_de]->()
    RETURN p
    """)
    for record in result:
        print(record)

# Consulta 4: Encontrar las personas que tienen una edad mayor a 50 años
with driver.session() as session:
    result = session.run("""
    MATCH (p:Persona)
    WHERE p.edad > 50
    RETURN p
    """)
    for record in result:
        print(record)

# Consulta 5: Encontrar las personas que les gusta la música
with driver.session() as session:
    result = session.run("""
    MATCH (p:Persona)
    WHERE 'Musica' IN p.gustos
    RETURN p
    """)
    for record in result:
        print(record)


@app.route('/')
def index():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(port=3000, debug=True)
