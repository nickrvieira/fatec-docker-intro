import os

import asyncpg
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "Hello, World!"}


class Item(BaseModel):
    name: str
    description: str


@app.post("/items/")
async def criar_item(item: Item) -> dict:
    """Essa função cria um item no banco de dados
    PS: Essa é uma versão extremamente simplificada e
    conexões com a DB não deveriam ser feitas dessa forma
    PS2: E a inserção tão pouco.

    Isso é apenas um exemplo para fins didáticos.

    :param item: Item para ser registrado no banco de dados
    :type item: Item
    :return: mensagem
    :rtype: dict
    """
    conn = await asyncpg.connect(
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        database=os.getenv("POSTGRES_DB"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
    )
    await conn.execute(
        """
        INSERT INTO items(name, description) VALUES($1, $2)
    """,
        item.name,
        item.description,
    )
    await conn.close()
    return {"message": f"Item {item.name} criado com sucesso"}
