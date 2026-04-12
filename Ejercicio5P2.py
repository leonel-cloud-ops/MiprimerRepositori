# Ejercicio 5
# 1. Inicia con la cadena "pYTHON".
# 2. Invierte las mayusculas por minusculas y las minusculas por mayusculas.
# 3. Alinea este nuevo texto hacia la izquierda en un espacio de 15 caracteres, rellenando los espacios vacios con asteriscos ("*").
texto = "pYTHON"
print("invertir mayusculas y minusculas")
texto_invertido = texto.swapcase()
print(texto_invertido)
print("Alinear a la izquierda")
textoFORMATO = texto.split()

for linea in textoFORMATO:
    print(linea.rjust(15, "*"))
resultado = texto_invertido.ljust(15, "*")
