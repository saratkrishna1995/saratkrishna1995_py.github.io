import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


lives=6
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
check=False
glist=[]

#Using a while loop to let the user guess again

while check is False:
    guess = input("Guess a letter: ").lower()
    display = ""

#Display gets built every time a new guess is made

    for letter in chosen_word:
        if letter in glist:
            display +=letter
            continue
        elif letter == guess:
            glist.append(guess)
            print(glist)
            display += guess
        else:
            display += "_"
    if display==chosen_word:
        check=True
        print("You won! End of game")
    print(display)

#Lives adjustment when wrong guess is made

    if guess not in chosen_word:
        lives -= 1
        print("Life lost")
        print(stages[lives])

    if "_" not in display:
        check = True
        print("You win.")

    if lives==0:
        print("You loose!Man hanged and game over")
        check=True
