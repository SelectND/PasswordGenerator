import random
import string


# Checks if any input is y, Y, n or N
def yes_no_checker(question):
    while True:
        inp = input(question)
        if inp == "y" or inp == "Y":
            return True
            break
        elif inp == "n" or inp == "N":
            return False
            break
        else:
            continue


# Asks for information
def information():

    # Asks for password length and checks the value for being a valid integer
    while True:
        inp = input("Password length: ")
        try:
            inp = int(inp)
        except ValueError:
            continue
        break

    # Puts the information in an array
    info = []
    info.append(inp)
    info.append(yes_no_checker("Should the password include the following chars? ( !@#$%^&*() ) [y/n]"))
    info.append(yes_no_checker("Should the password include normal letters? [y/n]"))
    info.append(yes_no_checker("Should the password include regular number(natural Numbers)? [y/n]"))
    return info


if __name__ == '__main__':
    # Initializes characters and information
    specialChars = r"!@#$%^&*()"
    digits = string.digits
    letters = string.ascii_letters
    info = information()

    # Puts allowed characters into an array
    allowedChars = []
    for i in range(len(info)):
        if info[i]:
            if i == 1:
                allowedChars.append(specialChars)
            elif i == 2:
                allowedChars.append(letters)
            elif i == 3:
                allowedChars.append(digits)
    allowedCharsString = ("".join(allowedChars))

    # Makes array from string and shuffles it
    chars = []
    for i in range(len(allowedCharsString)):
        chars.append(allowedCharsString[i])
    random.shuffle(chars)

    # Creates the password as an array
    passwd = []
    for i in range(info[0]):
        passwd.append(random.choice(chars))
    random.shuffle(passwd)

    # Converts array to string and prints the string
    finalPassword = ("".join(passwd))
    print(finalPassword)
    input("Press any key to leave: ")
