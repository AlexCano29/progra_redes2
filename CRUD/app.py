# -*- coding: utf-8 -*-
# Creando un servidor Web con Flask para proporcionar servicios
# mediante los métodos GET, PUT, DELETE, POST
# Julián Alexis Cano Cruces


import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('/home/linux19/Documentos/scripts/ejemplo.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET para obtener todos los registros
@app.route('/videojuegos', methods=['GET'])
def query_records():
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Videojuegos')
    data = cursor.fetchall()
    for reg in data:
        registros.append(dict(reg))
    conn.close()
    return jsonify(registros)

# Método GET para buscar por ID
@app.route('/videojuegos/<int:videojuego_id>', methods=['GET'])
def get_record(videojuego_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Videojuegos WHERE id = ?', (videojuego_id,))
    data = cursor.fetchone()
    conn.close()
    if data is None:
        return jsonify({'error': 'No se encontró el videojuego'}), 404
    else:
        return jsonify(dict(data))

# Método PUT para agregar un nuevo registro
@app.route('/videojuegos', methods=['PUT'])
def create_record():
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO Videojuegos(nombre, desarrolladora, lanzamiento, clasificacion) VALUES(?,?,?,?)'
    cursor.execute(insert, [record['nombre'], record['desarrolladora'], record['lanzamiento'], record['clasificacion']])
    conn.commit()
    return jsonify(record), 201

# Método DELETE para eliminar un registro por ID
@app.route('/videojuegos/<int:videojuego_id>', methods=['DELETE'])
def delete_record(videojuego_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM Videojuegos WHERE id= ?'
    cursor.execute(delete, (videojuego_id,))
    conn.commit()
    conn.close()
    return jsonify({'result': True})

# Método POST para actualizar un registro por ID
@app.route('/videojuegos/<int:videojuego_id>', methods=['POST'])
def update_record(videojuego_id):
    record = json.loads(request.data)

    conn = get_db_connection()
    cursor = conn.cursor()
    update = 'UPDATE Videojuegos SET nombre = ?, desarrolladora = ?, lanzamiento = ?, clasificacion = ? WHERE id= ?'
    cursor.execute(update, [record['nombre'], record['desarrolladora'], record['lanzamiento'], record['clasificacion'], videojuego_id])
    conn.commit()
    conn.close()
    return jsonify(record)

app.run(debug=True)
