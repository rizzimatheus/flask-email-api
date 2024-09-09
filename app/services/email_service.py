import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_USER, EMAIL_PASS, SMTP_HOST, SMTP_PORT

def send_email_service(to, subject, body):
    try:
        # Configura o servidor SMTP
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)

        # Monta o e-mail
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Envia o e-mail
        server.sendmail(EMAIL_USER, to, msg.as_string())
        server.quit()

        return 'E-mail enviado com sucesso!'
    except Exception as e:
        raise Exception(f"Erro ao enviar e-mail: {str(e)}")
