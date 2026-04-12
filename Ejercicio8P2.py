# Ejercicio 8
# 1. Define un bloque de texto de 3 lineas usando comillas triples (puedes usar un fragmento del poema de la guia).
# 2. Cuenta cuantas veces aparece la letra "a" en todo el bloque de texto.
# 3. Divide el bloque de texto por sus saltos de linea (splitlines) para convertirlo en una lista de oraciones independientes
poema = """Cultivo una rosa blanca
en junio como en enero
para el amigo sincero"""
conteo_a = poema.count("a")
lista_oraciones = poema.splitlines()
print(f"Ejercicio 8: Letras 'a' encontradas: {conteo_a}")
print(f"Lista de oraciones: {lista_oraciones}")
