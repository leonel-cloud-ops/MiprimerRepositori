a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a == b == c:
    print("Es un triángulo Equilátero.")
elif a == b or a == c or b == c:
    print("Es un triángulo Isósceles.")
else:
    print("Es un triángulo Escaleno.")
