from flask import Blueprint, redirect, request, jsonify, url_for
from database.database_manager import database_manager
from bson import ObjectId
import os

task_bp = Blueprint('task', __name__)

# Accede a las variables de entorno
DB_URI = os.getenv('MONGO_URI')

@task_bp.route('/tasks', methods=['GET'])
def list_tasks():
    # Obtener la colección de tareas directamente desde la instancia de database_manager
    tasks_collection = database_manager.get_db()['tasks']
    tasks = list(tasks_collection.find())  # Obtener todas las tareas y convertir el cursor a una lista
    return jsonify(tasks)

@task_bp.route('/add-task', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    task_priority = request.form.get('task_priority')

    # Crear un diccionario con los datos de la tarea
    task_data = {
        'name': task_name,
        'priority': task_priority
    }

    # Usar la instancia global de DatabaseManager para insertar la tarea
    collection_name = 'tasks'
    inserted_id = database_manager.insert(db_name=None,collection_name=collection_name, data=task_data)

    return redirect(url_for('home.home'))  # Redirige de vuelta a la página de inicio

@task_bp.route('/tasks/<task_id>', methods=['PUT'])
def modify_task(task_id):
    task_data = request.json
    if not ObjectId.is_valid(task_id):
        return jsonify({'error': 'Invalid task ID'}), 400

    collection_name = 'tasks'
    result = database_manager.update(collection_name=collection_name, task_id=ObjectId(task_id), data=task_data)
    
    if result == 0:
        return jsonify({'error': 'Task not found'}), 404

    return jsonify({'message': 'Task updated successfully'})

@task_bp.route('/tasks/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    if not ObjectId.is_valid(task_id):
        return jsonify({'error': 'Invalid task ID'}), 400

    collection_name = 'tasks'
    result = database_manager.delete(collection_name=collection_name, task_id=ObjectId(task_id))
    
    if result == 0:
        return jsonify({'error': 'Task not found'}), 404

    return '', 204
