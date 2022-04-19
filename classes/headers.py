import subprocess
import csv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from classes.utilities import utilities
import os

class scanheaders:
	def scaner(archivo,rutaout,correlativo,posicion):

		try:
			os.mkdir(rutaout + "Evidencias")
		except OSError as error:
			print("Se intento crear carpeta evidencias pero esta ya existe.")
		
		
		nombre = "headers.csv"
		sitios = utilities.Lfiles(archivo)
		columnas = ("Nombre del Sitio","strict-transport-security","content-security-policy","x-frame-options","x-content-type-options","referrer-policy","permissions-policy","Evidencia")
		pwd = subprocess.getoutput("pwd")
		pwd = pwd + "/classes/"
		with open(rutaout + nombre, 'w', newline='') as csvfile:
			csvwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			resultado = []
			csvwriter.writerow(columnas)
			c = 1
			for r in sitios:
				resultado.append(r)
				print("\nVamos por el sitio: " + str(c) + " de: " + str(len(sitios)))
				headers = subprocess.getoutput("nmap -p443 --script http-security-headers"+" "+ r).lower()
				if headers.__contains__("hsts not configured in https server"):
					resultado.append("False.")
				else:
					resultado.append("True")
				if headers.__contains__("content-security-policy"):
					resultado.append("True")
				else:
					resultado.append("False")
				if headers.__contains__("x-frame-options"):
					resultado.append("True")
				else:
					resultado.append("False")
				if headers.__contains__("x-content-type-options"):
					resultado.append("True")
				else:
					resultado.append("False")
				if headers.__contains__("referrer-policy"):
					resultado.append("True")
				else:
					resultado.append("False")
				if headers.__contains__("permissions-policy"):
					resultado.append("True")
				else:
					resultado.append("False")

				resultado.append(correlativo + "-" + str(posicion) + '.png')
				font = ImageFont.truetype(pwd + 'Roboto-Bold.ttf', 20)
				img = Image.new('RGB', (3000, 800))
				d = ImageDraw.Draw(img)
				d.text((20, 20), "Sitio: "+ r + "\n" + headers, fill=(255, 255, 255),font=font)
				img.save(rutaout +"Evidencias/"+ correlativo + "-" + str(posicion) + '.png','png')
				csvwriter.writerow(resultado)
				resultado = []
				posicion += 1
				c += 1
			print("Se ha creado el archivo: " + nombre + " en la ruta: " + rutaout)