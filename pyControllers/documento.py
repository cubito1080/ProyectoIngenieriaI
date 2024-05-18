import random
import string
from dbConnection import connectDB
import os
from werkzeug.utils import secure_filename

def documentosContrato(contratista, auditor):
    connection = connectDB()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT documento FROM documento as d join contratista as c join auditor as a WHERE " 
        "c.cedula=%s and a.cedula=%s ", (contratista["cedula"], auditor["cedula"]))

    documentos = cursor.fetchall()
    cursor.close()
    return documentos


def handleFile(file):
    basepath = os.path.dirname(__file__)
    filename = secure_filename(file.filename)

    extension = os.path.splitext(filename)[1]
    newFileName = stringAleatorio() + extension 

    uploadPath = os.path.join(basepath, 'documentos', newFileName)
    file.save(uploadPath)

    return newFileName


def uploadFile(file, contratista={"cedula": 1011511123}, auditor={"cedula": 1011638823}):
    connection = connectDB()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("INSERT INTO documento(cedula_contratista, cedula_auditor, documento, estado) " 
                        "VALUES (%s, %s, %s, %s)",
                        (contratista["cedula"], auditor["cedula"], file, "en espera"))
    connection.commit()
    cursor.close()

    # resultado_insert = cursor.rowcount #retorna 1 o 0
    # ultimo_id        = cursor.lastrowid #retorna el id del ultimo registro
    return cursor.rowcount





def stringAleatorio():
    return "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))