def ingresarnum1():
    num1 = int(input("ingresa el numero: "))
    
    
    return num1

def ingresarnum2():
    
    num2= int(input("Ingresa el numero 2: "))
    
    return num2






def suma(num1,num2):return num1 + num2 

def resta(num1,num2):return num1-num2

def div(num1,num2):return num1/num2

def mult(num1,num2):return num1*num2

print("Calculadora\n")

print("""
  Igresa la opcion deseada 
  1:Suma
  2:Resta
  3:MUltiplicacion
  4:Division    
      
      """)
    


opcion = int(input("Ingresa la opcion: "))


if (opcion == 1): 
    
    num1 = ingresarnum1()
    num2 = ingresarnum2()
    print(suma(num1, num2))
    
if (opcion == 2): 
    num1 = ingresarnum1()
    num2 = ingresarnum2()
    print(resta(num1, num2))

if (opcion == 3): 
    num1 = ingresarnum1()
    num2 = ingresarnum2()
    print(mult(num1, num2))
    
if (opcion == 4): 
    num1 = ingresarnum1()
    num2 = ingresarnum2()
    print(div(num1,num2))
    
    
