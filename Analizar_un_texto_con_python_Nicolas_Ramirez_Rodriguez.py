import requests # Importamos la biblioteca requests para hacer peticiones HTTP

enlace = "https://www.py4e.com/code3/mbox.txt" # Aqui se pone la url del archivo que vas a analizar, se obtiene el contewnido del archivo y 
obtener_enlace = requests.get(enlace)           # obtenemos el texto bruto del enlace
texto = obtener_enlace.text              

def count_vocales(texto): #se establece el contador en 0, se ponen las vocales para despues iterar en cada letra del texto
    numero_vocales = 0      #esto con fin de que si esta en las vocales pues se suma 1 al numero de vocales
    vocales = "aeiouAEIOU"
    for letra in texto:
        if letra in vocales:
            numero_vocales += 1
    return numero_vocales

def count_consonantes(texto): #se establece el contador en 0, se ponen las consonantes para despues iterar en cada letra del texto
    numero_consonantes = 0      #esto con fin de que si esta en las consonantes pues se suma 1 al numero de consonantes
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for letra in texto:
        if letra in consonantes:
            numero_consonantes += 1
    return numero_consonantes

def palabras_mas_repetidas(texto): 
    minuscula = texto.lower().split()       #Aqui se divide el texto en palabras con el split(), pero antes se transforma a minusculas, para que las cadenas sean iguales
    frecuencia = {}                         #luego se crea un diccionario para ver cuantas veces estara la palabra
    for palabra in minuscula:
        caracteres_validos = []
        for x in palabra:
            if x.isalnum():                  #Con esto se filtran solo los alfanumericos, pues para añadir letras/caracteres validos
                caracteres_validos.append(x)
        palabra_valida = "".join(caracteres_validos) #Aqui se forma la palabra valida
        if palabra_valida and not palabra_valida.isdigit(): #esta linea es para ver que sean palabras bajo las reglas que pusimos (minusculas, caracteres validos, etc)
            if palabra_valida in frecuencia:                   #y que no sean cadenas de numeros porque pues no son palabras xd
                frecuencia[palabra_valida] += 1             
            else:                                                   #este if y else, verifica si al palabra ya existe en el diccionario, entonces pues si si, 
                frecuencia[palabra_valida] = 1                      # se le va sumando de a 1 hasta las n veces que este
    palabras_en_orden = sorted(frecuencia.items(), key=lambda n: n[1], reverse=True) #y esto ordena de mayor a menor por el reverse, ya que sorted ordena la reves
    return palabras_en_orden[:50]

numero_vocales = count_vocales(texto)
numero_consonantes = count_consonantes(texto)

print(f'cantidad de vocales: {numero_vocales}')
print(f'cantidad de consonantes: {numero_consonantes}')
print('las 50 palabras más repetidas son:')
for palabra, frecuencia in palabras_mas_repetidas(texto):
    print(f'{palabra}: {frecuencia}')
