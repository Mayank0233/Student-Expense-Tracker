import calc
import inputs
import display
import Categories
import Storage

total = 0.0
budget = inputs.get_budget()

while True:
    display.menu()
    choice = inputs.get_choice()
    
    if choice == "1":
        item = inputs.get_item()
        cat = Categories.get_category()
        cost = float(inputs.get_cost())
        total = calc.add(total, cost)
        Storage.save(item, cat, cost)
        display.receipt(item, cat, cost)
    elif choice == "2":
        records = Storage.read()
        if not records:
            print("No expenses found.")
        else:
            print("\n--- ALL EXPENSES ---")
            for r in records:
                print(r, end="")
    elif choice == "3":
        rem = calc.remaining(budget, total)
        display.balance(budget, total, rem)
    elif choice == "4":
        print("bye")
        break
    

