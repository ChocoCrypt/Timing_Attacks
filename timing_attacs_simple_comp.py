import time



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
    real_password = "badbunny85"
    if(comp(real_password , password)):
        print("You're in'")
    else:
        print("Pailas")
