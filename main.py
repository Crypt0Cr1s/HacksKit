from classes.scriptNmap import nmapaut
from classes.HtmlParser2 import BurpEParser
from classes.scriptssl import ssl
from classes.headers import scanheaders
from classes.downloader import downloader
from classes.accesosV import accesovalidar
from classes.recon import recon

ifmenu = True
while ifmenu == True:
    print("------------------------------------------------")
    print("Hola gracias por utilizar el Toolkit de Crypt0Cr1s")
    print("Se cuenta con las siguientes herramientas:")
    print("1.Automatizador NMAP")
    print("2.Parser Burp Enterprise")
    print("3.Ejecutar Script SSL")
    print("4.Escanear headers")
    print("5.Validador de acceso")
    print("6.Reconocimiento")
    print("7.Salir")

    opcion = int(input("Ingrese la opcion deseada: "))

    if opcion == 1:
        print("------------------------------------------------")
        print("Se ha iniciado el modulo de: Automatizador NMAP")
        archivo=input("Ingresa el nombre del archivo con el listado de sitios a revisar: ")
        rutaout=input("Ingresa la ruta absoluta donde se desea que se generen los resultados: ")
        flags=input("Ingresa los flags que deseas utilizar en NMAP: ")
        nmapaut.nmapaut(archivo,rutaout,flags)
    elif opcion == 2:
        print("------------------------------------------------")
        print("Se ha iniciado el modulo de: Parser Burp Enterprise")
        namefile = input("Ingresa el listado de archivos como 'archivo1.html,achivo2.html': ")
        BurpEParser.parser(namefile)
    elif opcion == 3:
        print("------------------------------------------------")
        print("Se ha iniciado el modulo de: Ejecutar Script SSL")
        archivo=input("Ingresa el nombre del archivo con el listado de sitios a revisar: ")
        rutaout=input("Ingresa la ruta absoluta donde se desea que se generen los resultados: ")
        ssl.scaner(archivo,rutaout)
    elif opcion == 4:
        print("------------------------------------------------")
        print("Se ha iniciado el modulo de: Escanear headers")
        archivo=input("Ingrese el nombre del archivo con el listado de sitios a revisar: ")
        rutaout=input("Ingrese el nombre del archivo de salida: ")
        correlativo = input("Ingrese su correlativo: ")
        scanheaders.scaner(archivo,rutaout,correlativo)
    elif opcion == 5:
        print("------------------------------------------------")
        print("Se ha iniciado el modulo de: Validador Acceso")
        archivo=input("Ingrese el nombre del archivo con el listado de sitios a revisar: ")
        rutaout=input("Ingrese el nombre del archivo de salida: ")
        accesovalidar.validador(archivo,rutaout)
    elif opcion == 6:
        print("------------------------------------------------")
        print("Se ha iniciado el modulo de: Reconocimiento")
        archivo=input("Ingrese el nombre del archivo con el listado de sitios a revisar: ")
        rutaout=input("Ingresa la ruta absoluta donde se desea que se generen los resultados: ")
        recon.recon(archivo,rutaout)
    elif opcion == 7:
        print("------------------------------------------------")
        print("Saliendo...")
        print("Gracias por usar este toolkit")
        ifmenu = False
    else:
        print("------------------------------------------------")
        print("Error!!")

