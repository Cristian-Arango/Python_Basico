# 1 Desarrollar un programa que imprima el cuadrado del n´umero que el
# usuario ingresa mientras que el n´umero ingresado no sea negativo.

num=int(input("Ingrese un numero para sacar el cuadrado de este numero, Porfavor no ingrese un numero negativo:  "))

if(num>1):
    cuadrado=num*num
    print("El numero " ,num, " Al cuadrado es ",cuadrado)
else:
    print("No se puede hacer el caLculo debido a que ingreso un numero negativo")

