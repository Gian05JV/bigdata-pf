from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import monitoreo

app = Flask(__name__)
monitoreo.create_dash(app)
client = MongoClient('mongodb://192.168.0.13:27017/?serverSelectionTimeoutMS=5000')
db = client.dbisesion
users = db.users

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/register")
def regist():
    return render_template("registro.html")

@app.route('/register', methods=['POST'])
def register():
    campus = request.form.get('campus')
    name = request.form.get('nombre')
    apellidos = request.form.get('apellidos')
    email = request.form.get('email')
    password = request.form.get('password')

    users.insert_one({
        'campus': campus,
        'name': name,
        'apellidos': apellidos,
        'email': email,
        'password': password
    })

    return render_template("index.html")



@app.route("/login")
def isesion():
    return render_template("isesion.html")

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    user = users.find_one({'email': email})

    if user and user['password'] == password:
        return redirect(url_for("dash_temp"))
    else:
        return 'Error de inicio de sesión'
    #return redirect(url_for("isesion"))

@app.route("/dash_temp")
def dash_temp():
    return redirect("/dash")


if __name__ == '__main__':
    app.run(debug=True)
