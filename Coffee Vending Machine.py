MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report(res,money):
    for i in res:
        print(f"{i.title()} : {resources[i]} ml")
    print(f"Money : ${money}")

def resource_check(a,x,MENU):
    for i in a:
        if i in MENU[x]["ingredients"]:
            if a[i]>MENU[x]["ingredients"][i]:
                pass
            else:
                print(f"Sorry there is not enough {i}.")
                return "False"
            return "True"
        else:
            pass

def process_coins(x,MENU,money):
    print("Please insert coins")
    a=int(input("How many quarters?"))
    b=int(input("How many dimes?"))
    c=int(input("How many nickles?"))
    d=int(input("How many pennies?"))
    total=(a*0.25)+(b*0.1)+(c*0.05)+(d*0.01)
    if total>MENU[x]["cost"]:
        refund=total-MENU[x]["cost"]
        profit=money+MENU[x]["cost"]
        print(f"Here is ${round(refund,2)} dollars in change.")
        return profit, "success"
    elif total==MENU[x]["cost"]:
        profit = money + MENU[x]["cost"]
        return profit, "success"
    else:
        print("Sorry that's not enough money. Money refunded")
        return money,"failed"

def preparation(a,x,MENU):
    for i in a:
        if i in MENU[x]["ingredients"]:
            a[i]=a[i]-MENU[x]["ingredients"][i]
        else:
            pass
    print(f"Here is your {x}. Enjoy!")
    return a

machine ='on'
money = 0
a = resources
while machine=='on':
    x=input("What would you like ? (espresso/latte/cappuccino):").lower()
    if x=='off':
        machine ='off'
    elif x not in ("espresso","latte","cappuccino"):
        print("Please input correctly")
        pass
    else:
        report(a,money)
        all_ok=resource_check(a,x,MENU)
        if all_ok=="True":
            money, status=process_coins(x,MENU,money)
            if status=="success":
                a=preparation(a,x,MENU)
            else:
                pass
        else:
            pass