monto = float(input("Ingresa el monto de la compra: "))

if monto > 100:
    total = monto * 0.80
    print(f"Descuento del 20%. Total a pagar: ${total}")
elif 50 <= monto <= 100:
    total = monto * 0.90
    print(f"Descuento del 10%. Total a pagar: ${total}")
else:
    print(f"Sin descuento. Total a pagar: ${monto}")
