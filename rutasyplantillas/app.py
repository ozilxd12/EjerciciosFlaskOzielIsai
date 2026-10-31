from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/registrar")
def registrar():
    return render_template("registrar.html")

@app.route("/libros")
def libros():
    libro = "Matematicas"
    Autor = 25
    return render_template('libros.html', titulodellibro=libro, autordellibro=Autor)

@app.route('/enviar', methods=['POST'])
def recibir_datos():
    # Capturamos el dato usando el atributo 'name' del input
    nombredelibro = request.form.get('nombre')
    titulodellibro = request.form.get('autor')
    return f"¡Hola, Titulo:{nombredelibro}, Autor:{titulodellibro}, | Datos recibidos con éxito."

if __name__ == "__main__":
    app.run()
