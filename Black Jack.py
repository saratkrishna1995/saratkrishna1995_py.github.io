import random

"""Scoring if the dealt card is Ace"""

def ace(val,hand):
    x = random.choice(cards)
    hand.append(x)
    if val+x==21:
        pt=21
        return pt,hand
    elif x==11:
        if (val+x) >21:
            val=val+1
            return val,hand
        else:
            val=val+x
            return val,hand
    else:
        val=val+x
        return val,hand


"""Dealing the cards"""

def deal(val,player,hand):
    deal_again='y'
    while deal_again == 'y':
        print(f'{player} total is {val}')
        print(f'{player} hand is {hand}')
        choice=''
        if val!=21:
            choice = input('Do you want to deal (y/n):')
        if choice == 'y':
            score, deck = ace(val,hand)
            val=score
            if val ==21 or val >21:
                #result='n'
                return val,deck
        else:
            return val, hand

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game=input("Do you want to play blackjack y/n: ?")
player=input("Enter player's name: ")
game='y'
ct = random.choice(cards)
print(f"Computer's first card is {ct}")
pc1 = random.choice(cards)
pc2 = random.choice(cards)
pis=pc1+pc2
p_hand=[]
c_hand=[]
p_hand.append(pc1)
p_hand.append(pc2)
c_hand.append(ct)
while game =="y":
    pt, p_hand=deal(pis,player,p_hand)
    if pt==21:
        print(f"{player} wins! It's a black Jack. {player}'s hand is {p_hand}")
        game="n"
    elif pt<21:
        ct_result='true'
        while ct_result=='true':
            ct, c_hands=ace(ct,c_hand)
            if ct==21:
                print(f"Computer score is {ct}")
                print(f"Computers hand {c_hands} & {player}'s hand is {p_hand}")
                print(f"Computer wins, {player} loses!")
                ct_result='false'
                game="n"
            elif ct>21:
                print(f"Computer score is {ct}")
                print(f"Computers hand {c_hands} & {player}'s hand is {p_hand}")
                print(f"{player} wins, Computer loses!")
                ct_result='false'
                game = "n"
            elif ct>pt:
                print(f"Computer score is {ct}")
                print(f"Computers hand {c_hands} & {player}'s hand is {p_hand}")
                print(f"Computer wins, {player} loses!")
                ct_result='false'
                game = "n"
    else:
        print(f"Computers hand {c_hand} & {player}'s hand is {p_hand}")
        print("Computer wins, Player loses!")
        game="n"