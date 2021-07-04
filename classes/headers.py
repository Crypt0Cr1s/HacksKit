import subprocess
import csv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from classes.utilities import utilities

class scanheaders:
	def scaner(archivo,rutaout,correlativo):
		
		rutaout = rutaout + ".csv"
		sitios = utilities.Lfiles(archivo)
		columnas = ("Nombre del Sitio","strict-transport-security","content-security-policy","x-frame-options","x-content-type-options","referrer-policy","permissions-policy","Evidencia")
		pwd = subprocess.getoutput("pwd")
		pwd = pwd + "/classes/"
		with open(rutaout, 'w', newline='') as csvfile:
			csvwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			resultado = []
			csvwriter.writerow(columnas)
			c = 1
			for r in sitios:
				resultado.append(r)
				print("\nVamos por el sitio: " + str(c) + " de: " + str(len(sitios)))
				headers = subprocess.getoutput("nmap -p443 --script http-security-headers"+" "+ r).lower()
				if headers.__contains__("hsts not configured in https server"):
					resultado.append("Se identifico que en el sitio, no cuenta con la cabecera Strict-Transport-Security. Esta cabecera indica al navegador que el sitio web solo debe de cargarse en HTTPS.")
				else:
					resultado.append("True")
				if headers.__contains__("content-security-policy"):
					resultado.append("True")
				else:
					resultado.append("Se identifico que el sitio, no cuenta con la cabecera Content-Security-Policy. Esta cabecera es una medida efectiva de proteccion del sitio ante ataques XSS.")
				if headers.__contains__("x-frame-options"):
					resultado.append("True")
				else:
					resultado.append("Se identifico que en el sitio, es vulnerable a Clickjacking lo que permite agregarla dentro de un sitio externo controlado por una persona malintencionada, pudiendo engañar asi a los usuarios haciendo uso de practicas de Ingenieria social.")
				if headers.__contains__("x-content-type-options"):
					resultado.append("True")
				else:
					resultado.append("Se identifico que el sitio, no cuenta con la cabecera X-Content-Type-Options. Esta cabecera permite evitar ataques basados en la confusion del tipo de MIME, debido a que si el navegador recibe esta cabecera no intentara interpretar el tipo de MIME en ningun caso y utilizara el indicado en el Content-Type.")
				if headers.__contains__("referrer-policy"):
					resultado.append("True")
				else:
					resultado.append("Se identifico que el sitio, no cuenta con la cabecera Referrer-Policy. Esta cabecera permite controlar que informacion se envia en la cabecera Referer cual es utilizada por el navegador para indicarle al servidor desde que enlace se ha llegado a la pagina.")
				if headers.__contains__("permissions-policy"):
					resultado.append("True")
				else:
					resultado.append("Se identifico que el sitio, no cuenta con la cabecera Permissions-Policy. Esta cabecera permite a un sitio controlar que funciones y API's   se pueden usar en el navegador.")

				resultado.append(correlativo + "-" + str(c) + '.png')
				font = ImageFont.truetype(pwd + 'Roboto-Bold.ttf', 20)
				img = Image.new('RGB', (3000, 800))
				d = ImageDraw.Draw(img)
				d.text((20, 20), "Sitio: "+ r + "\n" + headers, fill=(255, 255, 255),font=font)
				img.save(correlativo + "-" + str(c) + '.png','png')
				csvwriter.writerow(resultado)
				resultado = []
				c += 1
			print("Se ha creado el archivo" + rutaout)