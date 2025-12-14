import math

DEFAULT_LINE = "-" * 38

# ! DISCLAIMER !
# I was really, really tired when I wrote this script
# If something (or everything) is not clear, blame the past me and not
# the present me.

def fill_textbox(text, spaces, centered = False):
    # First two spaces are always kept empty for padding, so the text will fit in (space-2)
    true_space = spaces-2

    # Cut string if it is too long
    if len(text) > true_space:
        text = text[:true_space-3] + "..."

    empty_space = true_space - len(text)

    # Text will be displayed to the left if centered==False
    if not centered:
        return f" {text}{' '*(spaces-2-len(text))} "

    # If the space left is not even, we want less spaces in the first half
    # And more spaces in the second
    first_half = math.floor(empty_space/2) * " "
    second_half = round(empty_space/2) * " "

    return f" {first_half + text + second_half} "

def print_line(text, single_line=True):
    # Single line mode will force the text in one line, cutting it if needed
    if single_line:
        print(f"-{fill_textbox(text, len(DEFAULT_LINE)-2, True)}-")
        return

    text_fit = len(DEFAULT_LINE)-4
    lines = math.ceil(len(text)/text_fit)

    for i in range(lines):
        to_print = text[i*text_fit:(i+1)*text_fit]
        print(f"-{fill_textbox(to_print, len(DEFAULT_LINE)-2, lines==1)}-")

def print_title(title):
    print()
    print(DEFAULT_LINE)
    print_line(title)
    print(DEFAULT_LINE)

# Although this function is named "error", it's just a notification
# I'm not refactoring it because I actually like the name.
def error(message, title="ERROR"):
    print()
    print_title(title)

    print_line(message, False)

    print(DEFAULT_LINE, end="\n\n")

    continue_text()

def print_table_purchase(id, description, amount):
    print(f"{fill_textbox(id, 5)}|{fill_textbox(description, 18)}|{fill_textbox(amount, 16)}")

def print_table_statistics(name, value, centered=False):
    print(f"{fill_textbox(name, 18, centered)}|{fill_textbox(value, 20, centered)}")

def continue_text():
    print()
    input("Press enter to continue...")

# Examples of use:
# error("Ciaoo :3, sto scrivendo un testo lungo per capire se l'errore mostrato qui si legge bene ed è visivamente carino, non farci caso :3333")

# error("Description cannot be this short!")

# print_title("Purchase History")
# print_table_purchase("ID", "DESCRIPTION", "AMOUNT")
# print_table_purchase("-", "-", "-")
# print_table_purchase("1", "Cinema", "€ 3.88")
# print(DEFAULT_LINE)

# print_title("Statistics")
# print_table_statistics("Name", "Valore", True)
# print(DEFAULT_LINE)
# print_table_statistics("Max purchase", "Newspaper (€100)")
# print_table_statistics("Min purchase", "Cinema (€50.80)")
# print(DEFAULT_LINE)