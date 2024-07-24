import random

hole = [i for i in range(1, 38)]

def roulette():
    global budget
    budget = 500
    start = False
    innerStart = False
    deposit = int(input("Input a deposit:"))
    if deposit > budget:
        print("Insufficient funds")
        start = False
    else:
        start = True

    if start:
        select = input("Select Red or Black: ")
        selectCap = select.capitalize()
        if selectCap == "Red" or "Black":
            innerStart = True
        else:
            innerStart = False
            print("Invalid selection")

    if innerStart:
        spin = random.randint(0, 36)
        if selectCap == "Red":
            if spin % 2 == 0:
                print("Congratulations! You won on red! Budget +100")
                budget += 100
            else:
                print("Sorry, you lost on red! Budget -50")
                budget -= 50
        elif selectCap == "Black":
            if spin % 2 != 0:
                print("Congratulations! You won on black! Budget +100")
                budget += 100
            else:
                print("Sorry, you lost on black! Budget -50")
                budget -= 50
    print(f"Current {budget}")

roulette()
