import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
pn=input("Rock, Paper, Scissors it is. Please enter your name:\n")
st=[rock,paper,scissors]
uc=int(input("What is your choice among (1: Rock, 2: Paper, 3: Scissors. Enter the integer:"))
cc=random.randint(0,2)
print(f"{pn}'s choice is: {st[uc-1]}\n")
ucf=uc-1
print(f"Computer's choice is:{st[cc]}")
if cc==ucf:
    print("It's a draw!")
else:
    if cc==0:
        if ucf==1:
            print(f"{pn} Wins. Computer lost")
        elif ucf==2:
            print(f"{pn} lost. Computer Wins")
    elif cc==1:
        if ucf==0:
            print(f"{pn} lost. Computer Wins")
        elif ucf==2:
            print(f"{pn} Wins. Computer lost")
    else:
        if ucf==0:
            print(f"{pn} Wins. Computer lost")
        elif ucf==1:
            print(f"{pn} lost. Computer Wins")
print("End of game!")