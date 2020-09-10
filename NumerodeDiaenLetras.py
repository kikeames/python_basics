'''El  año 2020 tiene 366 días, 
escriba un programa el cual al momento de ingresar
una cantidad de días transcurridos, 
este calcule en qué día estamos
ejemplo: 70
prompt : martes, 10 de Marzo
'''

sumaDias_Ene = 31
sumaDias_Feb = 29
sumaDias_Mar = 31
sumaDias_Abr = 30
sumaDias_May = 31
sumaDias_Jun = 30
sumaDias_Jul = 31
sumaDias_Ago = 31
sumaDias_Set = 30
sumaDias_Oct = 31
sumaDias_Nov = 30
sumaDias_Dic = 31

Acumulado1 = sumaDias_Ene + sumaDias_Feb
Acumulado2 = Acumulado1 + sumaDias_Mar
Acumulado3 = Acumulado2 + sumaDias_Abr
Acumulado4 = Acumulado3 + sumaDias_May
Acumulado5 = Acumulado4 + sumaDias_Jun
Acumulado6 = Acumulado5 + sumaDias_Jul
Acumulado7 = Acumulado6 + sumaDias_Ago
Acumulado8 = Acumulado7 + sumaDias_Set
Acumulado9 = Acumulado8 + sumaDias_Oct
Acumulado10 = Acumulado9 + sumaDias_Nov
Acumulado11 = Acumulado10 + sumaDias_Dic

def QueMesEs(x):
    if int(x)<=sumaDias_Ene:
        return ("Enero")
    else:
        if int(x)<=Acumulado1:
            return ("Febrero")
        else:
            if int(x)<=Acumulado2:
                return ("Marzo")
            else:
                if int(x)<=Acumulado3:
                    return ("Abril")
                else:
                    if int(x)<=Acumulado4:
                        return ("Mayo")
                    else:
                        if int(x)<= Acumulado5:
                            return ("Junio")
                        else:
                            if int(x)<=Acumulado6:
                                return ("Julio")
                            else:
                                if int(x)<=Acumulado7:
                                    return ("Agosto")
                                else:
                                    if int(x)<=Acumulado8:
                                        return ("Setiembre")
                                    else:
                                        if int(x)<=Acumulado9:
                                            return ("Octubre")
                                        else:
                                            if int(x)<=Acumulado10:
                                                return ("Noviembre")
                                            else:
                                                if int(x)<=Acumulado11:
                                                    return ("Diciembre")
                                                else:
                                                    print ("El numero ingresado excede la cantidad permitida")


def QueDiaEsNumber(x):
    if int(x)<=sumaDias_Ene:
        return (int(x))
    else:
        if int(x)<=Acumulado1:
            return (int(x)-sumaDias_Ene)
        else:
            if int(x)<=Acumulado2:
                return (int(x)-Acumulado1)
            else:
                if int(x)<=Acumulado3:
                    return (int(x)-Acumulado2)
                else:
                    if int(x)<=Acumulado4:
                        return (int(x)-Acumulado3)
                    else:
                        if int(x)<= Acumulado5:
                            return (int(x)-Acumulado4)
                        else:
                            if int(x)<=Acumulado6:
                                return (int(x)-Acumulado5)
                            else:
                                if int(x)<=Acumulado7:
                                    return (int(x)-Acumulado6)
                                else:
                                    if int(x)<=Acumulado8:
                                        return (int(x)-Acumulado7)
                                    else:
                                        if int(x)<=Acumulado9:
                                            return (int(x)-Acumulado8)
                                        else:
                                            if int(x)<=Acumulado10:
                                                return (int(x)-Acumulado9)
                                            else:
                                                if int(x)<=Acumulado11:
                                                    return (int(x)-Acumulado10)
                                                else:
                                                    print ("El numero ingresado excede la cantidad permitida")
    

Lunes = {6,13,20,27,34,41,48,55,62,69,76,83,90,97,104,111,118,125,132,139,146,
153,160,167,174,181,188,195,202,209,216,223,230,237,244,251,258,265,272,279,286,
293,300,307,314,321,328,335,342,349,356,363}

Martes = {7,14,21,28,35,42,49,56,63,70,77,84,91,98,105,112,119,126,133,140,147,154,
161,168,175,182,189,196,203,210,217,224,231,238,245,252,259,266,273,280,287,294,301,
308,315,322,329,336,343,350,357,364}

Miercoles = {1,8,15,1,8,15,22,29,36,43,50,57,64,71,78,85,92,99,106,113,120,127,
134,141,148,155,162,169,176,183,190,197,204,211,218,225,232,239,246,253,260,267,
274,281,288,295,302,309,316,323,330,337,344,351,358,365}

Jueves = {2,9,16,23,30,37,44,51,58,65,72,79,86,93,100,107,114,121,128,135,142,
149,156,163,170,177,184,191,198,205,212,219,226,233,240,247,254,261,268,275,282,289,
296,303,310,317,324,331,338,345,352,359,366}

Viernes = {3,10,17,24,31,38,45,52,59,66,73,80,87,94,101,108,115,122,129,136,143,150,
157,164,171,178,185,192,199,206,213,220,227,234,241,248,255,262,269,276,283,290,297,
304,311,318,325,332,339,346,353,360}

Sabado = {4,11,18,25,32,39,46,53,60,67,74,81,88,95,102,109,116,123,130,137,144,151,
158,165,172,179,186,193,200,207,214,221,228,235,242,249,256,263,270,277,284,291,298,
305,312,319,326,333,340,347,354,361}

Domingo = {5,12,19,26,33,40,47,54,61,68,75,82,89,96,103,110,117,124,131,138,145,152,159,
166,173,180,187,194,201,208,215,222,229,236,243,250,257,264,271,278,285,292,299,306,313,
320,327,334,341,348,355,362}

def QueDiaEsText(y):
    if int(y) in (Lunes):
        return ("Lunes")
    elif int(y) in (Martes):
        return ("Martes")
    elif int(y) in (Miercoles):
        return ("Miercoles")
    elif int(y) in (Jueves):
        return ("Jueves")
    elif int(y) in (Viernes):
        return ("Viernes")
    elif int(y) in (Sabado):
        return ("Sabado")
    elif int(y) in (Domingo):
        return ("Domingo")

  

num_dia = input("Ingrese el número de día\n")

print("El número ingresado pertenece al mes de", QueMesEs(num_dia))

print("El número ingresado pertenece al dia", QueDiaEsNumber(num_dia))

print("El número ingresado pertenece al dia", QueDiaEsText(num_dia))

print( QueDiaEsText(num_dia), QueDiaEsNumber(num_dia), "de",QueMesEs(num_dia),)

