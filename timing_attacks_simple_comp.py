import time
import numpy as np



#compare character by character
def comp(str1 , str2):
    if(len(str1) == len(str2)):
        for i in range(len(str1)):
            if(str1[i] != str2[i]):
                return False
        return True
    else:
        return False


def simple_login(password):
    real_password = "HOLA"
    if(comp(real_password , password)):
        return(True)
    else:
        return(False)

def create_bad_password(lenght):
    stupid = ""
    for i in range(lenght):
        stupid += "A"
    return(stupid)

#lo que estoy haciendo es mandar caracteres de diferentes longitudes para adivinar el tamaño de la llave
def crack_password_lengh():
    promedios = []
    #vamos a suponer que el password es de maximo 30 caracteres
    for i in range(30):
        prom = []
        #hago esto 1000 veces para saber cuanto se demora
        for j in range(10000):
            password = create_bad_password(i)
            #calculo el tiempo que se demora la funcion
            init = time.time()
            simple_login(password)
            end = time.time()
            total_time = end-init
            prom.append(total_time)
        media = np.mean(prom)
        promedios.append(media)
    #ahora agarro el mayor y ya
    password_lenght = np.argmax(promedios)
    print(f"la longitud de la llave es {password_lenght}")
    return(password_lenght)

def crack_key():
    dictionary = [chr(i) for i in range(ord("A") , ord("Z")+1)]
    password_lenght = crack_password_lengh()
    password = []
    pad = ""
    real_pad = ""
    palabra_prueba =f"{pad:<0{password_lenght}}"
    for l in range(password_lenght):
        proms_dictionary = []
        for j in dictionary:
            prom = []
            for x in range(200000):
                pad = real_pad + j
                palabra_prueba =f"{pad:<0{password_lenght}}"
                init = time.time()
                simple_login(palabra_prueba)
                stop = time.time()
                total = stop - init
                prom.append(total)
            promedio = np.mean(prom)
            proms_dictionary.append(promedio)
        chr_index = np.argmax(proms_dictionary)
        letter = dictionary[chr_index]
        real_pad += letter
        print(real_pad)
    password = real_pad
    print(f"password is {password}")
    return(password)


#crack_password_lengh()
crack_key()

