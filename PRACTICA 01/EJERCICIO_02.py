'''
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al 
usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no
'''
edad = int(input("Ingresa tu edad: "))
ingresos = int(input("Ingrese sus impuestos: "))


if edad > 16  and ingresos > 1000:
    print("El usuario ya puede tributar")
elif edad >= 16 and ingresos < 1000:
    print("El usuario no tiene suficientes ingresos")
elif edad < 16 and ingresos < 1000:
    print("El usuaio no tiene edad suficiente para tributar")
else:
    print("error")