# Creando un servidor Web con Flask para proporcionar servicios
# mediante los métodos GET, PUT, DELETE, POST
# Prof. Gabriel Barrón R.
#Julián Alexis Cano Cruces


import json
import sqlite3
from flask import Flask, request, jsonify


import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crud.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET donde busca un nombre
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM videojuegos')
    data = cursor.fetchall()
    for reg in data:
       registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))


@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO usuario(id, nombre, desarrolladora, lanzamiento, clasificacion ) VALUES(?,?,?,?,?)'
    cursor.execute(insert, [record['id'], record['nombre'], record['desarrolladora'], record['lanzamiento'], record['clasificacion']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
   
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM usuario WHERE id= ?'
    cursor.execute(delete, [record['id']])
    conn.commit()
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'UPDATE usuario SET nombre,desarrolladora,lanzamiento,clasificacion = ?,?,?,? WHERE id= ?'
    cursor.execute(delete, [record['email'], record['name']])
    conn.commit()
    return jsonify(record)
app.run(debug=True)