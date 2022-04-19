import subprocess
from classes.utilities import utilities

class nmapaut:
	def nmapaut(archivo,rutaout,flags):
		sitios = utilities.Lfiles(archivo)
		c = 1
		for r in sitios:
			print("\nVamos por la IP: " + str(c) + " de: " + str(len(sitios)))
			ssl = subprocess.getoutput("sudo nmap "+ flags +" "+r)
			outf = open(rutaout + r + ".txt", "w")
			outf.write(ssl)
			outf.close()
			print("\nSe ha creado el archivo: " + r + ".txt en la ruta: " + rutaout)
			c += 1

