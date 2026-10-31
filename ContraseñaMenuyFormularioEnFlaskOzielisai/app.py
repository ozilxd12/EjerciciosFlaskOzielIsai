from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conectar a la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bibliotecaozielisai'
mysql = MySQL(app)

# Configuraciones
app.secret_key = 'mysecretkey'

@app.route("/")
def inicio():
    return render_template("contraseña.html")

@app.route('/Login', methods=['POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')
        
        if usuario == 'admin' and password == '1234':
            return redirect(url_for('Menuprincipal'))
        else:
            flash('Contraseña incorrecta, vuelve a intentarlo')
            return redirect(url_for('inicio'))

# RUTA CORREGIDA: Acepta minúscula y mayúscula para evitar el error 404
@app.route("/Menuprincipal")
@app.route("/MenuPrincipal")
def Menuprincipal():
    return render_template("menu.html")

@app.route("/Empleados")
@app.route("/empleados")
def Empleados():
    return render_template("empleados.html")

@app.route('/Libros')
def Libros():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM libros')
    data = cur.fetchall()
    cur.close()
    return render_template('libros.html', libros = data)

@app.route('/Agregar_Libro', methods=['POST'])
def Agregar_Libro():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        edicion = request.form.get('edicion')
        año = request.form.get('año')
        editorial = request.form.get('editorial')
        nopaginas = request.form.get('nopaginas')
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO libros (Titulo, Autor, Edicion, Año, Editorial, NoPaginas) VALUES (%s, %s, %s, %s, %s, %s)',
                    (titulo, autor, edicion, año, editorial, nopaginas))
        mysql.connection.commit()
        cur.close()
        flash('Libro Agregado satisfactoriamente')
        return redirect(url_for('Libros'))

@app.route('/Modificarlibro/<id>')
def ModificarLibro(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM libros WHERE id=%s', (id,))
    data = cur.fetchall()
    cur.close()
    return render_template('modificarLibros.html', libros = data)

@app.route('/ActualizarLibro/<id>', methods=['POST'])
def ActualizarLibro(id):
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        edicion = request.form.get('edicion')
        año = request.form.get('año')
        editorial = request.form.get('editorial')
        nopaginas = request.form.get('nopaginas')
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE libros
            SET Titulo=%s,
                Autor=%s,
                Edicion=%s,
                Año=%s,
                Editorial=%s,
                NoPaginas=%s
            WHERE id=%s
        """, (titulo, autor, edicion, año, editorial, nopaginas, id))
        mysql.connection.commit()
        cur.close()
        flash('Libro actualizado exitosamente')
        return redirect(url_for('Libros'))

@app.route('/EliminarLibro/<string:id>')
def EliminarLibro(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM libros WHERE id=%s', (id,))
    mysql.connection.commit()
    cur.close()
    flash('Libro eliminado satisfactoriamente')
    return redirect(url_for('Libros'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
