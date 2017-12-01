#Abrir archivo
archivo= open("archivo.txt", "r")
cabecera= archivo. readline()
dic={}
for linea in archivo:
    lista=[x.stript()for x in linea.split("")]
    dic[lista[0]]=lista[1]
print(dic)