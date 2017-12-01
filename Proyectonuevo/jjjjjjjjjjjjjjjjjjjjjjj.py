f={"dia":0,"mes":"","año":0}
fi={}
n=1
for i in range(n):
    n=input("")
    if n[0]=="0":
        dia = int(n[0:2])
        mes = n[3:6]
        año = int(n[7:len(n)])
    elif int(n[0])==1 and n[1]=="-" or int(n[0])==2 and n[1]=="-" or int(n[0])==3 and n[1]=="-" or int(n[0])==4 and n[1]=="-" or int(n[0])==5 and n[1]=="-" or int(n[0])==6 and n[1]=="-" or int(n[0])==7 and n[1]=="-" or int(n[0])==8 and n[1]=="-" or int(n[0])==9 and n[1]=="-" :
        dia=int(n[0])
        mes=n[2:5]
        año = int(n[6:len(n)])
    elif int(n[0:2]) >9:
        dia = int(n[0:2])
        mes = n[3:6]
        año = int(n[7:len(n)])

    fi["dia"]=dia
    fi["mes"]=mes
    fi["año"]=año
    f[i] = fi
    if mes=="ENE":
        fi["mes"]=1
        fo = (fi["dia"], fi["mes"], fi["año"])
        print(fo)

    elif mes=="FEB":
        fi["mes"] = 2
        if dia>=30:
            print("Valor Invalido")
        else:
            fo = (fi["dia"], fi["mes"], fi["año"])
            print(fo)

    elif mes=="MAR":
        fi["mes"] = 3
        if dia >= 30:
            print("Valor Invalido")
        else:
            fo = (fi["dia"], fi["mes"], fi["año"])
            print(fo)

    if mes=="ABR":
        if dia >= 30:
            print("Valor Invalido")
        else:
            fi["mes"] = 4
            fo = (fi["dia"], fi["mes"], fi["año"])
        print(fo)

    if mes=="MAY":
        if dia >= 30:
            print("Valor Invalido")
        else:
            fi["mes"] = 5
            fo = (fi["dia"], fi["mes"], fi["año"])
        print(fo)

    if mes=="JUN":
        if dia >= 30:
            print("Valor Invalido")
        else:
            fi["mes"] = 6
            fo = (fi["dia"], fi["mes"], fi["año"])
            print(fo)

    if mes=="JUL":
        if dia >= 30:
            print("Valor Invalido")
        else:
            fi["mes"] = 7
            fo = (fi["dia"], fi["mes"], fi["año"])
            print(fo)

    if mes=="AGO":
        if dia >= 30:
            print("Valor Invalido")
        else:
            fi["mes"] = 8
            fo = (fi["dia"], fi["mes"], fi["año"])
            print(fo)

    if mes=="SET":
        if dia >= 30:
            print("Valor Invalido")
        else:
            fi["mes"] = 9
            fo = (fi["dia"], fi["mes"], fi["año"])
            print(fo)

    if mes=="OCT":
        if dia >= 30:
            print("Valor Invalido")
        else:
            fi["mes"] = 10
            fo = (fi["dia"], fi["mes"], fi["año"])
            print(fo)

    if mes=="NOV":
        if dia >= 30:
            print("Valor Invalido")
        else:
            fi["mes"] =11
            fo = (fi["dia"], fi["mes"], fi["año"])
            print(fo)

    if mes=="DIC":
        if dia >= 30:
            print("Valor Invalido")
        else:
            fi["mes"] =12
            fo = (fi["dia"], fi["mes"], fi["año"])
            print(fo)
    if mes=="ENERO" or mes=="FEBRERO" or mes=="MARZO" or mes=="ABRIL" or mes=="MAYO" or mes=="JUNIO" or mes=="JULIO" or mes=="AGOSTO" or mes=="STIEMBRE" or mes=="OCTUBRE" or mes=="NOVIEMBRE" or mes=="DICIEMBRE":
        print("Valor Invalido")