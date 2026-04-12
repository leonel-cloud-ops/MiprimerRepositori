def transformacion_multiple(texto, lista_opciones):
    resultado = texto
    for opcion in lista_opciones:
        resultado = "transformar_texto"(resultado, opcion)
    return resultado
