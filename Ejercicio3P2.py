# Ejercicio 3
# 1. Crea una variable con el texto "ING. Su nombre".
# 2. Remueve el prefijo "ING. " de la cadena.
# 3. Convierte el texto restante completamente a letras mayusculas.
texto = "ING. Leonel"
texto_sin_prefijo = texto.removeprefix("ING. ")
resultado = texto_sin_prefijo.upper()
print(f"Ejercicio 3: {resultado}")
