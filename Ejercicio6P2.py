# Ejercicio 6
# 1. Toma el texto "Su nombre".
# 2. Aplica el método de normalización fuerte (casefold) para prepararlo para una comparación ignorando mayúsculas.
# 3. Verifica si el texto resultante está compuesto únicamente por caracteres alfabéticos (letras) devolviendo un valor booleano.
texto6 = "Su nombre"
texto_normalizado = texto6.casefold()
es_alfabetico = texto_normalizado.replace(" ", "").isalpha()
print(f"Ejercicio: Normalizado: {texto_normalizado}, ¿Es alfabético?: {es_alfabetico}")
