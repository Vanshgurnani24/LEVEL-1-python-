def checkPass(inpstr):
    n=len(inpstr)
    lowercase=False
    uppercase=False
    isNumber=False
    isSpecial=False
    inputchar='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in range(n):
        if inpstr[i].isupper():
            uppercase=True
        if inpstr[i].islower():
            lowercase=True
        if inpstr[i].isdigit():
            isNumber=True
        if inpstr[i] not in inputchar:
            isSpecial=True
    print("Strength of password:- ",end="")
    if (lowercase and uppercase and isNumber and isSpecial and n>=8):
        print("Strong")
    elif(lowercase or uppercase) and (isSpecial and n>=6):
        print("Moderate")
    else:
        print("Weak")
inpstr=input("Enter your password: ")
checkPass(inpstr)