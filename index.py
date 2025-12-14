import os, actions, fancyprint

def input_id():
    user_input = None

    while True:
        try:
            user_input = int(input("Insert id: "))
        except ValueError:
            fancyprint.error("id must be an integer!")
            continue

        if user_input < 0:
            fancyprint.error("id must be positive!")
            continue

        break

    return user_input

def input_price():
    user_input = None

    while True:
        try:
            user_input = float(input("Input price: "))
        except ValueError:
            fancyprint.error("Price must be a number!")
            continue

        if 0 >= user_input:
            fancyprint.error("Price must be positive!")
            continue

        break

    return user_input

def input_text():
    user_input = None

    while True:
        user_input = input("Input description: ")

        if len(user_input)==0 or user_input.isspace():
            fancyprint.error("Description can't be empty!")
            continue

        if user_input.isnumeric():
            fancyprint.error("Description can't be a number!")
            continue

        break

    return user_input.strip()

purchaseHistory = []

# purchaseHistory = [
#     {"description": "Pane", "amount": 4.0},
#     {"description": "Pesce", "amount": 15.99},
#     {"description": "Uova", "amount": 10.55}
# ]

def start():
    running = True
    user_input = None

    while running:
        os.system("cls")
        actions.print_actions()

        # Check if input is a number
        try:
            user_input = int(input("Insert action code: "))
        except ValueError:
            fancyprint.error("Action code must be a number!")
            continue
        
        # Check if code exists
        if user_input <= 0 or user_input > len(actions.actions):
            fancyprint.error(f"Action {user_input} doesn't exist!")
            continue

        if user_input==1:
            description = input_text()
            price = input_price()

            actions.add_purchase(purchaseHistory, description, price)
        
        elif user_input==2:
            actions.view_all(purchaseHistory)

            fancyprint.continue_text()
        
        elif user_input==3:
            actions.statistics(purchaseHistory)

        elif user_input==4:
            actions.view_all(purchaseHistory)

            # If history is empty, skip iteration
            if len(purchaseHistory)==0:
                continue

            fancyprint.print_title("What do you want to remove?")

            id = input_id()

            actions.remove_purchase(purchaseHistory, id)
        
        elif user_input==5:
            break
    
    total = 0

    for v in purchaseHistory:
        total += v["amount"]

    fancyprint.error(f"You spent {total:.2f} in total for this session! thank you for relying on  us!", "Application closed")


start()
