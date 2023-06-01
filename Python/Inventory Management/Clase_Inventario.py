from Clase_Articulo import Articulo #Importamos la clase articulo del archivo Clase_Articulo
from io import open #Importamos el metodo open para manipular los archivos
import pickle # Metodo binario para cargar los articulos desde otro archivo

class Inventario:

    lista_articulos = []  #Lista donde se guardan los articulos

    #Constructor de la clase inventario binario, donde se crea y cargan los articulos del archiv externo
    def __init__(self): 
        
        articulos = open("ARTICULOS","ab+")
        articulos.seek(0)

        try:
            self.lista_articulos = pickle.load(articulos) 
        except EOFError:
            pass
        finally:
            articulos.close()


    #Metodo que guarda los datos en los archivos
    def guardarDatos(self): 
        articulos = open("ARTICULOS", "wb")
        pickle.dump(self.lista_articulos, articulos)
        articulos.close()

        archivo = open("ARTICULOS.txt", "w")
        for i in range(len(self.lista_articulos)):
            archivo.write(f"{self.lista_articulos[i].codigo} - {self.lista_articulos[i].nombre} - {self.lista_articulos[i].marca} - {self.lista_articulos[i].cantidad} - {self.lista_articulos[i].precio}$ - {self.lista_articulos[i].fecha} \n")
        archivo.close()

    #Metodo consultar, aqui se ingresa el codigo y busca dentro del archivo el codigo similar
    #y si lo encuentra lo imprime en pantalla
    def consultarArticulo(self): 
        if len(self.lista_articulos) > 0:
            print("|-------------------- CONSULTAR UN ARTICULO --------------------|\n")
            
            encontrado = False

            try:
                codigo = int(input("Indique el codigo del producto a mostrar: "))
                codigo = str(codigo)

                for i in range(len(self.lista_articulos)):
                    if codigo == self.lista_articulos[i].codigo:
                        encontrado = True
                        print(f"\n{self.lista_articulos[i].codigo} - {self.lista_articulos[i].nombre} - {self.lista_articulos[i].marca} - {self.lista_articulos[i].cantidad} - {self.lista_articulos[i].precio} - {self.lista_articulos[i].fecha} \n")
                        break

                if not encontrado: 
                    print("\nEl articulo no está registrado\n")
            except ValueError:
                print("\nSolo se permiten valores numéricos en este campo\n")
        else:
            print("\nNo hay articulos registrados\n")

    #Metodo para registrar articulos en los archivos, si el código del archivo que se va a registrar
    #no está en el archivo se completa la operación
    def registrarArticulo(self):
        print("|-------------------- REGISTRAR UN ARTICULO --------------------|\n")
        encontrado = False

        try:
            codigo = int(input("Ingrese el codigo: "))
            codigo = str(codigo)

            for i in range(len(self.lista_articulos)):
                if codigo == self.lista_articulos[i].codigo:
                    encontrado = True
                    print("\nEste código ya está asignado a un producto")
                    break

            if not encontrado:
                nombre = input("Ingrese el nombre: ")
                marca = input("Ingrese la marca: ")
                cantidad = int((input("Ingrese la cantidad en existensia: ")))
                precio = float((input("Ingrese el precio: ")))
                fecha = input("Ingrese la fecha de entrada: ")

                cantidad = str(cantidad)
                precio = str(precio)
                articulo = Articulo(codigo, nombre, marca, cantidad, precio, fecha)
                self.lista_articulos.append(articulo) 

                self.guardarDatos()
        except ValueError:
            print("\nSolo se permiten valores numéricos en este campo\n")
            
    #Metodo Comprar articulo al proveedor
    def comprarArticulos(self):
        if len(self.lista_articulos) > 0:
            pass
        else:
            print("\nNo hay articulos registrados\n")

    #Metodo Vender articulos
    def venderArticulos(self):
        if len(self.lista_articulos) > 0:
            try:
                codigo = int(input("Ingrese el código del articulo a vender: "))
                codigo = str(codigo)

                for i in range(len(self.lista_articulos)):
                    if codigo == self.lista_articulos[i].codigo:
                        encontrado = True
                        pos = i
                        break

                if encontrado:
                    cant = int(input("Qué cantidad venderá?: "))
                    self.lista_articulos[pos].cantidad = int(self.lista_articulos[pos].cantidad)

                    if cant < self.lista_articulos[pos].cantidad:
                        self.lista_articulos[pos].cantidad - cant
                        self.lista_articulos[pos].cantidad = str(self.lista_articulos[pos].cantidad)
                        
                        articulos = open("ARTICULOS", "wb")
                        pickle.dump(self.lista_articulos, articulos)
                        articulos.close()

                        archivo = open("ARTICULOS.txt", "w")
                        for i in range(len(self.lista_articulos)):
                            archivo.write(f"{self.lista_articulos[i].codigo} - {self.lista_articulos[i].nombre} - {self.lista_articulos[i].marca} - {self.lista_articulos[i].cantidad} - {self.lista_articulos[i].precio} - {self.lista_articulos[i].fecha} \n")
                        archivo.close()
                        print("\nOperación exitosa\n")
                    else:
                        print("\nNo hay la cantidad suficiente de este articulo para vender\n")
                else:
                    print("\nEl articulo no está registrado\n")
            except ValueError:
                print("\nSolo se permiten valores numéricos es este campo\n")
        else:
            print("\nNo hay articulos registrados\n")

        #archivo = open("ARTICULOS.txt", "w")
        #for i in range(len(self.lista_articulos)):
            #archivo.write(f"{self.lista_articulos[i].codigo} - {self.lista_articulos[i].nombre} - {self.lista_articulos[i].marca} - {self.lista_articulos[i].cantidad} - {self.lista_articulos[i].precio} - {self.lista_articulos[i].fecha} \n")
        #archivo.close()

    #Metodo para mostrar los artiuclos disponibles dentro del archivo
    #Si articulo no esta eliminado lo mostrará
    def mostrarArticulosDisponibles(self):
        if len(self.lista_articulos) > 0:
            print("|-------------------- ARTICULOS DISPONIBLES --------------------|\n")

            encontrado = False
            with open("ARTICULOS.txt", "r") as archivo:
                    for i, linea in enumerate(archivo,1):
                        if "*" not in linea:
                            encontrado = True
                            print(linea)
            if not encontrado:
                print("\nNo hay articulos disponibles")
        else:
            print("\nNo hay articulos registrados\n")
        
    #Metodo mostrrar articulos adquiridos en el año 2022, busca en todo el archivo
    #comparando las fechas, si encuentra similitud con los articulos en el archivo
    # este mostrará los articulos adquiridos en el 2022
    def mostrarArticulosCompradosAntes(self):
        if len(self.lista_articulos) > 0:
            print("|-------------------- ARTICULOS COMPRADOS EL 2022 --------------------|\n")

            fecha = "2022"
            encontrado = False
            with open("ARTICULOS.txt", "r") as archivo:
                for i, linea in enumerate(archivo,1):
                    if fecha  in linea and "*" not in linea:
                        encontrado = True
                        print(linea)
            if not encontrado:
                print("\nNo hay articulos registrados del 2022\n")
        else:
            print("\nNo hay articulos registrados\n")

    #Metodo para modificar un articulo existente
    def modificarArticulo(self):
        if len(self.lista_articulos) > 0:
            print("|-------------------- MODIFICAR UN ARTICULO --------------------|\n")

            encontrado = False

            try:
                codigo = int(input("Ingrese el código del articulo a modificar: "))
                codigo = str(codigo)

                for i in range(len(self.lista_articulos)):
                    if codigo == self.lista_articulos[i].codigo:
                        self.lista_articulos[i].codigo = "* " + self.lista_articulos[i].codigo
                if not encontrado:
                    print("\nEl articulo no está registrado\n")
            except ValueError:
                print("\nSolo se permiten valores numéricos en este campo\n")
        else:
            print("\nNo hay articulos registrados\n")

    #Método donde nuevamente se pide el código, si encuentra alguna similitud con los códigos del archivo
    #este se actualizara colocando un "*" al lado de la referencia del articulo para indicar que no está
    #disponible
    def eliminarArticulo(self):
        if len(self.lista_articulos) > 0:
            print("|-------------------- ELIMINAR UN ARTICULO --------------------|\n")

            encontrado = False

            try:
                codigo = int(input("Ingrese el código del articulo a eliminar: "))
                codigo = str(codigo)

                for i in range(len(self.lista_articulos)):
                    if codigo == self.lista_articulos[i].codigo:
                        encontrado = True
                        self.lista_articulos[i].codigo = "* " + self.lista_articulos[i].codigo

                        self.guardarDatos()
                        break
                
                if not encontrado:
                    print("\nEl articulo no está registrado\n")
            except ValueError:
                print("\nSolo se permiten valores numéricos en este campo\n")
        else:
            print("\nNo hay articulos registrados\n")



