from flask import Blueprint, redirect, session, url_for, flash
from app.logic.users_logic import auth_callback_logic

# Blueprint para las rutas de autenticación
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/callback')
def auth_callback():
    """
    Maneja el callback después de la autenticación en Auth0.
    Esta ruta es llamada después de que Auth0 redirige al usuario
    con un código de autorización.
    """
    result = auth_callback_logic(session)
    flash(result['message'], result['status'])
    return redirect(result['redirect_url'])
