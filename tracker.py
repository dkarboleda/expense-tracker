# Project: Expense Tracker - Installment 5
# Author: David Kristian M. Arboleda
# Description: Interactive menu-driven expense tracker with loop, choice handling, and budget verdict.

# 1. SETUP (Asked once)
print("-" * 40)
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("-" * 40)

print("\nMAIN MENU")
print("\t[1] Add an expense")
print("\t[2] View all expenses (coming soon)")
print("\t[3] Show total spent")
print("\t[4] Exit\n")

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print(f"Welcome, {name}!")

subtotal = 0.0
count = 0

# 2. INTERACTIVE MENU LOOP
while True:
    print("\nMAIN MENU")
    print("\t[1] Add an expense")
    print("\t[2] View all expenses (coming soon)")
    print("\t[3] Show total spent")
    print("\t[4] Exit\n")
    
    choice = input("Choose 1-4: ")
    
    if choice == "1":
        # OPTION 1: ADD EXPENSE & SIZE CHECK
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        
        if amount > 200:
            print("are you sure?")
            print("Huge expense")
        elif amount > 100:
            print("Big expense.")
        elif amount > 50:
            print("Moderate expense.")
        else:
            print("Small expense.")
            
    elif choice == "2":
        # OPTION 2: COMING SOON
        print("Coming soon: the tracker can't remember each item yet.")
        
    elif choice == "3":
        # OPTION 3: SUMMARY & VERDICT
        average = subtotal / count if count > 0 else 0.0
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = total > budget
        
        print("-" * 40)
        print("SUMMARY")
        print(f"Expenses:\t{count}")
        print(f"Subtotal:\t${subtotal}")
        print(f"Tax ({tax_percent}%):\t${tax}")
        print(f"Grand total:\t${total}")
        
        if over_budget:
            print(f"Over budget by ${total - budget}!")
        elif total > 0.9 * budget:
            print(f"Careful: only ${budget - total} left.")
        else:
            print(f"Within budget. ${budget - total} left.")
        print("-" * 40)
        
    elif choice == "4":
        # OPTION 4: EXIT
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print(f"Made by: David Kristian M. Arboleda | Installment 5")
        break
        
    else:
        # INVALID INPUT HANDLING
        print("Please choose 1, 2, 3 or 4.")