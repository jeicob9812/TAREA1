n = int(input("Ingrese un numero==> "))

def perfecto(n):
    s = 0
    
    
    for i in range(1, n):
        if n%i==0:
            s += i
    return s == n
if (perfecto(n)==True):
    print("[" + str(n) + "]es perfecto")
else:
    print("[" + str(n) + "] no es perfecto")
    
