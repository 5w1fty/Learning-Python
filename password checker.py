def passwordchecker(password):
    print("dein Password ist :" + password)
    passwordIn = input("Gebe dein Password ein:")
    if(passwordIn == password):
        print("Richtiges Password!")
        option = input("Options: 1=change password, 2=return")
        if(option == 1):
            password = input("New Password:")
        if(option == 2):
            return

if __name__ == "__main__":
    pword = input("Definiere dein Password:")
    while(True):
        passwordchecker(pword)