import sqlite3
bookstore=sqlite3.connect("bookstore.db")
curstore=sqlite3.connect("bookstore.db")
curstore=bookstore.cursor()
curstore.execute("INSERT INTO books (title , author , price ) VALUES ('think python','allen b drowney',450);")
curstore.execute("INSERT INTO books (title , author , price ) VALUES ('harry potter','j k rowling',650);")
curstore.execute("INSERT INTO books (title , author , price ) VALUES ('julius caesar','williams shakespeare',850);")
curstore.execute("INSERT INTO books (title , author , price ) VALUES ('alice in wonderland','lewis caroll',550);")
bookstore.commit()

