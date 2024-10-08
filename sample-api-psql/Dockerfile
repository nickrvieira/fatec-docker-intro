# Imagem oficial do Python - versão 3.12
FROM python:3.12-slim

# Define o local/pasta de trabalho
WORKDIR /app

# Copia o APP para o container
COPY api/hello_world.py /app
COPY requirements.txt /app

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8000
EXPOSE 8000

# Roda o comando abaixo quando o container roda
CMD ["fastapi", "run", "hello_world.py"]
