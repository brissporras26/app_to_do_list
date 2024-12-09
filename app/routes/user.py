from flask import Blueprint, redirect, url_for, session, request, flash, render_template
from app.logic.users_logic import register_user_logic, login_user_logic, auth_callback_logic, logout_user_logic

import os

# Blueprint para las rutas de usuario
user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['GET', 'POST'])
def add_user():
    """
    Ruta para registrar un nuevo usuario.
    """
    if request.method == 'POST':
        email_user = request.form.get('email')
        password_user = request.form.get('password')

        # Llamar a la lógica para registrar el usuario
        register_user_logic(email_user, password_user)
        flash("Registro exitoso. Por favor inicia sesión.", 'success')
        return redirect(url_for('user.get_user'))

    return render_template('register.html')

@user_bp.route('/', methods=['GET', 'POST'])
def get_user():
    """
    Ruta para manejar el inicio de sesión local.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Llamar a la lógica para verificar el inicio de sesión
        if login_user_logic(email, password):
            flash("Has iniciado sesión exitosamente.", 'success')
            session['user_email'] = email  # Guarda el email en la sesión
            return redirect(url_for('home.home'))  # Redirige al home después de login exitoso
        else:
            flash("Email o contraseña incorrectos.", 'error')

    return render_template('login.html')

@user_bp.route('/login')
def login():
    """
    Redirige al usuario a Auth0 para autenticación.
    """
    return redirect(url_for('auth.auth_callback'))  # Redirige al callback de Auth0

@user_bp.route('/auth/callback')
def auth_callback():
    """
    Maneja el callback después de la autenticación en Auth0.
    """
    result = auth_callback_logic(session)
    flash(result['message'], result['status'])
    return redirect(result['redirect_url'])  # Redirige después del login con Auth0

@user_bp.route('/logout')
def logout():
    """
    Cierra la sesión del usuario y redirige a la página principal.
    """
    result = logout_user_logic(session)
    flash(result['message'], result['status'])
    return redirect(result['redirect_url'])
