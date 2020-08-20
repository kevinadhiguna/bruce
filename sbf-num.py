import random

password = str(input("[+] Enter your password (only numbers): "))
guess = ""

while guess != password:
    guess = str(random.randint(0, 9999))

    print("=> "+ guess)

    if (guess == password):
        print("The password is : "+ password)
        break
