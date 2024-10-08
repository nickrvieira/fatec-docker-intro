# Hello World (FastAPI)


## Para buildar:

```
docker build -t hello_world_fatec:v3.0.0 .
```

- `-t` especifica o nome da imagem. O caractere `:` é opcional e pode ser seguido de uma tag/versão.
- `.` indica que o Dockerfile está no diretório atual.

## Para rodar:

```
docker run hello_world_fatec:v3.0.0
```

Esse launch não expõe nenhuma porta do container.

```
docker run -p 9000:8000 hello_world_fatec:v3.0.0
```

O argumento `-p 9000:8000` mapeia a porta 8000 do container para a porta 9000 do host.
