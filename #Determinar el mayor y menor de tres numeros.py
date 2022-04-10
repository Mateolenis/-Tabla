#Determinar el mayor y menor de tres numeros

n1 = int(input("ingrese el primer numero:"))
n2 = int(input("ingrese el segundo mumero:"))
n3 = int(input("ingrese el tercer numero:"))

if n2 < n1 > n3: 
    print("el numero mayor es el primer numero:",n1)
elif n1 < n2 > n3:
    print("el numero mayor es el segundo numero:",n2)
elif n1 < n3 > n2:
    print("el numero mayor es el tercer numero:",n3)


if n2 > n1 < n3: 
    print("el numero menor es el primer numero:",n1)
elif n1 > n2 < n3:
    print("el numero menor es el segundo numero:",n2)
elif n1 > n3 < n2:
    print("el numero menor es el tercer numero:",n3)
    