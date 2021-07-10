#
import pandas as pd
import matplotlib.pyplot as plt

datos= pd.read_csv("UCI_std.csv")
#Se crean variables donde se guardan los datos de cada region 
AyP= datos[datos.Region=="Arica y Parinacota"]
T= datos[datos.Region=="Tarapacá"]
A= datos[datos.Region=="Antofagasta"]
At= datos[datos.Region=="Atacama"]
C= datos[datos.Region=="Coquimbo"]
V= datos[datos.Region=="Valparaíso"]
RM= datos[datos.Region=="Metropolitana"]
O= datos[datos.Region=="O’Higgins"]
Ma= datos[datos.Region=="Maule"]
Ñ= datos[datos.Region=="Ñuble"]
B= datos[datos.Region=="Biobío"]
Ar= datos[datos.Region=="Araucanía"]
LR= datos[datos.Region=="Los Ríos"]
LL= datos[datos.Region=="Los Lagos"]
Ay= datos[datos.Region=="Aysén"]
M= datos[datos.Region=="Magallanes"]

d= pd.read_csv("UCI.csv", index_col=1)
df= pd.DataFrame(d)
df.head()
#print(df)

x= list(df.columns.values)
xs= x[-14:]
#print(xs)


yc = pd.read_csv("UCI.csv",",")
y = yc.iloc[3,[-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]]
ys= list(y)
#print(ys)

plt.bar(xs, ys)
plt.show






'''
menuprincipal= int(input("Menu Principal: \n 1- Gráficos  \n 2-Listado de Regiones y sus Códigos \n 3- Datos de Región  \n 4-Región con más y menos pacientes UCI \n 0- Salir \n Ingrese una opción: "))
while menuprincipal != 0 :
    if menuprincipal == 1 :
        print("Gráficos")
    elif menuprincipal == 2:
        print("Regiones")
        print("Las regiones y sus códigos son respectivamente:")
        #Se muestran las regiones y los codigos que las representan
        print("Arica y Parinacota:15 \n Tarapacá:1 \n Antofagasta:2 \n Atacama:3 \n Coquimbo:4 \n Valparaíso:5 \n Metropolitana:13 \n O’Higgins:6 \n Maule:7 \n Ñuble:16 \n Biobío:8 \n Araucanía:9 \n Los Ríos:14 \n Los Lagos:10 \n Aysén:11 \n Magallanes:12")
    elif menuprincipal == 3:
        print("Datos de Regiones")
        codigoregion=input("Ingrese el código o nombre de la región:")
        flag= False 

        while flag==False:

            if codigoregion == "Arica y Parinacota" or codigoregion == "15":
                print(AyP.iloc[-14:])  #Muestran los datos de la region ingresada de las ultimas 2 semanas
                flag=True
            elif codigoregion == "Tarapacá" or codigoregion == "1":
                print(T.iloc[-14:])
                flag=True
            elif codigoregion == "Antofagasta" or codigoregion == "2":
                print(A.iloc[-14:])
                flag=True
            elif codigoregion == "Atacama" or codigoregion == "3":
                print(At.iloc[-14:])
                flag=True
            elif codigoregion == "Coquimbo" or codigoregion == "4":
                print(C.iloc[-14:])
                flag=True
            elif codigoregion == "Valparaíso" or codigoregion == "5":
                print(V.iloc[-14:])
                flag=True
            elif codigoregion == "Metropolitana" or codigoregion == "13":
                print(RM.iloc[-14:])
                flag=True
            elif codigoregion == "O’Higgins" or codigoregion == "6":
                print(O.iloc[-14:])
                flag=True
            elif codigoregion == "Maule" or codigoregion == "7":
                print(M.iloc[-14:])
                flag=True
            elif codigoregion == "Ñuble" or codigoregion == "16":
                print(Ñ.iloc[-14:])
                flag=True
            elif codigoregion == "Biobío" or codigoregion == "8":
                print(B.iloc[-14:])
                flag=True
            elif codigoregion == "Araucanía" or codigoregion == "9":
                print(Ar.iloc[-14:])
                flag=True
            elif codigoregion == "Los Ríos" or codigoregion == "14":
                print(LR.iloc[-14:])
                flag=True
            elif codigoregion == "Los Lagos" or codigoregion == "10":
                print(LL.iloc[-14:])
                flag=True
            elif codigoregion == "Aysén" or codigoregion == "11":
                print(Ay.iloc[-14:])
                flag=True
            elif codigoregion == "Magallanes" or codigoregion == "12":
                print(M.iloc[-14:])
                flag=True
            else:
                codigoregion=input("Error, Ingrese un código o nombre de región válido: ")
                 
    elif menuprincipal == 4:
        print("Cantidad de pacientes UCI")

    else:
        print("Porfavor digite una opcion correcta")
    menuprincipal= int(input("Menu Principal: \n 1- Gráficos  \n 2-Listado de Regiones y sus Códigos \n 3- Datos de Región  \n 4-Región con más y menos pacientes UCI \n 0- Salir \n Ingrese una opción: "))
    
'''





'''
plt.plot(T.Poblacion,T.fecha)
plt.legend(["Pacientes UCI"])
plt.xlabel("dias")
plt.ylabel("pacientes")
plt.show


y= pd.read_csv("UCI_std.csv")
yc = T.iloc[4,[-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]]
ys= list(yc)
print(ys)
'''








