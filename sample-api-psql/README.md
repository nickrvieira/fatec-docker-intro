# Hello World (FastAPI + Postgres)


## Para rodar:

Diferentemente das outras ocasiões, utilizaremos o `docker compose` para buildar e rodar o projeto

```bash
docker compose up -d --build --force-recreate --no-deps
```

O compose fica definido no arquivo `docker-compose.yml` e é composto por 2 serviços:
- api: serviço que roda a aplicação FastAPI
- db: serviço que roda o banco de dados Postgres

Para validar que ambos serviços est˜ao rodando, execute:

```bash
docker ps
```

(deve apresentar dois containers em pé, um para o postgres e um para a API)

### Para testar o hello:

```bash
curl --request GET \
     --url localhost:8000/hello
```

### Para testar o banco de dados:

```bash
curl -X POST "http://127.0.0.1:8000/items/" \
    -H "Content-Type: application/json" \
    -d '{"name": "Esse é um item feliz!", "description": "para palestra da fatec"}'
```

## Para desativar os containers do compose:

```bash
docker compose down
```
