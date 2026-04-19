n1 = float(input("Primer número: "))
op = input("Operación (+, -, *, /): ")
n2 = float(input("Segundo número: "))

if op == "+":
    print(f"Resultado: {n1 + n2}")
elif op == "-":
    print(f"Resultado: {n1 - n2}")
elif op == "*":
    print(f"Resultado: {n1 * n2}")
elif op == "/":
    if n2 != 0:
        print(f"Resultado: {n1 / n2}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida.")
