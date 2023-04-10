# pip install Flask-SQLAlchemy
# pip install psycopg2
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    def __init__(self, id_usuario, nombre, apellidos, campus, area, email, password, id_rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.campus = campus
        self.area = area
        self.email = email
        self.password = password
        self.id_rol = id_rol

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Text, nullable=False)
    apellidos = db.Column(db.Text, nullable=False)
    campus = db.Column(db.Text, nullable=True)
    area = db.Column(db.Text, nullable=True)
    email = db.Column(db.Text, nullable=True)
    password = db.Column(db.Text, nullable=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id_rol'))

class Roles(db.Model):
    __tablename__ = 'roles'

    def __init__(self, id_rol, nombre):
        self.id_rol = id_rol
        self.nombre_rol = nombre

    id_rol = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Text, nullable=True)
    usuario = db.relationship('Usuarios', backref='usuario', lazy=True)

class Dispositivos(db.Model):
    __tablename__ = 'dispositivos'

    def __init__(self, id_dispositivo, tipo, marca, mac, antivirus, f_caducidad, id_usuario, modelo):
        self.id_dispositivo = id_dispositivo
        self.tipo = tipo
        self.marca = marca
        self.mac = mac
        self.antivirus = antivirus
        self.f_caducidad = f_caducidad
        self.id_usuario = id_usuario
        self.modelo = modelo

    id_dispositivo = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Text, nullable=True)
    marca = db.Column(db.Text, nullable=True)
    mac = db.Column(db.Integer, nullable=True)
    antivirus = db.Column(db.Text, nullable=True)
    f_caducidad = db.Column(db.Date, nullable=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario'))
    modelo = db.Column(db.Text, nullable=True)