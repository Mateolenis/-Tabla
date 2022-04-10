#Deteminar el IMC de un usuario

Peso = float(input("Escriba su peso (Kg):"))
Estatura = float(input("Escriba su estatura (m):"))

IMC = Peso / (Estatura**2)
print("IMC:", round(IMC,2))

if IMC < 18.5:
    print("Bajo peso")
elif 18.5 <= IMC and IMC < 25:
    print("Normal") 
elif  25 <= IMC  and IMC < 30:
    print("Sobre peso")
elif IMC >= 30:
    print("Obesidad")
    