def transformar_con_validacion(texto, opcion):
    if opcion not in [1, 2, 3]:
        return "Opción inválida"
    return "transformar_texto"(texto, opcion)
