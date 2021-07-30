import sqlite3
idpass=sqlite3.connect("idpass.db")
curidpass=sqlite3.connect("idpass.db")
curidpass=idpass.cursor()
curidpass.execute("INSERT INTO idpass (fname , [lname ] , password) VALUES ('vaibhav','sharma',1816110232);")
idpass.commit()
