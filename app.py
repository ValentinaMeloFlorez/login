from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

usuarios = []

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/registro', methods=['POST'])
def registro():
    datos = request.json

    usuario = datos['usuario']
    password = datos['password']

    usuarios.append({
        "usuario": usuario,
        "password": password
    })

    return jsonify({"mensaje": "Usuario registrado correctamente"})


@app.route('/login', methods=['POST'])
def login():
    datos = request.json

    usuario = datos['usuario']
    password = datos['password']

    for u in usuarios:
        if u['usuario'] == usuario and u['password'] == password:
            return jsonify({"mensaje": "Autenticación satisfactoria"})

    return jsonify({"error": "Error en la autenticación"})


if __name__ == '__main__':
    app.run(debug=True)