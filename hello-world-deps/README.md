# Hello World


## Para buildar:

```
docker build -t hello_world_fatec:v2.0.0 .
```

- `-t` especifica o nome da imagem. O caractere `:` é opcional e pode ser seguido de uma tag/versão.
- `.` indica que o Dockerfile está no diretório atual.

## Para rodar:

```
docker run hello_world_fatec:v2.0.0
```

Essa opção utilizará os as ENVs defaults do Dockerfile.

```
docker run -e APP_ENV=production hello_world_fatec:v2.0.0
```

Essa opção sobrescreverá a ENV `APP_ENV` do Dockerfile com a string "production".
