# Flask Email API
Este projeto é uma API RESTful construída com Flask para envio de e-mails, utilizando o serviço **smtplib** do Python. A API é documentada usando **Swagger**, possui testes unitários com **unittes** e utiliza **Docker** para facilitar o setup e deploy. Além disso, há suporte a **logging** e gerenciamento de dependências com **venv**.

## Sumário
- [Requisitos](#requisitos)
- [Setup do Projeto](#setup-do-projeto)
- [Configuração do Email com smtplib](#configuração-do-email-com-smtplib)
- [Documentação com Swagger](#documentação-com-swagger)
- [Executando Testes](#executando-testes)
- [Comandos do Makefile](#comandos-do-makefile)
- [Rodando com Docker](#rodando-com-docker)
- [Logging](#logging)
- [Coleta de Métricas com Prometheus](#coleta-de-métricas-com-prometheus)
- [Integração Contínua com GitHub Actions](#integração-contínua-com-github-actions)
- [Configuração do Virtual Environment (venv)](#configuração-do-virtual-environment-venv)
- [Descrição do Teste Técnico - Microserviço de Envio de E-mails](#descrição-do-teste-técnico---microserviço-de-envio-de-e-mails)

## Requisitos

- **Python 3.8+**
- **Docker** (opcional)
- **pip** (gerenciador de pacotes Python)
- **Virtualenv** (opcional, mas recomendado)

## Setup do Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/rizzimatheus/flask-email-api.git
cd flask-email-api
```

Utilize o comando abaixo para executar automaticamente os passos 2, 3 e 4, ou siga as instruções manualmente caso não tenha o make disponível:
```bash
make init
```

### 2. Criar o Ambiente Virtual (opcional, mas recomendado)
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate  # Windows
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o Arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```bash
EMAIL_USER=seu_email@gmail.com
EMAIL_PASS=sua_senha
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
```

### 5. Iniciar o Servidor

Para rodar o servidor Flask:

```bash
make run
```

Agora, a API estará disponível em `http://localhost:5000`.

## Configuração do Email com smtplib

O **smtplib** é uma biblioteca Python usada para enviar emails usando o protocolo SMTP. Neste projeto, as credenciais e o host SMTP são configurados no arquivo `.env` e utilizados dentro do serviço de email.

### Exemplo de Configuração:

- **Gmail**:
    - `SMTP_HOST=smtp.gmail.com`
    - `SMTP_PORT=587`
    - Se você utiliza a autenticação de dois fatores, é necessário criar uma Senha de App na sua conta Google.
- **Outros serviços de email**:
    - O host SMTP e porta variam. Consulte a documentação do seu provedor.

## Documentação com Swagger

A documentação da API foi gerada com **Flask-Swagger-UI** e está disponível através da seguinte URL após iniciar o servidor:

```bash
http://localhost:5000/swagger/
```

Esta documentação contém os endpoints disponíveis, como enviar um email, e os parâmetros esperados.

## Executando Testes

Este projeto inclui testes unitários utilizando **unittest**. Para rodar os testes, use o seguinte comando:

```bash
make test
```

Isso irá executar todos os testes na pasta `tests/` e gerar um relatório sobre a cobertura dos testes.


## Comandos do Makefile

O Makefile facilita a execução de tarefas comuns. Utilize `make help` para ver todos os comandos disponíveis.

## Rodando com Docker

O projeto inclui um **Dockerfile** para facilitar a criação de um ambiente isolado. Para rodar a aplicação usando Docker:

### 1. Construir a Imagem Docker

```bash
make docker-build
```

### 2. Rodar o Container

```bash
make docker-run
```

A aplicação estará disponível em `http://localhost:5000`.

## Logging

O projeto utiliza o módulo **logging** do Python para registrar informações de eventos e erros no console. O nível de logging pode ser ajustado conforme necessário para registrar apenas erros, avisos, ou informações mais detalhadas.

## Coleta de Métricas com Prometheus

Este projeto possui um endpoint dedicado à coleta de métricas para monitoramento via **Prometheus**.

### Endpoint `/metrics`

O endpoint `/metrics` está disponível para fornecer métricas sobre o desempenho e o estado da aplicação, como tempo de resposta das requisições, contagem de e-mails enviados, falhas e mais.

- **URL**: `http://localhost:5000/metrics`
- **Tipo de Resposta**: Métricas no formato adequado para scraping por **Prometheus**.

### Exemplo de Métricas Coletadas:

- Contagem de requisições HTTP
- Tempo de resposta por endpoint
- Sucesso ou falha no envio de e-mails
- Utilização de CPU e memória

### Configuração com Prometheus

Para integrar com **Prometheus**, adicione o seguinte trecho ao arquivo de configuração do Prometheus (`prometheus.yml`):

```yaml
scrape_configs:
  - job_name: 'flask-email-api'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:5000']
```

Isso configurará o Prometheus para coletar as métricas da sua aplicação Flask a cada 5 segundos.

### Visualização de Métricas

Depois de configurado, você pode visualizar e monitorar as métricas da sua API através do **Prometheus** ou integrá-lo com ferramentas de visualização como **Grafana** para criar dashboards interativos.

## Integração Contínua com GitHub Actions

Este projeto possui integração contínua configurada com **GitHub Actions** para executar automaticamente os testes unitários sempre que um **push** ou **pull request** é feito na branch `main`.

### Como Funciona:

- Quando um novo **commit** é enviado para a branch `main`, ou um **pull request** é aberto, o GitHub Actions automaticamente:
    1. Faz o **checkout** do código.
    2. Configura o ambiente Python.
    3. Instala as dependências do projeto listadas no `requirements.txt`.
    4. Executa os testes unitários utilizando o **unittest**.

### Monitoramento:

- O status de cada execução do workflow pode ser visualizado na aba **Actions** do repositório no GitHub.
- Em caso de falha nos testes, o desenvolvedor será notificado diretamente no GitHub, permitindo correções rápidas antes do merge na branch principal.

## Configuração do Virtual Environment (venv)

Recomenda-se usar um ambiente virtual para isolar as dependências do projeto e evitar conflitos. Para configurar:

### Criar um Ambiente Virtual:

```bash
python3 -m venv venv
```

### Ativar o Ambiente Virtual:

- **Linux/Mac**:
    
    ```bash
    source venv/bin/activate
    ```
    
- **Windows**:
    
    ```bash
    venv\Scripts\activate
    ```
    

### Instalar Dependências:

```bash
pip install -r requirements.txt
```

---

# Descrição do Teste Técnico - Microserviço de Envio de E-mails

## Instruções
Crie um microserviço simples que permita o envio de e-mails utilizando uma API RESTful. O objetivo é implementar e documentar a API de envio de e-mails e criar testes unitários para as rotas. Você pode escolher entre Node.js ou Python para a implementação, conforme sua preferência.

## Tarefas

1. **Configuração Inicial**
   - Configure um projeto Node.js utilizando Express.js ou um projeto Python utilizando Flask.
   - Crie uma estrutura básica de pastas para o projeto, incluindo `routes`, `controllers`, e `services`.

2. **Criação da API de Envio de E-mails**
   - Implemente uma rota POST `/send-email` que receba os seguintes dados no corpo da requisição:
     ```json
     {
       "to": "destinatario@example.com",
       "subject": "Assunto do E-mail",
       "body": "Conteúdo do E-mail"
     }
     ```
   - Utilize um serviço de envio de e-mails de sua escolha (por exemplo, Nodemailer, smtplib, ou qualquer outro). Documente claramente como configurar e utilizar o serviço escolhido.

3. **Documentação da API**
   - Crie uma documentação simples utilizando Swagger ou outra ferramenta de documentação para descrever a rota `/send-email`.

4. **Testes**
   - Implemente testes unitários para a rota criada utilizando uma biblioteca de testes como Jest (para Node.js) ou unittest/pytest (para Python).

## Configuração da Conta de E-mail

Para o envio de e-mails, você pode utilizar qualquer serviço de e-mail de sua escolha (por exemplo, Mailtrap, Gmail, etc.). Certifique-se de documentar claramente como configurar o serviço escolhido.

### Nota

Lembre-se de não expor credenciais sensíveis em seu código. Utilize variáveis de ambiente para configurá-las.

## Critérios de Avaliação

- **Funcionalidade**: O microserviço deve ser capaz de enviar e-mails corretamente.
- **Qualidade do Código**: O código deve ser bem estruturado, organizado e seguir boas práticas de desenvolvimento.
- **Documentação**: A API deve estar bem documentada e fácil de entender.
- **Testes**: A implementação de testes unitários é essencial para validar a robustez da aplicação.

## Recursos Disponíveis

- Documentação do Nodemailer: [Nodemailer](https://nodemailer.com/about/).
- Documentação do smtplib: [smtplib](https://docs.python.org/3/library/smtplib.html).

## Entrega

- Envie o link para o repositório do GitHub contendo o código-fonte do projeto.
- A entrega deve incluir instruções claras de como rodar a aplicação localmente.

Boa sorte! Estamos ansiosos para ver como você resolverá este desafio e demonstrará suas habilidades.
