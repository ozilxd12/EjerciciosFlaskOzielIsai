from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal que muestra la interfaz y procesa el formulario
@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route('/Paisaje1')
def Paisaje1():
    return render_template('archivo1.html')

@app.route('/Paisaje2')
def Paisaje2():
    return render_template('archivo2.html')

@app.route('/Paisaje3')
def Paisaje3():
    return render_template('archivo3.html')

if __name__ == '__main__':
    app.run(debug=True)
