import subprocess
import os
from progress.bar import IncrementalBar

class downloader:
	def downloader(n,url1,url2):
		n = int(input("Ingrese la cantidad de archivos a descargar: "))
		i = 1
		url1 = input("Ingrese la primera parte de la URL (Antes del parametro que cambia): ")
		url2 = input("Ingrese la segunda parte de la URL (Despues del parametro que cambia): ")

		bar = IncrementalBar('Descargando:', max = n)

		while i <= n:
			bar.next()
			subprocess.getoutput("wget " + url1 + str(i) + url2)
			os.rename(r''+str(i)+url2,r''+str(i)+'.jpg')
			i += 1
