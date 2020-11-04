

#!/usr/bin/python3
import cgi
import mysql.connector
from mysql.connector import errorcode

datos=cgi.FieldStorage();

print('Content-Type: text/html')
print('<h1>Bienvenido {}</h1>'.format(datos.getvalue('fname')))

nombres=datos.getvalue("Nombres")
apellidos=datos.getvalue("Apellidos")
idempl=datos.getvalue("Id Empleado")
ciudad=datos.getvalue("Ciudad")


try:
	cnx=mysql.connector.connect(user='juandiaz',password='12345',database='db',localhost='127.0.0.1')
	cursor=cnx.cursor()
	sql="INSERT INTO empleados(nombres, apellidos, idempl, ciudad) VALUES (%s,%s,%s,%s)"
	cursor.execute(sql)
	cnx.commit()
	print("<h1>Ingreso exitoso</h1>"
	cursor.close()
	cnx.close()


except mysql.connector.Error as err:
	if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
		print("Usuario o contraseña invalido")
	elif err.errno==errorcode.ER_BAD_DB_ERROR:
		print("La base de datos no existe")
	else: 
		print(err)
else:
	cnx.close()





