from flask import Flask, jsonify, request,json
from random import choice
app = Flask(__name__)

from album import album

@app.route('/api/album', methods=['POST'])
def agregarAlbum():
    nuevoAlbum = {
        "id":request.json['id'],
        "name": request.json['name'],
        "created_at": request.json['created_at']
    }
    album.append(nuevoAlbum)
    return jsonify ({"msg": "Album agregado exitosamente"},200)

@app.route('/api/album', methods=['GET'])
def listarAlbum():
    if len(album)==0:
        return jsonify ({"Album":album,"msg": "No hay album"},400)
    return jsonify({"Album":album},200)


@app.route('/api/album/<string:id_album>/stamp', methods=['POST'])
def obtenerAlbum(id_album):
    #Recupera los datos en formato json 
    datos = open('teams.json',encoding="utf8")
    equipos = datos.read()
    #Convierte el tipo de dato
    teams_album = json.loads(equipos)
    
    albumEncontrado = [unAlbum for unAlbum in album if unAlbum['id']==id_album]  

    if (len(albumEncontrado)>0):
        #"Instrucciones a realizar"
        sobre = []
        for _ in range (6):
            equipo=choice(teams_album)
            jugador = choice(equipo['elements'])
            sobre.append(jugador)
        
        clave = "Estampita"
        valores = sobre
        album[0].update({clave:valores})

        
        return jsonify ({"Estampillas":sobre},200)        

    return jsonify ({"msg":"El album no existe"},400)


if __name__ == "__main__":
    app.run(debug=True, port=4000) 

