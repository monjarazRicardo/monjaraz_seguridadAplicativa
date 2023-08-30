diccionario = {
	"Juan":8,
	"Giselle":9,
	"Damian":5,
	"Ricardo":6,
	"Yaotzin":6,
	"Erick":7,
    "Mario":8,
    "Edgar":9,
    "Fernanda":5,
    "Daniel":6,
    "Jesus":7,
    "Damian":8,
    "Jesus":7,
    "Damian":8,
    "Yema":6,
    "Eduardo":9,
    "Bryan":9,
    "Mariano":10,
    "Alberto":8
        
}

def promedio(diccionario):
    
    promedio = 0
    suma = 0
    total = len(diccionario)
    for calif in diccionario:
        
        suma += int(diccionario[calif])
    promedio = suma / total
        
    print("El promedio es: ", promedio)
    

def menor(diccionario):
    for calif in diccionario:
        if (int(diccionario[calif] <= 5)):
            
            print(calif)
    
def mayor(diccionario):
    for calif in diccionario:
        if (int(diccionario[calif] ==10)):
            
            print(calif)      
            


        
            
    
    
promedio(diccionario)
menor(diccionario)
mayor(diccionario)
