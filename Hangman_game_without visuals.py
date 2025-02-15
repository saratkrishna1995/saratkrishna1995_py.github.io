import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
display = ""
# TODO-1: - Use a while loop to let the user guess again.
while display!=chosen_word:
    guess = input("Guess a letter: ").lower()

# TODO-2: Change the for loop so that you keep the previous correct letters in display.
    for letter in chosen_word:
        test = []
        if len(display)==len(chosen_word):
            i = 0
            while i<len(display):
                test.append(display[i])
                i+=1
            x=test
            for y in range(0,len(display)):
                if test[y]=="_":
                    if guess==chosen_word[y]:
                        x[y]=guess
                    else:
                        pass
                else:
                    pass
            final=''
            for alpha in x:
                final=final+alpha
            display=final
        elif letter == guess:
            display += letter
        else:
            display += "_"
    print(display)
    if display==chosen_word:
        print("Cheers mate! You won")
    else:
        print("Let us keep guessing.")
print(f"Current Status:{final}")