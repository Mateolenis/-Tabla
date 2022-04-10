#Funcion para suma, resta, multiplicacion y division.

N1 = float(input("Ingrese el primer numero: "))
N2 = float(input("Ingrese el segundo numero: "))

suma = N1 + N2
resta = N1 - N2
multiplicacion = N1 * N2

if N2 == 0:
    print(" La suma es:", suma, "\n La resta es:", resta, "\n La multiplicacion es:",
     multiplicacion, "\n La division : No se puede dividir entre cero" )

else:
    division = N1 / N2
    print(" La suma es:", suma, "\n La resta es:", resta, "\n La multiplicacion es:",
     multiplicacion, "\n La division es:", division)

