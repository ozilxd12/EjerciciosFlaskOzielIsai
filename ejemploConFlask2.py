from flask import Flask

app = Flask(__name__)

# Ruta principal (Home)
@app.route('/')
def home():
    return "¡Hola! Esta es la página de inicio."

# Ruta personalizada
@app.route('/contacto')
def contacto():
    return "Página de contacto de mi web."

# Ruta con parámetros (ej. /usuario/juan)
@app.route('/usuario/<nombre>')
def perfil_usuario(nombre):
    return f"Bienvenido al perfil de, Oziel Isai"

if __name__ == '__main__':
    app.run(debug=True)
