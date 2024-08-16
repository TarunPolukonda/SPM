import random
def genotp():
    otp=''
    caps=[chr(i) for i in range(ord('A'),ord('Z'))]
    sm=[chr(i) for i in range(ord('a'),ord('z'))]
    for i in range(0,2):
        otp=otp+random.choice(caps)
        otp+=str(random.randint(0,9))
        otp+=random.choice(sm)
    return otp
