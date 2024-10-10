import pymysql
import json

DB_NAME = "confessions_db"
DB_USERNAME = "dbadmin"
DB_PASSWORD = "dbadmin"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

with open('database/querys.json', 'r') as querys:
	QUERY_DICT = json.load(querys)

# -- conn ---

def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

# -- querys --  podria agregar excepciones si hay errores de conexion

def agregar_contacto(nombre, email, celular, comuna_id, fecha_creacion):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["agregar_contacto"], (nombre, email, celular, comuna_id, fecha_creacion,))
	user = cursor.fetchone()
	return user

def obtener_contactos_ordenados():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_contactos_ordenados"], ())
	user = cursor.fetchone()
	return user

def agregar_dispositivo(contacto_id, nombre, descripcion, tipo, anos_uso, estado):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["agregar_dispositivo"], (contacto_id, nombre, descripcion, tipo, anos_uso, estado,))
	user = cursor.fetchone()
	return user

def obtener_dispositivos_con_contacto(contacto_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_dispositivos_con_contacto"], (contacto_id,))
	conn.commit()

def obtener_primeros_5_disp():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_primeros_5_disp"], ())
	confessions = cursor.fetchall()
	return confessions

def obtener_siguientes():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_siguientes"], ())
	conn.commit()

def no_name( ):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["no_name"], ( ))
	conn.commit()

def insertar_archivo(ruta_archivo, nombre_archivo, dispositivo_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_archivo"], (ruta_archivo, nombre_archivo, dispositivo_id,))
	user_img = cursor.fetchone()
	return user_img

def obtener_archivos(dispositivo_id ):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_archivos"], (dispositivo_id, ))
	conn.commit()
	

# -- db-related functions --

"""""
def register_user(username, password, email):
	# 1. check the email is not in use
	_email_user = get_user_by_email(email)
	if _email_user is not None:
		return False, "El correo ya esta en uso."
	# 2. check the username is not in use
	_username_user = get_user_by_username(username)
	if _username_user is not None:
		return False, "El nombre de usuario esta en uso."
	# 3. create user
	create_user(username, password, email)
	return True, None

def login_user(username, password):
	a_user = get_user_by_username(username)
	if a_user is None or a_user[3] != password:
		return False, "Usuario o contraseña incorrectos."
	return True, None

"""""