import unittest
from app import app
from unittest.mock import patch

class TestEmailController(unittest.TestCase):

    def setUp(self):
        # Configura a aplicação para os testes
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.controllers.email_controller.send_email_service')
    def test_send_email_success(self, mock_send_email):
        # Configura o mock para simular um envio bem-sucedido
        mock_send_email.return_value = "E-mail enviado com sucesso!"

        # Dados da requisição POST
        payload = {
            "to": "destinatario@example.com",
            "subject": "Assunto do E-mail",
            "body": "Conteúdo do E-mail"
        }

        # Faz a requisição POST para a rota /send-email
        response = self.app.post('/send-email', json=payload)

        print(f"[{response.status_code}] {response.get_data(as_text=True)}")

        # Verifica o código de resposta
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"E-mail enviado com sucesso", response.data)

    def test_send_email_missing_fields(self):
        # Faz a requisição POST com dados incompletos
        payload = {
            "to": "test@destino.com",
            "subject": ""
        }
        response = self.app.post('/send-email', json=payload)

        # Verifica o código de resposta e a mensagem de erro
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Todos os campos sao obrigatorios", response.data)

if __name__ == '__main__':
    unittest.main()
