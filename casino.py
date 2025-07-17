import random
print("Welcome to the Python Slot Machine Game!")
print("You have a balance of $100.")
balance=100
letters=["A","B","C"]
while balance>0:
    print(f"You have {balance}")
    while True:
        lines = int(input("Enter the number of lines to bet on (1-3): "))
        if 0<lines<4:
            break
        else:
            print("Please enter a number between 1 and 3")
    while True:
        bet = int(input("Enter your bet per line: "))
        total_bet=bet*lines
        if total_bet<=balance:
            break
    winnings=0
    for i in range(lines):
        a=random.choice(letters)
        b=random.choice(letters)
        c=random.choice(letters)
        print("|",a,"|",b,"|",c,"|")
        if a==b==c:
            win_amount=bet*5
            print("You won: ",win_amount)
            winnings=winnings+win_amount
    balance=balance-total_bet
    balance=balance+winnings
    print("You have:",balance)
    while True:
        
        question = input("Do you wish to continue? ").lower()
        if question == "y":
            break
        elif question == "n":
            print("Thanks for playing")
            exit()
        else:
            print("Please enter y or n!")
    if balance<0:
        print("You are out of money")
        break
        
        
    
    
        
    
