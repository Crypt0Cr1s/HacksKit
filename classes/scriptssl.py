import subprocess
from progress.bar import IncrementalBar
from classes.utilities import utilities

class ssl:
	def scaner(archivo,rutaout):
		
		sitios = utilities.Lfiles(archivo)

		bar = IncrementalBar('Revisando Sitios:', max = len(sitios))


		for r in sitios:
			bar.next()
			ssl = subprocess.getoutput("./ssl.sh"+" "+r)
			outf = open(rutaout + r + ".txt", "w")
			outf.write(ssl)
			outf.close()
			print("\nSe ha creado el archivo: " + r + ".txt en la ruta: " + rutaout)
			
		bar.finish()
