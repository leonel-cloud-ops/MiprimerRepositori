USER_DB = "admin"
PASS_DB = "1234"

usuario = input("Usuario: ")
password = input("Contraseña: ")

if usuario == USER_DB and password == PASS_DB:
    print("Acceso permitido")
else:
    print("Acceso denegado")
