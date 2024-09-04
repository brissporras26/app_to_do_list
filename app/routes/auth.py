from flask import Blueprint, render_template, request, redirect, url_for
from app.logic.auth_logic import  authenticate_user, create_user  # Asegúrate de que esta función esté definida en auth_logic

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if authenticate_user(email, password):
            # Redirige al usuario a la página principal o a otra página después del login
            return redirect(url_for('home.home'))
        else:
            # Manejo de error si el login falla
            return render_template('login.html', error='Invalid credentials')
    
    # Renderiza la página de login para solicitudes GET
    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Aquí debes implementar la lógica para registrar al usuario en la base de datos
        # Supongamos que tienes una función `create_user` para manejar el registro
        if create_user(username, email, password):
            return redirect(url_for('home.home'))
        else:
            # Manejo de error si el registro falla
            return render_template('register.html', error='Registration failed')
    
    # Renderiza la página de registro para solicitudes GET
    return render_template('register.html')
