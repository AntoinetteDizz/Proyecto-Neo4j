# Proyecto de Gestión de Red Social

## Descripción del Proyecto

Este proyecto consiste en una aplicación web que gestiona una red social, utilizando Python con el framework Flask y una base de datos Neo4j. Permite realizar diversas consultas sobre las relaciones entre personas, como encontrar personas casadas, padres, mayores de 50 años, y a quienes les gusta la música.

## Funcionalidades de la Aplicación

1. **Consulta de Personas y Relaciones:**
   - La aplicación permite visualizar todas las personas con sus relaciones, incluyendo los tipos de relación y los elementos relacionados.

2. **Consulta de Personas Casadas:**
   - Permite encontrar todas las personas que están casadas.

3. **Consulta de Personas Padres:**
   - Permite encontrar todas las personas que son padres.

4. **Consulta de Personas Mayores de 50 Años:**
   - Permite encontrar todas las personas que tienen una edad mayor a 50 años.

5. **Consulta de Personas Aficionadas a la Música:**
   - Permite encontrar todas las personas a quienes les gusta la música.

## Uso de la Aplicación

1. **Inicio de la Aplicación:**
   - Al ejecutar la aplicación, se mostrará una página principal con las opciones de consulta disponibles.

2. **Selección de Consultas:**
   - El usuario puede seleccionar las consultas deseadas para ver los resultados correspondientes.

3. **Visualización de Resultados:**
   - Los resultados de las consultas se mostrarán en la misma página, permitiendo al usuario ver la información de manera clara y ordenada.

4. **Interacción con la Base de Datos:**
   - La aplicación utiliza una base de datos Neo4j para almacenar y consultar la información sobre las relaciones entre las personas.

## Configuración del Programa

1. **Conexión con la Base de Datos Neo4j:**
   - Asegurarse de modificar la función de conexión a Neo4j (`uri`, `user`, `password`) con la información correcta para establecer la conexión.

2. **Ejecución de la Aplicación:**
   - Ejecutar el script principal (`app.py`) para iniciar la aplicación.

## Requisitos

1. **Python:**
   - Se requiere tener Python instalado en el sistema.

2. **Librerías:**
   - Asegurarse de tener las librerías necesarias instaladas, como Flask y la librería de Neo4j.

3. **Base de Datos Neo4j:**
   - Se necesita una instancia de Neo4j para almacenar y gestionar la información de la red social.

## Créditos

Desarrollado por Antonietta Palazzo y Kevin Herrera.
