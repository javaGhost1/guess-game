from random import randint



correct_guess = randint(1, 10)
print(correct_guess)
print('Hello, what is your name?')
name = input()
print(f"okay! {name} I am Guessing a number between 1 and 10:")

plays = 0


while plays < 5:
    guess = int(input())

    plays += 1
    if guess < correct_guess:
        print("Your guess is too low")
    elif guess > correct_guess:
        print('Your guess is too high')
    else:
        print(f"You guessed the number in {plays} tries")
        break

