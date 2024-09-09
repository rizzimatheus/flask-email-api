from flask import Flask
from app.routes.email_routes import email_bp
from flask_swagger_ui import get_swaggerui_blueprint
from config import logger
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
app.register_blueprint(email_bp)

metrics = PrometheusMetrics(app, group_by='endpoint')

# Swagger setup
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API de Envio de E-mails"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
