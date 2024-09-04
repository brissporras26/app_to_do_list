import uuid
from database.database_manager import  database_manager

def create_task(name, priority):
    """
    Crea una nueva tarea en la colección 'tasks'.
    :param name: Nombre de la tarea.
    :param priority: Prioridad de la tarea (alta, media, baja).
    :return: ID de la tarea creada.
    """
    try:
        task_id = str(uuid.uuid4())  # Genera un ID único para la tarea
        task_data = {
            'task_id': task_id,
            'name': name,
            'priority': priority
        }
        inserted_id = database_manager.insert('tasks', task_data)
        return inserted_id
    except Exception as e:
        print(f"Error al crear la tarea: {e}")
        raise

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

        update_result = database_manager.update('tasks', {'task_id': task_id}, update_data)
        return update_result > 0
    except Exception as e:
        print(f"Error al actualizar la tarea: {e}")
        raise

def delete_task(task_id):
    """
    Elimina una tarea de la colección 'tasks'.
    :param task_id: ID de la tarea a eliminar.
    :return: True si la eliminación fue exitosa, False en caso contrario.
    """
    try:
        result = database_manager.delete('tasks', {'task_id': task_id})
        return result > 0
    except Exception as e:
        print(f"Error al eliminar la tarea: {e}")
        raise
