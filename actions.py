import fancyprint

actions = [
    "Add purchase",
    "See purchase history",
    "See statistics",
    "Remove purchase",
    "Exit"
]

def input_confirmation():
    user_input = None

    while True:
        user_input = input("Confirmation (y/n): ").lower()[:1]

        if user_input!="y" and user_input!="n":
            fancyprint.error("Confirmation must strictly 'y' or 'n'!")
            continue

        break

    return user_input=="y"

def print_actions():
    print()
    fancyprint.print_title("Actions")

    for i, Action in enumerate(actions):
        print(f"{i+1}. {Action}")

    print(fancyprint.DEFAULT_LINE, end="\n\n")

def add_purchase(history, description, amount):
    history.append({
        "description": description,
        "amount": amount
    })

    fancyprint.error("Purchase was added to history!", "SUCCESS")

def remove_purchase(history, id):
    if id > len(history):
        fancyprint.error(f"ID {id} is not present in history")
        return

    found = history[id]

    fancyprint.print_title("Confirmation")
    fancyprint.print_line("Are you sure you want to remove   this item? (y/n)", False)
    print(fancyprint.DEFAULT_LINE)
    fancyprint.print_table_purchase("ID", "DESCRIPTION", "AMOUNT")
    print(fancyprint.DEFAULT_LINE)
    fancyprint.print_table_purchase(str(id), found["description"], str(found["amount"]))
    print(fancyprint.DEFAULT_LINE)
    print()

    confirmation = input_confirmation()

    if not confirmation:
        fancyprint.error(f"Remove purchase sequence interrupted", "INTERRUPTED")
        return

    del history[id]

    fancyprint.error(f"{id} was removed from history!", "SUCCESS")

def view_all(history):
    if len(history)==0:
        fancyprint.error("Purchase history is empty!", "INFO")
        return
    
    fancyprint.print_title("Purchase History")
    fancyprint.print_table_purchase("ID", "DESCRIPTION", "AMOUNT")
    fancyprint.print_table_purchase("-", "-", "-")

    for id, purchase in enumerate(history):
        fancyprint.print_table_purchase(str(id), purchase["description"], str(purchase["amount"]))

    print(fancyprint.DEFAULT_LINE)

def statistics(history):
    # TODO Purchase count, Purchase total, Average purchase price, highest purchase, lowest purchase
    count = len(history)

    if count==0:
        fancyprint.error("History is empty!", "Cannot show statistics")
        return

    total_price = 0
    highest_purchase = None
    lowest_purchase = None

    for i, purchase in enumerate(history):
        amount = purchase["amount"]

        total_price += amount

        if not highest_purchase or amount > highest_purchase["amount"]:
            highest_purchase = purchase

        if not lowest_purchase or lowest_purchase["amount"] > amount:
            lowest_purchase = purchase
    
    fancyprint.print_title("Statistics")
    fancyprint.print_table_statistics("Name", "Value", True)
    print(fancyprint.DEFAULT_LINE)
    fancyprint.print_table_statistics("Count", str(count))
    fancyprint.print_table_statistics("Total money", f"{total_price:.2f}")
    fancyprint.print_table_statistics("Average purchase", f"{total_price/count:.2f}")
    fancyprint.print_table_statistics("Max purchase", f"{highest_purchase["description"]} ({highest_purchase["amount"]})")
    fancyprint.print_table_statistics("Min purchase", f"{lowest_purchase["description"]} ({lowest_purchase["amount"]})")
    print(fancyprint.DEFAULT_LINE)

    fancyprint.continue_text()