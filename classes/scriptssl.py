import subprocess
from progress.bar import IncrementalBar
from classes.utilities import utilities
from datetime import datetime
import csv
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class ssl:
	def scaner(archivo,rutaout,correlativo):
		nolinea = 0
		c = 1
		pwd = subprocess.getoutput("pwd")
		pwd = pwd + "/classes/"
		comando = "nmap --script ssl-cert,ssl-enum-ciphers -p 443"
		sitios = utilities.Lfiles(archivo)
		bar = IncrementalBar('Escaneando Sitios:', max = len(sitios))

		for r in sitios:
			bar.next()
			ssl = subprocess.getoutput(comando + " " + r).lower()
			outf = open(rutaout + r + ".txt", "w")
			outf.write(ssl)
			outf.close()
			print("\nSe ha creado el archivo: " + r + ".txt en la ruta: " + rutaout)
			
		bar.finish()
		bar2 = IncrementalBar('Generando resultados:', max = len(sitios))
		resultados = []
		imagen = ""
		columnas = ("URL","Issuer","public key type","public key bits","validity","Protocols")
		with open(rutaout + "resultados.csv", 'w', newline='') as csvfile:
			csvwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			csvwriter.writerow(columnas)


			for r in sitios:
				resultados.append(r)
				bar2.next()
				file = open(rutaout + r + ".txt")
				lines = file.readlines()
				while nolinea < 3:
					line = lines[nolinea]
					imagen += line
					nolinea += 1
				while nolinea < len(lines):
					line = lines[nolinea]
					if line.__contains__("issuer"):
						resultados.append(line[21:])
						imagen += "Issuer: " + line[21:] + "\n"
						nolinea += 1
					elif line.__contains__("public key type"):
						resultados.append(line[18:])
						imagen += "Public key type: " + line[18:]
						nolinea += 1
					elif line.__contains__("public key bits"):
						resultados.append(line[18:])
						imagen += "Public key bits: " + line[18:]
						nolinea += 1
					elif line.__contains__("not valid after"):
						line = line[20:]
						line = line.replace("t"," ")
						imagen += "Not valid after: " + line
						line = line.replace("\n","")
						vencimiento = datetime.strptime(line, "%Y-%m-%d %H:%M:%S")
						hoy = datetime.now()
						dias = vencimiento - hoy
						dias = str(dias)
						i = 0
						while dias[i] != " ":
							i += 1
						dias = dias[0:-(len(dias)-i)]
						if int(dias) < 0:
							resultados.append("Se encuentra vencido por: " + dias + " dias")
							nolinea += 1
						else:
							resultados.append("Aun es valido por: " + dias + " dias")
							nolinea += 1
					elif line.__contains__("ssl-enum-ciphers"):
						imagen += "ssl-enum-ciphers: \n"
						bandera = False
						nolinea += 1
						line = lines[nolinea]
						while nolinea < len(lines):
							bandera = False
							line = lines[nolinea]
							if line.__contains__("sslv2:"):
								resultados.append("SSLv2")
								imagen += line
								nolinea += 1
							elif line.__contains__("sslv3:"):
								resultados.append("SSLv3")
								imagen += line
								nolinea += 1
							elif line.__contains__("tlsv1.0:"):
								resultados.append("TLSv1.0")
								imagen += line
								nolinea += 1
							elif line.__contains__("tlsv1.1:"):
								resultados.append("TLSv1.1")
								imagen += line
								nolinea += 1
							elif line.__contains__("tlsv1.2:"):
								resultados.append("TLSv1.2")
								imagen += line
								nolinea += 1
							elif line.__contains__("ciphers:"):
								while bandera == False and nolinea < len(lines):
									line = lines[nolinea]
									if line.__contains__("sslv3:") or line.__contains__("tlsv1.0:") or line.__contains__("tlsv1.1:") or line.__contains__("tlsv1.2:"):
										bandera = True
									else:
										nolinea += 1
							else:
								nolinea += 1
					else:
						nolinea += 1
				resultados.append(correlativo + "-" + str(c) + '.png')
				font = ImageFont.truetype(pwd + 'Roboto-Bold.ttf', 20)
				img = Image.new('RGB', (1000, 400))
				d = ImageDraw.Draw(img)
				d.text((20, 20), "Sitio: "+ r + "\n" + imagen, fill=(255, 255, 255),font=font)
				img.save(rutaout +"Evidencias/"+ correlativo + "-" + str(c) + '.png','png')
				imagen = ""
				csvwriter.writerow(resultados)
				resultados = []
				c += 1
				nolinea = 0
			print("\nSe ha creado el archivo resultados.csv en la ruta: " + rutaout)