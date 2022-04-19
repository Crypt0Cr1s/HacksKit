import subprocess
from classes.utilities import utilities

class recon:
	def recon(archivo,rutaout):
		sitios = utilities.Lfiles(archivo)
		c = 1
		for r in sitios:
			print("\nVamos por el segmento: " + str(c) + " de: " + str(len(sitios)))
			ssl = subprocess.getoutput("sudo masscan " + r + " --ping ")
			outf = open(rutaout + r[:len(r)-3] + ".txt", "w")
			outf.write(ssl)
			outf.close()
			print("\nSe ha creado el archivo: " + r[:len(r)-3] + ".txt en la ruta: " + rutaout)
			
			fclean = open(rutaout + r[:len(r)-3] + ".txt", "r")
			fcleaned = open(rutaout + r[:len(r)-3] + "-cleaned.txt", "w")
			lines = fclean.readlines()
			for line in lines:
				if line.__contains__("Discovered open port 0/icmp on "):
					linecleaned = line.replace("Discovered open port 0/icmp on ","")
					fcleaned.write(linecleaned)
			fclean.close()
			fcleaned.close()
			print("\nSe ha creado el archivo: " + r[:len(r)-3] + "-cleaned.txt en la ruta: " + rutaout)

			c += 1

