import readline
import random

#cantidad de palabras
ruta = "/home/javier/Escritorio/spanish.lst"
archivo = open(ruta)

cantidad_de_palabras = 0
for x in archivo:
        cantidad_de_palabras += 1

print("Cantidad de palabras:", cantidad_de_palabras)  

#promedio
archivo = open(ruta)
cantidad_de_letras = 0

for linea in archivo:
        cantidad_de_letras_por_linea = len((linea).strip())
        cantidad_de_letras += cantidad_de_letras_por_linea

promedio = cantidad_de_letras / cantidad_de_palabras
print("Promedio de letras por palabra:", "{0:.2f}".format(promedio))

#palabras mas larga

archivo = open(ruta)
lista_palabras = archivo.readlines()
lista_ordenada = sorted(lista_palabras, key=len, reverse=True)
palabra_mas_larga = (lista_ordenada[0])
palabra_final = palabra_mas_larga.strip("\n")
cantidad_caracteres = len(palabra_final)
    
print(f"La palabras mas larga es:, {palabra_mas_larga} y tiene {cantidad_caracteres} caracteres")

#Solicitar al operador una determinada cantidad de letras, si es cero termina el programa, si no
# elegir 20 palabras al azar que midan esa cantidad de letras y mostrarlas. (en mayúsculas)

archivo = open(ruta)
cantidad_de_letras = int(input("Ingrese una cantidad de letras:"))
if input == 0:
        exit()
else:    

        palabras_a_mostrar = []
lista_de_palabras = archivo.readlines()
for palabra in lista_de_palabras:
        if len(palabra.strip("\n")) == cantidad_de_letras:
            palabra = palabra.upper()
            palabras_a_mostrar.append(palabra.strip("\n"))
if len(palabras_a_mostrar) < 20:
                print(palabras_a_mostrar)
else:        
                print(random.choices(palabras_a_mostrar, k=20))