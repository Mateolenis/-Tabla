#Factorial de un numero

N = int(input("Ingrese un numero:"))
def factorial(N):
    if (N==0):
        return 1 
    
    else:
        return N * factorial(N-1)
print("El factorial de " + str(N) + " es: " + str(factorial(N)))

