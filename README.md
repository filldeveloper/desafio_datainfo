# Desafio Datainfo
Desafio técnico proposto pela empresa Datainfo

# Pré-requisitos

Para esse projeto será necessário:
- Git;
- Python3;
- Pip;
- Docker;
- Postman

Prosseguir com as devidas instalações de acordo com o Sistema Operacional utilizado.

### Clonar repositório
```bash
$ git clone https://github.com/filldeveloper/desafio_datainfo.git
```
# Comando Docker para preparar o banco de dados

Baixando a imagem do mongodb
```bash
$ docker pull mongo
```

Rodonda a imagem mongo
```bash
$ docker run -d -p 27017:27017 -e AUTH=no mongo
```

### Criando ambiente virtual

A criação do ambiente virtual é opcional.
```bash
$ python3 -m venv venv
```

### Instalando bibliotecas

Vá para a onde foi clonado o repositório e instale as bibliotecas através do requirements.
```bash
$ pip install -r requirements.txt
```

### Rodando a aplicação

Navegue até a pasta onde foi clonado o projeto e execute a aplicação.
```bash
$ python3 app.py
```

OBS. O banco de dados está vazio, então será necessário primeiro fazer um POST utilizando o Postman. Segue exemplo de como deve ser:
{
    "autor": "Fulano de Tal",
    "noticia": "Escrever algum texto aqui",
    "titulo": "Escrever algum texto aqui"
}

### Métodos e parâmetros possíveis

Seguem os métodos e parâmetros possíveis de serem executados com a aplicação.

- POST (com o exemplo informado):
http://127.0.0.1:5000/noticias

- GET:
http://127.0.0.1:5000/noticias

- PUT:
http://127.0.0.1:5000/noticias/id       (O id será coletado após o GET)

- DELETE:
http://127.0.0.1:5000/noticias/id
