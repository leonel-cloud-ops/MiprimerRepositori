Algoritmo nota
	Definir notas Como Real
	Escribir "Introdusca la nota"
	leer notas
	
	Si notas >= 6 Entonces
		Escribir "La nota es ",notas,"Por lo tanto el estudiante queda aprobado"
	FinSi
	Si notas = 5 Entonces
		Escribir "La nota es ",notas,"Por lo tanto el estudiante queda en recuperacion"
	FinSi
	
	Si notas <=4
		Escribir "La nota es ",notas, "Por lo tanto el estudiante queda reprobado"
	FinSi
	Si notas > 10 Entonces
		Escribir "La nota es ",notas, "Esta nota es invalida"
		
	FinSi
FinAlgoritmo
