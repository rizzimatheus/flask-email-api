from flask import request, jsonify
from app.services.email_service import send_email_service
from config import logger

def send_email():
    try:
        # Obtém os dados enviados no corpo da requisição
        data = request.get_json()
        to = data.get('to')
        subject = data.get('subject')
        body = data.get('body')

        # Validações básicas
        if not to or not subject or not body:
            msg = "Todos os campos sao obrigatorios"
            logger.info(f"[Fail: {msg}] Data: {data}")
            return jsonify({'message': msg}), 400

        logger.info("Processando envio de email...")
        
        # Chama o serviço para enviar o e-mail
        email_result = send_email_service(to, subject, body)

        logger.info(f"[Success] Data: {data}")
        return jsonify({'message': 'E-mail enviado com sucesso', 'result': email_result}), 200
    except Exception as e:
        msg = 'Erro ao enviar e-mail'
        logger.info(f"[Fail: {msg} - {str(e)}] Data: {data}")
        return jsonify({'message': msg, 'error': str(e)}), 500
