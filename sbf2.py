import random
import pyautogui
import string

# Make use of 'sting.printable' instead of manual definition.
# chars = "abdefghijklmnopqrstuvwxyz0123456789"

# 'string.printable' means it will include all character capable of being typed on a keyboard.
chars = string.printable
chars_list = list(chars)

password = pyautogui.password("Enter your password here: ")

guess_password = ""

while (guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print("<====="+ str(guess_password)+ "=====>")

    if(guess_password == list(password)):
        print("Your password is : "+ "".join(guess_password))
        break
