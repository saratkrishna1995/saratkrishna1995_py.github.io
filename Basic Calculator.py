def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

print("Hello, Welcome to cruncher! I just crunch numbers")

n1 = int(input("Please enter first number:"))

calculation=1

while calculation==1:
    n2 = int(input("Please enter second number:"))
    operations = {"+": add(n1, n2),
                  "-": sub(n1, n2),
                  "*": mul(n1, n2),
                  "/": div(n1, n2)
                  }
    operation=input("Please enter the mathematical operation you wish to perform + , - , *, / : ")
    for key in operations:
        if key == operation:
            print(f"Result is {operations[operation]}")
            follow_up = input("Do you want to continue with the result y/n/stop:").lower()
            break
        else:
            continue

    if follow_up=="y":
        n1=operations[operation]
    elif follow_up=="n":
        n1 = int(input("Please enter first number:"))
    elif follow_up=="stop":
        print("Result delivered. End of crunching")
        calculation=0