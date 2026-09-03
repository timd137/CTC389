#Timothy Duong
#CTC 389 Lab 7 Part 1

number = 3
guess = int(input("Guess my number: "))

while guess >= number-2 and guess <= number+2 and guess != number:
    guess = int(input("Close, try again: "))
if guess == number:
    print("Well done! You guessed my number")
elif guess > number+2:
    print("Sorry, you lost. Your guess was higher than my number which is", number)
elif guess < number-2:
    print("Sorry, you lost. Your guess was lower than my number which is", number)

