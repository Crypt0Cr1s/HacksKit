class utilities:
    def Lfiles(archivo):
        f = open(archivo, "r")
        sitios = []
        for line in f:
            sitios.append(line[0:len(line)-1])
        f.close()
        return sitios