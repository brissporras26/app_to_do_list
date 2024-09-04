from flask import Blueprint, render_template, jsonify
from app.logic.task_logic import get_task_by_name
from database.database_manager import database_manager

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    # Obtener la colección de tareas directamente desde la instancia de database_manager
    tasks_collection = database_manager.get_db('ToDoCluster')['tasks']  # Asegúrate de reemplazar 'your_database_name' por tu base de datos real
    tasks = list(tasks_collection.find())  # Obtener todas las tareas y convertir el cursor a una lista
    
    return render_template('home.html', tasks=tasks)
