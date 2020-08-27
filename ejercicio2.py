import math
n = int(input("digite un numero==>"))

def esPrimo(n):
    contador = 0
    resultado = True
    
    for i in range(1, int(math.sqrt(n))+1):
        if (n%i == 0):
            contador += 1
        if (contador > 2):
            resultado = False
            break
    return resultado
if (esPrimo(n) == True):
        print("es==>" + str(n) + "= un numero primo")
else: 
        print("el numero==>" + str(n) + "=no es un numero primo ")
         
