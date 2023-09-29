def num_primo(n):
    if n < 2: return False
    for i in range (2, int(n/2)+1):
        if n % i == 0: return False
    return True

num_primo(7)

def num_prim_sig(n):
    if not num_primo: return False
    i = 0
    while True:
        i += 1
        if num_primo(n+i): return(n+i)
    
num_prim_sig(4)

def median(datos):
    mitad = len(datos) // 2
    datos.sort()
    return datos[mitad]

lista= [1,3,2]
print(median(lista))

import random
def contra_random():
    contra = ""
    for i in range (1,random.randrange(7,10)):
        contra += chr(random.randrange(33, 126, 1))
    return contra

contra_random()

def hipotenusa(a,b):
    return(a**2+b**2)**.5

hipotenusa(3,4)