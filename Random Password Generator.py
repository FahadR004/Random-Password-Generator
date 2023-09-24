import random
from tkinter import *
from tkinter import messagebox

class NegativeLengthError(Exception):
    pass

class MissingValueError(Exception):
    pass


def check_numbers(string):
    for num in numbers:
        if num in string:
            return True


def check_symbols(string):
    for symbol in symbols:
        if symbol in string:
            return True


def get_password(length, chars="ALL"):
    password = ""

    if chars == "ONLYABC":  # Only alphabets
        for i in range(0, int(length)):
            index = random.randint(0, len(alphabets) - 1)  # len of alphabets variable
            password += alphabets[index]
        password_box.insert(0, password)

    elif chars == "ONLYABC123":  # Only alphabets and numbers
        ltrs_and_num = alphabets + numbers
        while True:
            for i in range(0, int(length)):
                index = random.randint(0, len(ltrs_and_num) - 1)
                password += ltrs_and_num[index]
            check_num = check_numbers(password)
            if check_num is True:
                break
        password_box.insert(0, password)

    elif chars == "ONLYABC#$&":
        ltrs_and_symbols = alphabets + symbols
        while True:
            for i in range(0, int(length)):
                index = random.randint(0, len(ltrs_and_symbols) - 1)
                password += ltrs_and_symbols[index]
            check_symbol = check_symbols(password)
            if check_symbol is True:
                break
        password_box.insert(0, password)

    elif chars == "ALL":
        all_characters = alphabets+numbers+symbols
        while True:
            for i in range(0, int(length)):
                index = random.randint(0, len(all_characters)-1)  # len of characters variable
                password += all_characters[index]
            check_num = check_numbers(password)
            check_symbol = check_symbols(password)
            if check_num is True and check_symbol is True:
                break
        password_box.insert(0, password)


def generate_password():
    try:
        if entry_box.get() == "":
            raise MissingValueError
        length = int(entry_box.get())
        password_box.delete(0, END)
        assert length <= 50
        if length < 0:
            raise NegativeLengthError
    except MissingValueError:
        icon = messagebox.showerror("Missing Length", "Please enter a value for length!!!")    
    
    except ValueError:
        icon = messagebox.showerror("Type Error", "Invalid Length!!!")
    
    except AssertionError:
        icon = messagebox.showerror("Length Error", "Length cannot be greater than 50 characters!!!")
    
    except NegativeLengthError:
        icon = messagebox.showerror("Invalid Length", "Length cannot be negative!!!")
    
    else:
        num_button_val = num_var.get()
        symbol_button_val = symbol_var.get()

        if num_button_val == "OFF" and symbol_button_val == "OFF":
            get_password(length, chars="ONLYABC")

        elif num_button_val == "ON" and symbol_button_val == "OFF":
            get_password(length, chars="ONLYABC123")

        elif num_button_val == "OFF" and symbol_button_val == "ON":
            get_password(length, chars="ONLYABC#$&")

        else:
            get_password(length, chars="ALL")   # Just showing explicitly


alphabets = "abcdefghijklmnopqrstuvwxyz"  # Length is 26
numbers = "1234567890"  # Length is 10
symbols = "!@#$%^&*?<>)(}{|"  # Length is 16

root = Tk()
root.title("Random Password Generator")

length_label = Label(root, text="Length (1-50): ")
length_label.grid(row=0, column=2)

entry_box = Entry(root, width=5, borderwidth=4)
entry_box.grid(row=0, column=3)

numbers_label = Label(root, text="Numbers")
numbers_label.grid(row=1, column=2)

num_var = StringVar()
number_checkbox = Checkbutton(root, variable=num_var, onvalue="ON", offvalue="OFF")
number_checkbox.deselect()
number_checkbox.grid(row=1, column=3)

symbols_label = Label(root, text="Symbols")
symbols_label.grid(row=2, column=2)

symbol_var = StringVar()
symbols_checkbox = Checkbutton(root, variable=symbol_var, onvalue="ON", offvalue="OFF")
symbols_checkbox.deselect()
symbols_checkbox.grid(row=2, column=3)

password_box = Entry(root, width=80, borderwidth=10)
password_box.grid(row=3, column=2, columnspan=3)


generate_password = Button(root, text="Generate Password", command=generate_password)
generate_password.grid(row=4, column=2, columnspan=3)

root.mainloop()
