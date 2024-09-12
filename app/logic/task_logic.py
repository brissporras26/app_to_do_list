import uuid
from database.database_manager import  database_manager
from bson import ObjectId
from flask import redirect, url_for
# task_logic.py

def add_task_logic(task_name, task_priority, database_manager):
    # Crear un diccionario con los datos de la tarea
    task_data = {
        'name': task_name,
        'priority': task_priority
    }

    # Usar la instancia global de DatabaseManager para insertar la tarea
    collection_name = 'tasks'
    inserted_id = database_manager.insert(db_name=None, collection_name=collection_name, data=task_data)

    return inserted_id

def get_task_by_name(name):
    """
    Busca una tarea en la colección 'tasks' por su nombre.
    :param name: Nombre de la tarea.
    :return: Documento de la tarea si se encuentra, None en caso contrario.
    """
    try:
        task = database_manager.select('tasks', {'name': name})
        task_list = list(task)  # Convertir el cursor en una lista
        if not task_list:
            return None
        return task_list[0]
    except Exception as e:
        print(f"Error al obtener la tarea: {e}")
        raise

def update_task(task_id, new_name=None, new_priority=None):
    """
    Actualiza una tarea en la colección 'tasks'.
    :param task_id: ID de la tarea a actualizar.
    :param new_name: Nuevo nombre de la tarea (opcional).
    :param new_priority: Nueva prioridad de la tarea (opcional).
    :return: True si la actualización fue exitosa, False en caso contrario.
    """
    try:
        update_data = {}
        if new_name:
            update_data['name'] = new_name
        if new_priority:
            update_data['priority'] = new_priority

        if not update_data:
            return False  # No hay nada que actualizar

        update_result = database_manager.update(db_name=None, collection_name='tasks', query={'_id': ObjectId(task_id)}, update_data=update_data)
        return update_result > 0
    except Exception as e:
        print(f"Error al actualizar la tarea: {e}")
        raise

"""def delete_task(task_id):
    tasks_collection = database_manager.get_db()['tasks']
    try:
        result = tasks_collection.delete_one({'_id': ObjectId(task_id)})

        if result.deleted_count > 0:
            print(f"Tarea con ID {task_id} eliminada correctamente.")
        else:
            print(f"No se encontró una tarea con ID {task_id}.")
    except Exception as e:
        print(f"Error al eliminar la tarea: {e}")

    return redirect(url_for('home.home'))"""
