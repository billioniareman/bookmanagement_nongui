import mysql.connector as sql


def database_create():
    db = sql.connect(host="localhost",
                     user="root",
                     password="ayush")
    myc = db.cursor()
    myc.execute("CREATE DATABASE book")
    return "created database"


def connect_with_database():
    db = sql.connect(host="localhost",
                     user="root",
                     password="ayush",
                     database="book")
    a = db.is_connected()
    if a == True:
        return "connection done"
    else:
        return "error in connection setting"
