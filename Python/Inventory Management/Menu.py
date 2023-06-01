from Clase_Inventario import *
from os import system

inventario = Inventario() #Aqui creamos el invetario

while True:

    try:
        system("cls") #Menu donde el usuario indica la operacion que quiera hacer
        print("|------------------------- Menu -------------------------|")
        print("1. Consultar un articulo")
        print("2. Registrar nuevo articulo")
        print("3. Comprar articulos al proveedor")
        print("4. Venta de articulos")
        print("5. Mostrar lista de articulos disponibles")
        print("6. Mostrar lista de articulos comprados en el 2022")
        print("7. Modificar un articulo")
        print("8. Eliminar un articulo")
        print("9. Salir del programa")
        opc = int(input("Ingrese su opcion: "))
        
        #Aqui se llaman los metodos segun la opcion del usuario
        if opc ==  1:
            system("cls")
            inventario.consultarArticulo()
            system("pause")
        elif opc ==  2:
            system("cls")
            inventario.registrarArticulo()
            system("pause")
        elif opc ==  3:
            system("cls")
            inventario.comprarArticulos()
            system("pause")
        elif opc ==  4:
            system("cls")
            inventario.venderArticulos()
            system("pause")
        elif opc ==  5:
            system("cls")
            inventario.mostrarArticulosDisponibles()
            system("pause")
        elif opc ==  6:
            system("cls")
            inventario.mostrarArticulosCompradosAntes()
            system("pause")
        elif opc == 7:
            system("cls")
            inventario.modificarArticulo()
            system("pause")
        elif opc == 8:
            system("cls")
            inventario.eliminarArticulo()
            system("pause")
        elif opc == 9:
            system("cls")
            print("Gracias por usar el programa")
            break
        else:
            system("cls")
            print("La opción ingresada es inválida, intente nuevamente\n")
            system("pause")        
    except ValueError:
        system("cls")
        print("Solo se permiten valores numéricos\n")
        system("pause") 