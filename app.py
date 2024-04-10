from flask import Flask
from flask import render_template, redirect, request, Response, session
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__,template_folder='template')

app.config['MySQL_HOST']='localhost'
app.config['MySQL_USER']='root'
app.config['MySQL_PASSWORD']=''
app.config['MySQL_DB']='login'
app.config['MySQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

#funcion de login
@app.route('/acceso-login', methods=["GET", "POST"])
def login():

    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtContraseña':
        correo = request.form['txtCorreo']
        constraseña = request.form['txtContraseña']

        cur=mysql.connection.cursor()
        cur.execute('SELECT *  FROM usuarios WHERE correo =%s AND contraseña = %s', (_correo, _contraseña))
        account = cur.fetchone()

        if account:
            session['Se ha iniciado Sesion'] = True
            session['id'] = account['id'] 

            return render_template("admin.html")           
        else:
            return render_template("index.html")

    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key="key"
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)