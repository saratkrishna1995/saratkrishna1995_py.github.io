import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
ltf=''
syf=''
nuf=''
for i in range(0,nr_letters):
    a=random.choice(letters)
    ltf+=a
    i+=1
#print(ltf)
for i in range(0,nr_symbols):
    a=random.choice(symbols)
    syf+=a
    i+=1
#print(syf)
for i in range(0,nr_numbers):
    a=random.choice(numbers)
    nuf+=a
    i+=1
#print(nuf)
pwd=ltf+syf+nuf
print(f"Generated Password is : {pwd}")
l_pwd=list(pwd)
#print(l_pwd)
random.shuffle(l_pwd)
rpwd=''
for i in l_pwd:
    rpwd+=i
print(f"Randomized Pssword is : {rpwd}")