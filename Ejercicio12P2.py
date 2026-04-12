# Ejercicio 12
# 1. Toma el nombre de archivo "Sunombre.txt".
# 2. Remueve el sufijo ".txt" y posteriormente remueve el prefijo "ING. ".
# 3. Toma el texto que quede limpio, convertido a minúsculas.
archivo = "Leonel.txt"
temp = archivo.removesuffix(".txt")
texto_limpio = temp.removeprefix("ING. ")
resultado = texto_limpio.lower()

print(f"Ejercicio 12: {resultado}")
