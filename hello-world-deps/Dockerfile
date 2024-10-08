# Imagem oficial do Python - versão 3.12
FROM python:3.12-slim

# Define o local/pasta de trabalho
WORKDIR /app

# Copia o conteúdo da pasta atual (local) para o path /app (container)
COPY . /app

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Define a variável de ambiente
ENV APP_ENV=development

# Roda o comando abaixo quando o container roda
CMD ["python", "hello_world.py"]
