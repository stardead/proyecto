f={"dia":0,"mes":"","año":0}
fi={}
n=1
for i in range(n):
    dia=int(input(""))
    mes=input("")
    año=int(input(""))
    fi["dia"]=dia
    fi["mes"] = mes
    fi["año"] = año
    f[i] = fi
    if mes=="ENE":
        fi["mes"]=1
    elif mes=="FEB":
        fi["mes"] = 2
    elif mes=="MAR":
        fi["mes"] = 3
    if mes=="ABR":
        fi["mes"] = 4
    if mes=="MAY":
        fi["mes"] = 5
    if mes=="JUN":
        fi["mes"] = 6
    if mes=="JUL":
        fi["mes"] = 7
    if mes=="AGO":
        fi["mes"] = 8
    if mes=="SET":
        fi["mes"] = 9
    if mes=="OCT":
        fi["mes"] = 10
    if mes=="NOV":
        fi["mes"] =11
    if mes=="DIC":
        fi["mes"] =12
fo=(fi["dia"],fi["mes"],fi["año"])
print(fo)
