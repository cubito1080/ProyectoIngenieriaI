import random
import string
from dbConnection import connectDB
import os
from werkzeug.utils import secure_filename

def documentosContrato(contrato_id):
    connection = connectDB()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM documento WHERE contrato_id=%s", (contrato_id,))

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

def updateFile(file, documento_id):
    connection = connectDB()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("UPDATE documento SET documento=%s WHERE id=%s", (file, documento_id))
    connection.commit()
    cursor.close()
    return cursor.rowcount


def uploadFile(file, contrato_id):
    connection = connectDB()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("INSERT INTO documento(documento, contrato_id) " 
                        "VALUES (%s, %s)",
                        (file, contrato_id))
    connection.commit()
    cursor.close()
    # resultado_insert = cursor.rowcount #retorna 1 o 0
    # ultimo_id        = cursor.lastrowid #retorna el id del ultimo registro
    return cursor.rowcount




def stringAleatorio():
    return "".join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))