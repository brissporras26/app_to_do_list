from flask import Blueprint, render_template, session, redirect, url_for
from database.database_manager import database_manager

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    # Check if user is authenticated via either method
    if not session.get('user_email') and not session.get('user'):
        return redirect(url_for('user.get_user'))
    
    tasks_collection = database_manager.get_db()['tasks']
    
    # Get user_email from either OAuth or regular login
    user_email = session.get('user_email') or session.get('user', {}).get('email')
    
    # Get tasks for the specific user
    tasks = list(tasks_collection.find({'user_email': user_email}))
    print(f'Tasks to render: {tasks}')  # Debug print
    
    return render_template('home.html', tasks=tasks, user_email=user_email)