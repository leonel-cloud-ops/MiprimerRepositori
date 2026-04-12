# Ejercicio 4
# 1. Toma la palabra "CANTANDO".
# 2. Convierte toda la cadena a letras minusculas.
# 3. Elimina el sufijo "ando" de la palabra resultante y encuentra en que indice (posicion) quedo la letra "t".
palabra = "CANTANDO"
palabra_min = palabra.lower()
palabra_final = palabra_min.removesuffix("ando")
indice_t = palabra_final.find("t")

print(f"Ejercicio 4: Palabra: {palabra_final}, Índice de 't': {indice_t}")
