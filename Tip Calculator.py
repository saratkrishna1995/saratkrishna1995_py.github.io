print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = 1+int(input("What percentage tip would you like to give? 10 12 15 "))/100
people = int(input("How many people to split the bill? "))
share=round((bill*tip)/people,2)
print(f"Each person should pay: ${share}")