import functions




while (True) :
    username = input("Username : ") 
    password = input("Password :")

    if functions.usercheck(username,password) == 1 : #This is login check.
        print("Logged in")
        break
   
    else:
        print("Can not logged in username or password entered incorrectly...")
        userdecision = input("if you want to register please tab 1 else please tab 2... ")
        if userdecision == "1" : 

            while (True): #this is register check.

                newusername = input("New Username :")
                newpassword = input("New Password :")

                if functions.registercheck(newusername,newpassword) == 0 : #İf the newly entered username does not exist before
                    functions.useradd(newusername,newpassword) #Append new user.
                    print("Registered succesfuly...")
                    break
                else:
                    print("This username already exist... ")
        else:
            print("You didn't want to register, we'll wait for you later...")
            break
            
                


 







