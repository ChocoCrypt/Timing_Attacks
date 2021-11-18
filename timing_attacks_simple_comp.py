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
    real_password = "bad"
    if(comp(real_password , password)):
        print("You're in'")
    else:
        return(False)

def create_bad_password(lenght):
    stupid = ""
    for i in range(lenght):
        stupid += "A"
    return(stupid)

#vamos a suponer que el password es de maximo 20 caracteres
def crack_password_lengh():
    promedios = []
    for i in range(1,21):
        prom = []
        #hago esto 1000 veces para saber cuanto se demora
        for i in range(10000):
            password = create_bad_password(i)
            #calculo el tiempo que se demora la funcion
            init = time.time()
            simple_login(password)
            end = time.time()
            total_time = end-init
            prom.append(total_time)
        media = np.mean(prom)
        print(media)

crack_password_lengh()

