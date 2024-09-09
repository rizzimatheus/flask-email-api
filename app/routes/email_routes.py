from flask import Blueprint
from app.controllers.email_controller import send_email

email_bp = Blueprint('email', __name__)

# Definindo a rota POST para envio de e-mails
@email_bp.route('/send-email', methods=['POST'])
def send_email_route():
    return send_email()
