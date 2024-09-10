from flask import Blueprint, redirect, request, jsonify, url_for
from database.database_manager import database_manager
from bson import ObjectId
import os
from bson import ObjectId
from app.logic.task_logic import add_task_logic



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

    # Llamar a la lógica para agregar la tarea
    add_task_logic(task_name, task_priority, database_manager)

    return redirect(url_for('home.home'))  # Redirige de vuelta a la página de inicio

@task_bp.route('/tasks-edit/<task_id>', methods=['POST'])
def modify_task(task_id):
    if request.form.get('_method') == 'PUT':
        task_name = request.form.get('task_name')
        task_priority = request.form.get('task_priority')

        if not ObjectId.is_valid(task_id):
            return jsonify({'error': 'Invalid task ID'}), 400

        # Definir los datos actualizados
        updated_data = {
            'name': task_name,
            'priority': task_priority
        }

        try:
            # Llamar al método de actualización del DatabaseManager
            result = database_manager.update('tasks', task_id=ObjectId(task_id), data=updated_data)

            if result == 0:
                return jsonify({'error': 'Task not found'}), 404

            print(f"Tarea con ID {task_id} actualizada correctamente.")
            return redirect(url_for('home.home'))

        except Exception as e:
            print(f"Error al actualizar la tarea: {e}")
            return redirect(url_for('home.home'))
    else:
        return redirect(url_for('home.home'))



@task_bp.route('/tasks-delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    if request.form.get('_method') == 'DELETE':
        print(f"Request method: {request.method}")  
        print(f"Task ID received: {task_id}")  

        try:
            # Convertir task_id a ObjectId
            query = {'_id': ObjectId(task_id)}

            deleted_count = database_manager.delete('tasks', query)

            if deleted_count > 0:
                print(f"Tarea con ID {task_id} eliminada correctamente.")
                return redirect(url_for('home.home'))
            else:
                print(f"No se encontró una tarea con ID {task_id}.")
                return redirect(url_for('home.home'))
        except Exception as e:
            print(f"Error al eliminar la tarea: {e}")
            return redirect(url_for('home.home'))
    else:
        return redirect(url_for('home.home'))
