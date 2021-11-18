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
    real_password = "JUEPUTA"
    if(comp(real_password , password)):
        print("You're in'")
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

def replace_index(string,index , letter):
    try:
        string = list(string)
        string[index] =  letter
        string = "".join(string)
        return(string)
    except:
        return(string)

def crack_key():
    dictionary = [chr(i) for i in range(ord("A"),ord("Z")+1)]
    password_lenght = crack_password_lengh()
    password = []
    palabra_prueba = create_bad_password(password_lenght)
    #entonces ahora lo que hacemos es intentar cada caracter n veces y según el tiempo de respuesta pues nos quedamos con el mayor
#crack_password_lengh()
crack_key()

