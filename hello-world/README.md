# Hello World


## Para buildar:

```
docker build -t hello_world_fatec:v1.0.0 .
```

- `-t` especifica o nome da imagem. O caractere `:` é opcional e pode ser seguido de uma tag/versão.
- `.` indica que o Dockerfile está no diretório atual.

## Para rodar:

```
docker run hello_world_fatec:v1.0.0
```