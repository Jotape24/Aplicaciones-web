import pymysql
import json

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
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
	contacto_id = cursor.lastrowid
	conn.commit()
	return contacto_id

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
	conn.commit()
	dispositivo_id = cursor.lastrowid
	return dispositivo_id

def obtener_dispositivos_con_contacto(contacto_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_dispositivos_con_contacto"], (contacto_id,))
	dispositivos = cursor.fetchall()
	conn.commit()
	return dispositivos

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

def obtener_dispositivos_con_comuna( ):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_dispositivos_con_comuna"], ( ))
	conn.commit()
	confessions = cursor.fetchall()
	return confessions

def insertar_archivo(ruta_archivo, nombre_archivo, dispositivo_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_archivo"], (ruta_archivo, nombre_archivo, dispositivo_id,))
	conn.commit()
	user_img = cursor.fetchone()
	return user_img

def obtener_archivos(dispositivo_id ):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_archivos"], (dispositivo_id, ))
	archivos = cursor.fetchall()
	conn.commit()
	return archivos

def obtener_comuna_por_nombre(nombre):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_comuna_por_nombre"], (nombre,))
	comuna = cursor.fetchone()
	return comuna

def obtener_regiones():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_regiones"], ())
	regiones = cursor.fetchall()
	print(regiones)
	return regiones


def obtener_comunas_por_region(region_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["obtener_comunas_por_region"], (region_id,))
    comunas = cursor.fetchall()
    return [{"id": comuna[0], "nombre": comuna[1]} for comuna in comunas]

def obtener_comuna_por_contacto(contacto_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_comuna_por_contacto"], (contacto_id,))
	comuna = cursor.fetchone()
	conn.commit()
	return comuna

def obtener_fotos_por_dispositivo(dispositivo_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_fotos_por_dispositivo"], (dispositivo_id,))
	fotos = cursor.fetchall()
	conn.commit()
	return fotos

def obtener_dispositivos_paginados(offset, limit=5):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["obtener_dispositivos_con_paginacion"], (limit, offset))
    dispositivos = cursor.fetchall()
    conn.commit()
    return dispositivos


def obtener_donante_por_dispositivo(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["obtener_donante_por_dispositivo"], (id,))
    dispositivos = cursor.fetchone()
    conn.commit()
    return dispositivos




def obtener_dispositivo_por_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["obtener_dispositivo_por_id"], (id,))
    dispositivos = cursor.fetchone()
    conn.commit()
    return dispositivos

def obtener_comuna_por_id(comuna_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["obtener_comunas_por_id"], (comuna_id,))
    comuna = cursor.fetchone()
    return comuna[0] if comuna else None

def obtener_region_por_comuna_id(comuna_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(QUERY_DICT["obtener_regiones_id_comunas"], (comuna_id,))
    region = cursor.fetchone()
    return region[0] if region else None


def obtener_comentario(dispositivo_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_comentario"], (dispositivo_id,))
	comentarios = cursor.fetchall()
	return comentarios

def insertar_comentario(nombre, texto, fecha, dispositivo_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_comentario"], (nombre, texto, fecha, dispositivo_id,))
	comentario_id = cursor.lastrowid
	conn.commit()
	return comentario_id

def comuna_y_cantidad():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["comuna_y_cantidad"], ())
	resultados = cursor.fetchall()
	data = []
	for resultado in resultados:
		data.append({"comuna": resultado[0], "cantidad_contactos": resultado[1]})
	return data


def tipos_y_cantidad():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["tipos_y_cantidad"], ())
	resultados = cursor.fetchall()
	data = []
	for resultado in resultados:
		data.append({"tipo": resultado[0], "cantidad_dispositivos": resultado[1]})
	return data
