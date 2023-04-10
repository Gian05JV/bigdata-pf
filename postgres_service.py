from models import db, Usuarios, Roles, Dispositivos

def insert_usuario(id_usuario, nombre, apellidos, campus, area, email, password, id_rol):
    usuario = Usuarios(id_usuario, nombre, apellidos, campus, area, email, password, id_rol)
    db.session.add(usuario)
    db.session.commit()

def insert_dispositivo(id_dispositivo, tipo, marca, mac, antivirus, f_caducidad, id_usuario, modelo):
    dispositivo = Dispositivos(id_dispositivo, tipo, marca, mac, antivirus, f_caducidad, id_usuario, modelo)
    db.session.add(dispositivo)
    db.session.commit()

def delete_usuario(id_usuario):
    usuario = Usuarios.query.filter_by(id=id).first()
    db.session.delete(usuario)
    db.session.commit()

def get_usuarios():
    usuario = Usuarios.query.all()
    return usuario

def get_dispositivos():
    dispositivo = Dispositivos.query.all()
    #user = Usuarios.query.filter_by(id_usuario=id_usuario, nombre=nombre)
    db.session.commit()
    return dispositivo

def get_dispositivo():
    dispositivo = Dispositivos.query.filter_by(id=id).first()
    db.session.commit()
    return dispositivo

def get_usuario(id_usuario):
    usuario = Usuarios.query.filter_by(id_usuario=id_usuario).first()
    return usuario

def get_acceso(correo, passw, campus):
    usuario = Usuarios.query.filter_by(email=correo, password=passw, campus=campus).first()
    return usuario