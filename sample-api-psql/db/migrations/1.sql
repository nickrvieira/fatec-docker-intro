CREATE DATABASE fatec;

\c fatec

CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    description VARCHAR(1024) NOT NULL
);