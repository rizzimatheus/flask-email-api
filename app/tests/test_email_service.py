import unittest
from unittest.mock import patch
from app.services.email_service import send_email_service

class TestEmailService(unittest.TestCase):

    @patch('app.services.email_service.smtplib.SMTP')  # Mocka o SMTP
    def test_send_email_service_success(self, mock_smtp):
        # Configura o mock para o comportamento esperado
        instance = mock_smtp.return_value
        instance.sendmail.return_value = {}

        # Chama a função do serviço de envio de e-mails
        result = send_email_service("destinatario@example.com", "Assunto do E-mail", "Conteúdo do E-mail")

        # Verifica se o retorno foi de sucesso
        self.assertEqual(result, 'E-mail enviado com sucesso!')

    @patch('app.services.email_service.smtplib.SMTP')
    def test_send_email_service_failure(self, mock_smtp):
        # Configura o mock para levantar uma exceção
        instance = mock_smtp.return_value
        instance.sendmail.side_effect = Exception('Erro no envio de e-mail')

        # Verifica se a exceção é levantada corretamente
        with self.assertRaises(Exception) as context:
            send_email_service("destinatario@example.com", "Assunto do E-mail", "Conteúdo do E-mail")

        self.assertIn('Erro ao enviar e-mail', str(context.exception))

if __name__ == '__main__':
    unittest.main()
