
def guess_num():
    secret_num = 411
    a = 0
    while a != secret_num:
        a = int(input("Guess the number: "))
        if a > secret_num:
            print("Too High")
        elif a < secret_num:
            print("Too low")
        else:
            print("You guessed the correct number. You WON!")

print("The game is starting.....")
guess_num()