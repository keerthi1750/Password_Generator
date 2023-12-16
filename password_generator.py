import string
import random

characters= list(string.digits + string.ascii_letters + "!@#$%^&*()_")


def password_gen():

    pwd_length = int(input("enter the length of password: "))

    random.shuffle(characters)  #shuffles the list characters,which is in the order of digits,alpha and special chars
    password= []

    for i in range(pwd_length
                   ):
        password.append(random.choice(characters))   #picks random element of shuffled list (double shuffle!). random.choice choosse a single element randomly, so for every iteration, only 1 element is appended to the list
        #without random.choice, forms 'i' no of lists,each with all chars - in order if no shuffle(line 11), else out of order

    password = "".join(password)  #can only join elements of a single list object into a string, not multiple lists
    print(password)
    
option = input("Do you want a password? (y/n): ")

if option == 'y':
    password_gen()
elif option == 'n':
    print("program terminated")
    quit()
else:
    print("invalid input")
    quit()