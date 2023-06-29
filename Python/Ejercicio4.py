# Dise˜ne un programa que muestre las tablas de multiplicar del 1 al 9.
for i in range(1,11):
    print("Tabla de multiplicar del ",i)
    print("")
    for j in range (1,11):
        resultado=i*j
        print(i," * ",j,"=",resultado)
