#Determinar con tres notas de 30%, 30% y 40% si aprobo o reprobo

def Calcularnota(Nota1,Nota2,Nota3):
    return (Nota1*0.3) + (Nota2*0.3) + (Nota3*0.4)

Nota1 = float(input("ingrese la primera nota:"))
Nota2 = float(input("ingrese la segunda nota:"))
Nota3 = float(input("ingrese la tercera nota:"))

Notafinal = Calcularnota (Nota1, Nota2, Nota3)

if(Notafinal>=3):
    print("su Nota es:",round(Notafinal,2)," Felicidades, Aprobo")
else:
    print("su Nota es:",round(Notafinal,2)," lo siento, Reprobo")
    
