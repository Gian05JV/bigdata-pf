from flask import Flask, render_template, url_for, request, session, redirect, flash
import postgres_service
from postgres_service import get_usuarios, get_usuario, insert_usuario, delete_usuario, insert_dispositivo
from init import create_app

app_web = create_app()
#app_web = Flask(__name__)
#app_web.secret_key = b'\xf1\x8eu\xf1\xaa\x10\xfc\xc6\xbc\xfb\xc9V\xc0/I\t\xe5\\h\x10<\xd8\xf7\x81'

@app_web.route("/",methods=['GET', 'POST'])
def inicio():
    return render_template("index.html")

@app_web.route("/isesion")
def isesion():
    return render_template("isesion.html")

@app_web.route("/isesion", methods=["POST"])
def iniciar_sesion():
    if request.method == "POST":
        correo = request.form["email"]
        password = request.form["password"]
        campus = request.form["campus"]
        usuario = postgres_service.get_acceso(correo, password, campus)

        if usuario != None:
            session['s_usuario'] = usuario.nombre
            return redirect(url_for("perfil"))
        else:
            flash("Error al escribir correo o password")
            return redirect(url_for("isesion"))

@app_web.route("/perfil")
def perfil():
    return render_template("perfil.html")

@app_web.route("/cerrar_sesion")
def cerrar_sesion():
    session.pop("s_usuario", None)
    return redirect(url_for("inicio"))

@app_web.route("/registrar")
def registro():
    return render_template("registro.html")


@app_web.route("/consultar")
def consulta():
    datos = postgres_service.get_usuarios()
    return render_template("consulta.html", lista=datos)

@app_web.route("/registrar", methods=["POST"])
def datos():
    lista = []
    if request.method == "POST":
        insert_usuario(4, request.form["nombre"], request.form["apellidos"], request.form["campus"], request.form["area"], request.form["email"], request.form["password"], 1)
        datos = postgres_service.get_usuarios()
        return render_template("datos_registro.html", lista=datos)

@app_web.route("/rdispositivo")
def registrar_dispositivo():
    return render_template("rdispositivo.html")

@app_web.route("/consultard")
def consultad():
    datos1 = postgres_service.get_dispositivos()
    return render_template("consultad.html", lista1=datos1)

@app_web.route("/rdispositivo", methods=["POST"])
def datos_dispositivo():
    lista1 = []
    if request.method == 'POST':
        #id_dispositivo, tipo, marca, mac, antivirus, f_caducidad, id_usuario
        insert_dispositivo(request.form["serie"], request.form["tipod"], request.form["marca"], request.form["mac"], request.form["antivirus"], request.form["caducidad"], 4, request.form["modelo"])
        datos1 = postgres_service.get_dispositivos()
        return render_template("consultad.html", lista=datos1)

if __name__ == '__main__':
    app_web.run(host='0.0.0.0', port='3000', debug=True)


