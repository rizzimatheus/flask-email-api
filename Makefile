# Nome da imagem Docker
IMAGE_NAME = flask-email-api
DOCKER_TAG = latest

# Porta para rodar o servidor
PORT = 5000

# Variáveis de ambiente (por exemplo, desenvolvimento)
ENV = development

# Nome do arquivo env
ENV_FILE = .env

# Definições de comandos
.PHONY: help
help:
	@echo "Comandos disponíveis:"
	@echo "  make init               - Instala as dependências do projeto"
	@echo "  make run                - Inicia o servidor Flask"
	@echo "  make test               - Roda os testes unitários"
	@echo "  make docker-build       - Constrói a imagem Docker"
	@echo "  make docker-run         - Roda a aplicação via Docker"
	@echo "  make docker-test        - Roda os testes unitários dentro do container Docker"
	@echo "  make clean              - Remove arquivos de cache e imagens Docker"

# Inicializa o projeto, instalando as dependências
.PHONY: init
init: create-env
	@echo "Instalando dependências..."
	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

# Gera o arquivo .env
.PHONY: create-env
create-env:
	@if [ -f $(ENV_FILE) ]; then \
		echo "$(ENV_FILE) já existe. Nenhuma ação necessária."; \
	else \
		echo "Criando arquivo .env..."; \
		echo "EMAIL_USER=" >> $(ENV_FILE); \
		echo "EMAIL_PASS=" >> $(ENV_FILE); \
		echo "SMTP_HOST="smtp.gmail.com"" >> $(ENV_FILE); \
		echo "SMTP_PORT=587" >> $(ENV_FILE); \
		echo ".env criado com sucesso!"; \
	fi

# Inicia o servidor Flask localmente
.PHONY: run
run:
	@echo "Iniciando o servidor Flask..."
	FLASK_ENV=$(ENV) FLASK_APP=run.py flask run --host=0.0.0.0 --port=$(PORT)

# Roda os testes unitários
.PHONY: test
test:
	@echo "Rodando testes..."
	python -m coverage run -m unittest discover -s app/tests -v
	python -m coverage report

# Constrói a imagem Docker
.PHONY: docker-build
docker-build:
	@echo "Construindo a imagem Docker..."
	docker build -t $(IMAGE_NAME):$(DOCKER_TAG) .

# Roda a aplicação via Docker
.PHONY: docker-run
docker-run:
	@echo "Iniciando o container Docker..."
	docker run --rm -p $(PORT):$(PORT) $(IMAGE_NAME):$(DOCKER_TAG)

# Roda os testes dentro do container Docker
.PHONY: docker-test
docker-test:
	@echo "Rodando testes dentro do container Docker..."
	docker run --rm $(IMAGE_NAME):$(DOCKER_TAG) python -m unittest discover -s app/tests -v

# Limpa arquivos temporários e containers
.PHONY: clean
clean:
	@echo "Removendo arquivos temporários e containers..."
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
	docker rmi $(IMAGE_NAME)
