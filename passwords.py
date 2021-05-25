from random import choice
import string
import os

masterPassword = "ILOVEPYTHON"

def generatePassword(passLength):
    chars = string.ascii_letters + string.digits
    password = ''.join(choice(chars) for i in range(passLength))

    def copyToClipboard(text):
        command = 'echo ' + text.strip() + '| clip'
        os.system(command)

    copyToClipboard(password)
    print(password)
    