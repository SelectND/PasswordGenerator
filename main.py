import random
import string


# Checks if any input is y, Y, n or N
def yes_no_checker(question):
    while True:
        inp = input(question)
        if inp == "y" or inp == "Y":
            return True
        elif inp == "n" or inp == "N":
            return False
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
        if inp < 3:
            print("The password has to be at least 3 characters long.")
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
    info = information()
    while True:
        # Initializes characters and information
        specialChars = r"!@#$%^&*()"
        specialCharsArr = []
        for i in specialChars:
            specialCharsArr.append(i)
        digits = string.digits
        letters = string.ascii_letters

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

        # Checks that the password contains at least one of each earlier specified character group
        digits_in = False
        letter_in = False
        special_char_in = False
        for pos in passwd:
            for i in string.digits:
                if pos == i:
                    digits_in = True

        for pos in passwd:
            for i in string.ascii_letters:
                if pos == i:
                    letter_in = True

        for pos in passwd:
            for i in specialCharsArr:
                if pos == i:
                    special_char_in = True

        # Matches the result with the given preferences
        matches = 0
        if info[1] == special_char_in:
            matches += 1
        if info[2] == letter_in:
            matches += 1
        if info[3] == digits_in:
            matches += 1

        # Final check


        # Converts array to string
        finalPassword = ("".join(passwd))

        # Prints the string
        print(finalPassword)
        if matches <= 2:
            print("The password didn't match the specified information. Regenerating...")
            continue
        input("Press enter to leave: ")
        break
