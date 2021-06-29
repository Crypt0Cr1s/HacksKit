import subprocess
from classes.utilities import utilities

class accesovalidar:
    def validador(archivo,rutaout):
        rutaout = rutaout
        sitios = utilities.Lfiles(archivo)
        c = 1
        outf = open(rutaout + ".txt", "w")
        for r in sitios:
            print("\nVamos por la IP: " + str(c) + " de: " + str(len(sitios)))
            validador = subprocess.getoutput("ping " + r + "-n 1")
            if validador.__contains__("Respuesta desde"):
                outf.write("Respondio la IP: " + r)
            c += 1
        print("\nSe ha creado el archivo: " + rutaout + ".txt")
        outf.close()