          """Se crea previamente un archivo en excel que contiene:
            harina Azucar   Maiz
201  5     1   5   4
2016   6   2   11
2017   8   90   3
2018   5   32   6 
"""
#El programa leera los datos del archivo excel y calculara el promedio de cada producto
#Al terminar se creara otro archivo vacio de excel llamado promedio_anual donde se escribira el nombre de cada producto y su promedio de precios

import csv

import pprint

archivo= open("datosExcel.csv","r")


#Lista que almacenara los renglones
tabla=[]

#Ciclo que añadira cada renglon a la lista tabla
for renglon in csv.reader(archivo):
    tabla.append(renglon)
    
#cerramos el archivo
archivo.close()

#Imprime en forma de tabla
pprint.pprint(tabla)

    
#se crea el renglon donde se escribiran los resultados
renglon=[0.0]*len(tabla[0])


#primer elemento de la tabla llevara la palabra promedios
renglon[0]="promedios"


#Ciclo que recorre las columnas de 1 a longitud del renglon 
for c in range(1,len(renglon)):
    s=0
    
    
#Ciclo que realiza la suma de los elementos de cada columna
    for r in range(1,len(tabla)):
        s+=float(tabla[r][c])    #Se convierten los elementos de la cadena flotantes
        
    renglon[c]=s/3  #Divide el resultado de la suma entre el num de renglones -1
    
    
print(renglon)


#Escribee la tabla[0] y renglon en otro archivo llamado promedio_anual
salida=open("promedio_anual.cvs","w")

for k in range(0, len(tabla[0])):

    salida.write(str(tabla[0][k]))
salida.write("","")
salida.write("\n")
salida.write(str(renglon))
salida.close()



  
