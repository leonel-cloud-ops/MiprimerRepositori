Algoritmo SumaContinua
	Definir num,suma Como Real
	suma <- 0
	Repetir
		Escribir "Ingrese un numero: "
		Leer num
		
		Si num >= 0 Entonces
			suma <- suma + num
		FinSi
	Hasta Que num < 0
	Escribir "La suma de los numeros positivos es: ", suma 
	
FinAlgoritmo
