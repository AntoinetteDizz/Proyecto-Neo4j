from flask import Flask, render_template
from neo4j import GraphDatabase

app = Flask(__name__)

# Conexión a la base de datos Neo4j
user = "neo4j"
password = "Z9YriNGt_vOu9m3_Awg-Om4PWOtOXWEAv_yzfgOx7Rk"
uri = "neo4j+s://e117892e.databases.neo4j.io"

driver = GraphDatabase.driver(uri=uri, auth=(user, password))

@app.route('/')
def index():
    with driver.session() as session:
        # Consulta 1: Obtener todas las personas con sus relaciones
        personas_relaciones = list(session.run("""
        MATCH (p:Persona)-[r]->(c)
        RETURN p, type(r), c
        """))

        # Consulta 2: Encontrar todas las personas casadas
        personas_casadas = list(session.run("""
        MATCH (p:Persona)-[:Casado_con]->()
        RETURN p
        """))

        # Consulta 3: Encontrar todas las personas que son padres
        personas_padres = list(session.run("""
        MATCH (p:Persona)-[:Padre_de]->()
        RETURN p
        """))

        # Consulta 4: Encontrar las personas que tienen una edad mayor a 50 años
        personas_mayores = list(session.run("""
        MATCH (p:Persona)
        WHERE p.edad > 50
        RETURN p
        """))

        # Consulta 5: Encontrar las personas que les gusta la música
        personas_musica = list(session.run("""
        MATCH (p:Persona)
        WHERE 'Musica' IN p.gustos
        RETURN p
        """))

    return render_template('index.html', personas_relaciones=personas_relaciones, personas_casadas=personas_casadas, personas_padres=personas_padres, personas_mayores=personas_mayores, personas_musica=personas_musica)

if __name__ == '__main__':
    app.run(port=3000, debug=True)