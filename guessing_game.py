import random
secret_number = random.choice(range(1, 101))

print("I've selected a number between 1 and 100!!! ")

while True:
    guess = int(input("Your guess: "))

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue  

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You got it!")
        break
