#Determinar si un numero es primo, par e impar

N1 = int(input("Ingrese un numero: "))

if N1%2==0:
    print("El numero ",N1," es un numero par")
else:
    print("El numero ",N1, " es un numero impar")


if N1 > 1:
    cont=0
    for i in range(2,N1):
        resto=N1%i
        #print("{} % {} = {}".format(N1,i,resto))
        if resto==0:
            cont+=1
    if cont==0:
        print("El numero ",N1," es un numero primo".format(N1))

   













    

    
    