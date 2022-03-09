import mysql.connector as sql
import userconnector

password = "ayush"
if userconnector.connect_with_database():
    db = sql.connect(host="localhost",
                     user="root",
                     password="ayush",
                     database="book")
    myc = db.cursor()


    def insertion():
        book_name = input("enter book name : ")
        author_name = input("enter author of the book : ")
        price_book = int(input("enter the price of book : "))
        sq = "insert into all_Books(NAME,AUTHOR,PRICE) values(%s,%s,%s)"
        val = (book_name, author_name, price_book)
        myc.execute(sq, val)
        db.commit()


    def deletion():
        print("for security reasons:\nEnter password of your database server")
        passwd = input()
        if password == passwd:
            book_name = input("enter book name to delete : ")
            myc.execute("select * from all_Books")
            row = myc.fetchall()
            for i in row:
                if i[0] == book_name:
                    query = "delete from all_Books where NAME='{}'".format(book_name)
                    myc.execute(query)
                    db.commit()
                else:
                    continue
        else:
            print("enter correct password")


    def updation():
        print("for security reasons:\nEnter password of your database server")
        passwd = input()
        if password == passwd:
            print("we cannot update whole entity \n only price can update ")
            book_name = input("enter book name to update the price : ")
            price = int(input("enter updated price : "))
            myc.execute("select * from all_Books")
            row = myc.fetchall()
            for i in row:
                if i[0] == book_name:
                    query = "UPDATE all_Books SET PRICE ={} WHERE NAME ='{}'".format(price, book_name)
                    myc.execute(query)
                    db.commit()
                else:
                    continue
        else:
            print("enter correct password")


    def seeall():
        db = sql.connect(host="localhost",
                         user="root",
                         password="ayush",
                         database="book")
        myc = db.cursor()
        myc.execute("select * from all_Books")
        row = myc.fetchall()
        for i in row:
            print(i)
