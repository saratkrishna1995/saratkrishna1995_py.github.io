import random

def guess(val,c_choice):
    while val>0:
        inp= int(input("Make a guess : "))
        if inp > c_choice:
            print("Too High.")
            print("Guess again.")
            val-=1
            print(f"You have {val} attempts remaining to guess the number.")
        elif inp < c_choice:
            print("Too low.")
            print("Guess again.")
            val -= 1
            print(f"You have {val} attempts remaining to guess the number.")
        else:
            if inp==c_choice:
                print(f"You got it! The answer was {inp}")
                val=0
    if val==0 and inp!=c_choice:
        print("You've run out of guesses. Game lost")

    replay =''
    while replay=='':
        replay= input("Do you want to play again(y / n):")
        if replay=='n':
            return "false"
        elif replay == 'y':
            return "true"
        else:
            print("Recheck and enter: ")


run="true"
print("Welcome to the Number Guessing Game!")

while run=="true":
    print("I'm Thinking of a number between 1 and 100.")
    rand_choice=random.choice(range(1,101))
    dl=input("Choose a difficulty. Type 'easy' or 'hard':")
    if dl == 'easy':
        dl=10
        run=guess(dl,rand_choice)
    elif dl== 'hard':
        dl=5
        run=guess(dl,rand_choice)
    else:
        print("Validate and re-enter the difficulty levels")