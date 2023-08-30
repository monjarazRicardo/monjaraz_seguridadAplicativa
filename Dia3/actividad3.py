a=[8,9,10,6,6,7,8,9,5,6,7,6,8,8,9,9,5,6,7,9,10,7,8,9,9]

def promedio(a):
    
    totalcalif = len(a)
    suma = 0
    for calif in a:
        suma += calif
    promedio = suma / totalcalif
    
    print("promedio: ", promedio)


    
def reprobaron(a):
    
    contador = 0
    for calif in a:
        if calif < 6:
            contador +=1 
     
    print("Reprobaron:", contador )
    
promedio(a)
reprobaron(a)
