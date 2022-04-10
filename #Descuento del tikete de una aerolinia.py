#DDescuento del tikete de una aerolinia

Edad = int(input("Digite la edad del pasajero: "))

if Edad <=5:
    print("No paga el valor del tikete: $0.0")

elif Edad ==18:
    Precio = 300.000
    Descuento = Precio * 0.50
    Precio_final = Precio - Descuento
    print(f"EL precio a pagar del tikete es de: ${Precio_final:.3f}")

else: 
    print("Paga el valor total del tikete: $300.000")
    
