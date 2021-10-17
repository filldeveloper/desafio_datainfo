from flask import Flask, request, Response
from database.db import inicializa_db
from database.models import News

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/test'
}

inicializa_db(app)

@app.route('/noticias')
def get_noticias():
    noticias = News.objects().to_json()
    return Response(noticias, mimetype="application/json", status=200)

@app.route('/noticias', methods=['POST'])
def add_noticia():
    conteudo = request.get_json()
    noticia = News(**conteudo).save()
    id = noticia.id
    return {'id': str(id)}, 200

@app.route('/noticias/<id>', methods=['PUT'])
def update_movie(id):
    conteudo = request.get_json()
    News.objects.get(id=id).update(**conteudo)
    return 'Notícia Atualizado!', 200

@app.route('/noticias/<id>', methods=['DELETE'])
def delete_movie(id):
    News.objects.get(id=id).delete()
    return 'Notícia Excluída!', 200

if __name__ == '__main__':
    app.run(debug=True)