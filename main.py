import random
import string

if __name__ == '__main__':
    # defining the base construction
    length = int(input("Password length: "))
    chars = list(string.ascii_letters + string.digits + r"!@#$%^&*()")
    random.shuffle(chars)

    # creating the password as an array
    passwd = []
    for i in range(length):
        passwd.append(random.choice(chars))
    random.shuffle(passwd)

    # converting array to string and printing the string
    finalPassword = ("".join(passwd))
    print(finalPassword)
    input("Press any key to leave: ")
