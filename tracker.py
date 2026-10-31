# Project: Expense Tracker - Installment 4
# Author: David Kristian M. Arboleda
# Description: Calculates running subtotal, tax rate, grand total, budget status, and remaining budget.

# 1. MENU & GREETING
print("=" * 40)
print("\t    EXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("\nMAIN MENU")
print("\t[1] Add an expense\t\t(coming soon)")
print("\t[2] View all expenses\t\t(coming soon)")
print("\t[3] Show total spent\t\t(coming soon)")
print("\t[4] Exit\t\t\t(coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

subtotal = 0.0

# 2. FIRST EXPENSE
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

# FIRST EXPENSE SIZE CHECK
if amount1 > 200:
    print("  are you sure?")
    print("  Huge expense")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# 3. SECOND EXPENSE
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

# SECOND EXPENSE SIZE CHECK
if amount2 > 200:
    print("  are you sure?")
    print("  Huge expense")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# TWO-BIG WARNING
if amount1 > 100 and amount2 > 100:
    print("  slow down!")
    print("  Two big expenses in a row")

# 4. CALCULATIONS
average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget

# 5. SUMMARY SECTION
print("\n" + "-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")

# VERDICT
if over_budget:
    print(f"Over budget by ${total - budget}!")
elif total > 0.9 * budget:
    print(f"Careful: only ${budget - total} left.")
else:
    print(f"Within budget. ${budget - total} left.")

print("-" * 40)
print("Made by: David Kristian M. Arboleda  |  Installment 4")