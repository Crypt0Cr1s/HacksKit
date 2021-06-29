from bs4 import BeautifulSoup
import re
import csv

class BurpEParser:
    def parser(namefile):
        listaarchivos = namefile.split(',')
        for n in listaarchivos:
            file = open(namefile)
            lines = file.readlines()
            contador = 0
            resultados = []
            valores = []
            banderaVal = True
            contadorResultados = 0
            cadena = ""
            high = 0
            medium = 0
            low = 0
            information = 0
            while contador < len(lines):
                line = lines[contador]
                if "Issue detail:" in line:
                    contadorResultados = contadorResultados + 1
                    resultados.append(str(contadorResultados))
                    bandera = True
                    numeraciontemp = contador - 3
                    while bandera == True:
                        line = lines[numeraciontemp]
                        if "Issue background" in line:
                            bandera = False
                            cadena = re.sub('<.*?>', '', cadena)
                            resultados.append(cadena)
                            cadena = ""
                        elif (numeraciontemp != contador-1 and numeraciontemp < contador):
                                if "Issue detail:" in line:
                                    numeraciontemp = numeraciontemp + 1
                                else:
                                    if "href" in line:
                                        linea = line[9:]
                                        linea = linea[:len(linea)-8]
                                        resultados.append(linea)
                                        numeraciontemp = numeraciontemp + 1
                                    elif line == "\n":
                                        numeraciontemp = numeraciontemp + 1
                                    else:
                                        linea = re.sub('<.*?>', '', line)
                                        resultados.append(linea)
                                        numeraciontemp = numeraciontemp + 1
                        else:
                            line = re.sub('<.*?>', '', line)
                            if line == "\n":
                                numeraciontemp = numeraciontemp + 1
                            else:
                                if "Issue detail:" in line:
                                    numeraciontemp = numeraciontemp + 1
                                else:
                                    cadena = cadena + line + ". "
                                    numeraciontemp = numeraciontemp + 1
                    contador = numeraciontemp
                elif "Issue background" in line:
                    contador += 1
                    bandera = True
                    while bandera == True:
                        line = lines[contador]
                        line = re.sub('<.*?>', '', line)
                        if "Issue remediation" in line or "References" in line:
                            bandera = False
                            cadena = re.sub('<.*?>', '', cadena)
                            resultados.append(cadena)
                            cadena = ""
                        elif line == "\n":
                            contador = contador + 1
                        else:
                            cadena = cadena + line
                            contador = contador + 1
                elif "Issue remediation" in line:
                    contador += 1
                    bandera = True
                    while bandera == True:
                        line = lines[contador]
                        line = re.sub('<.*?>', '', line)
                        if "Vulnerability classifications" in line or "References" in line:
                            bandera = False
                            cadena = re.sub('<.*?>', '', cadena)
                            resultados.append(cadena)
                            cadena = ""
                        elif line == "\n":
                            contador = contador + 1
                        else:
                            cadena = cadena + line
                            contador = contador + 1
                else:
                    contador += 1

            contador = 0

            while banderaVal == True:
                line = lines[contador]
                if "High" in line:
                    high += 1
                    if high > 1:
                        linea = re.sub('<.*?>', '', line)
                        linea2 = re.sub('<.*?>', '', lines[contador+1])
                        valores.append(linea)
                        valores.append(linea2)
                        contador += 2
                    else:
                        contador += 1
                elif "Medium" in line:
                    medium += 1
                    if medium > 1:
                        linea = re.sub('<.*?>', '', line)
                        linea2 = re.sub('<.*?>', '', lines[contador+1])
                        valores.append(linea)
                        valores.append(linea2)
                        contador += 2
                    else:
                        contador += 1
                elif "Low" in line:
                    low += 1
                    if low > 1:
                        linea = re.sub('<.*?>', '', line)
                        linea2 = re.sub('<.*?>', '', lines[contador+1])
                        valores.append(linea)
                        valores.append(linea2)
                        contador += 2
                    else:
                        contador += 1
                elif "Information" in line:
                    information += 1
                    if information > 1:
                        linea = re.sub('<.*?>', '', line)
                        linea2 = re.sub('<.*?>', '', lines[contador+1])
                        valores.append(linea)
                        valores.append(linea2)
                        contador += 2
                    else:
                        contador += 1
                elif "More details for" in line:
                    banderaVal = False
                else:
                    contador += 1
            row = []
            actual = 1
            n = 0
            n2 = 0
            h = 0
            datos = ("No.","Nombre","Ruta","Issue Detail","Issue background","Issue remediation","Severity","Confidence")
            with open(n[:len(n)-5] +'-parseado.csv', mode='w') as resul_file:
                writer = csv.writer(resul_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(datos)
                while n < len(resultados):
                    revision = resultados[n]
                    while revision != str(actual + 1) and n < len(resultados):
                        if revision != "\n" and revision != "":
                            resul = resultados[n]
                            resul = resul.replace("\n","")
                            resul = resul.replace("&nbsp;&nbsp;","")
                            if resul[0] == " ":
                                while resul[h] == " ":
                                    h += 1
                                resul = resul[h:]
                            row.append(resul)
                            n += 1
                            if n < len(resultados):
                                revision = resultados[n]
                        elif n < len(resultados):
                            n += 1    
                            revision = resultados[n]
                    if len(row) < 6:
                        while len(row) < 6:
                            row.append("")
                    row.append(valores[n2].replace("\n",""))
                    row.append(valores[n2+1].replace("\n",""))
                    actual += 1
                    writer.writerow(row)
                    row.clear()
                    n2 += 2
            file.close
                    
