from tkinter import *
from tkmacosx import Button
import re

win = Tk()
win.geometry("250x315")
win.title("Calculator")
win.attributes('-alpha', 0.95)
win.attributes('-type', 'dock')
icon = PhotoImage(file = "/Users/arinaymahendru/Desktop/Coding/Python/hackathon/icon.png")
# icon = PhotoImage(file = "icon.png")

win.iconphoto(False,icon)
win.resizable(0,0)

expression = "0"

def click(cont):
    global expression
    expression = str(expression)
    if expression == 0 or expression == "0":
        expression = ""

    valid_operators = ("+", "-", "×", "÷")

    if cont in valid_operators and expression[-1] in valid_operators:
        expression = expression[:-1]
    
    expression = expression + str(cont)
    input_text.set(expression)

def clear():
    global expression
    expression = "0"
    input_text.set("0")

def sign():
    global expression
    expression = str(expression)
    expression = list(expression)
    constant_index = len(expression) - 1
    while constant_index >= 0 and expression[constant_index] in "1234567890.":
        constant_index -= 1
    constant_index += 1
    if constant_index > 0 and expression[constant_index - 1] == "-":
        expression.pop(constant_index - 1)
    else:
        expression.insert(constant_index, "-")
    expression = "".join(expression)
    input_text.set(expression)

def percentage():
    global expression
    expression = str(eval(expression))
    expression = str(float(expression) / 100)
    input_text.set(expression)

def square():
    global expression
    expression = str(expression)
    if expression and expression[-1].isdigit():
        expression = expression + "²"
    input_text.set(expression)

def square_root():
    global expression
    expression = str(expression)
    fake_expression = expression
    if expression == "0" or expression == "":
        expression = ""
    elif expression[-1] in "+-×÷":
        fake_expression = fake_expression[:-1]
    else:
        last_num = re.findall(r'\d*\.?\d+', expression)[-1]
        fake_expression = fake_expression.replace(last_num, f"√({last_num})")

    expression = expression + "**(1/2)"
    input_text.set(fake_expression)
     
def cube():
    global expression
    expression = str(expression)
    if expression and expression[-1].isdigit():
        expression = expression + "³"
    input_text.set(expression)

def cube_root():
    global expression
    expression = str(expression)
    fake_expression = expression
    if expression == "0" or expression == "":
        expression = ""
    elif expression[-1] in "+-*/":
        fake_expression = fake_expression[:-1]
    else:
        last_num = re.findall(r'\d*\.?\d+', expression)[-1]
        fake_expression = fake_expression.replace(last_num, f"∛({last_num})")

    expression = expression + "**(1/3)"
    input_text.set(fake_expression)

def delete():
    global expression
    if expression == "0" or 0:
        expression = "0"
    else:
        expression = expression[:-1]
        if expression[:1] == "":
            expression = "0"
    input_text.set(expression)

def calc():
    global expression
    expression = str((expression)).replace("²", "**2")
    expression = str((expression)).replace("³", "**3")
    expression = str((expression)).replace("÷", "/")
    expression = str((expression)).replace("×", "*")
    result = eval(expression)
    input_text.set(result)
    expression = result

input_text = StringVar()

input_frame = Frame(win, width=312, height=100, bd=-20, highlightbackground="black",
                    highlightcolor="black", highlightthickness=2, padx=0, pady=0)
inpu = input_frame

input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 30), width=50, textvariable=input_text,
justify=RIGHT, bd=0, border=0, borderwidth=0, state='disabled',)
input_text.set("0")

input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

buttons_frame = Frame(win, width=236, height=272, padx=0, pady=0, bd=-20)
buttons_frame.pack()

# First row

CA = Button(buttons_frame, text="AC", fg="#eee", width=50, height=50, bd=0, bg="#393940", activebackground="#bbbabf",takefocus=0, focuscolor="", command=lambda: clear()).grid(row=0, column=0, padx=0, pady=0)
negative_positive = Button(buttons_frame, text="-/+", fg="#eee", width=50, height=50, bd=0, bg="#393940", activebackground="#bbbabf",takefocus=0, focuscolor="", command=lambda: sign()).grid(row=0, column=1, padx=0, pady=0, columnspan=1)

percentage_calc = Button(buttons_frame, text="%", fg="#eee", width=50, height=50, bd=0, bg="#393940",activebackground="#bbbabf", takefocus=0, focuscolor="", command=percentage).grid(row=0, column=2, padx=0, pady=0)

divide = Button(buttons_frame, text="÷", width=50, fg="#eee", height=50, bd=0, bg="#ff9f0b", activebackground="#bbbabf",takefocus=0, focuscolor="", command=lambda: click("÷")).grid(row=0, column=3, padx=0, pady=0)

sqr = Button(buttons_frame, text="x²", width=50, fg="#eee", height=50, bd=0, bg="#ff9f0b", activebackground="#bbbabf",takefocus=0, focuscolor="", command=lambda: square()).grid(row=0, column=4, padx=0, pady=0)

# Second row

seven = Button(buttons_frame, text="7", fg="#eee", width=50, height=50, bd=0, bg="#595960", takefocus=0, focuscolor="",activebackground="#bbbabf", borderwidth=0, command=lambda: click(7)).grid(row=1, column=0, padx=0, pady=0)

eight = Button(buttons_frame, text="8", fg="#eee", width=50, height=50, bd=0, bg="#595960", takefocus=0, focuscolor="",activebackground="#bbbabf", borderwidth=0,  command=lambda: click(8)).grid(row=1, column=1, padx=0, pady=0)

nine = Button(buttons_frame, text="9", fg="#eee", width=50, height=50, bd=0, bg="#595960", takefocus=0, focuscolor="",activebackground="#bbbabf", borderwidth=0,  command=lambda: click(9)).grid(row=1, column=2, padx=0, pady=0)

multiply = Button(buttons_frame, text="×", fg="#eee", width=50, height=50, bd=0, bg="#ff9f0b", takefocus=0, focuscolor="",activebackground="#bbbabf", borderwidth=0, command=lambda: click("×")).grid(row=1, column=3, padx=0, pady=0)

squareroot = Button(buttons_frame, text="√ ", width=50, fg="#eee", height=50, bd=0, bg="#ff9f0b", takefocus=0,focuscolor="", activebackground="#bbbabf", command=lambda: square_root()).grid(row=1, column=4, padx=0, pady=0)

# Third row

four = Button(buttons_frame, text="4", fg="#eee", width=50, height=50, bd=0, bg="#595960", takefocus=0,focuscolor="", activebackground="#bbbabf", command=lambda: click(4)).grid(row=2, column=0, padx=0, pady=0)

five = Button(buttons_frame, text="5", fg="#eee", width=50, height=50, bd=0, bg="#595960", takefocus=0,focuscolor="", activebackground="#bbbabf", command=lambda: click(5)).grid(row=2, column=1, padx=0, pady=0)

six = Button(buttons_frame, text="6", fg="#eee", width=50, height=50, bd=0, bg="#595960", takefocus=0,focuscolor="", activebackground="#bbbabf", command=lambda: click(6)).grid(row=2, column=2, padx=0, pady=0)

minus = Button(buttons_frame, text="-", fg="#eee", width=50, height=50, bd=0, bg="#ff9f0b", takefocus=0,focuscolor="", activebackground="#bbbabf", command=lambda: click("-")).grid(row=2, column=3, padx=0, pady=0)

cube_ = Button(buttons_frame, text="x³", fg="#eee", width=50, height=50, bd=0, bg="#ff9f0b", takefocus=0,focuscolor="", activebackground="#bbbabf", command=lambda: cube()).grid(row=2, column=4, padx=0, pady=0)

# Fourth row

one = Button(buttons_frame, text="1", fg="#eee", width=50, height=50, bd=0, bg="#595960", takefocus=0,focuscolor="", activebackground="#bbbabf", command=lambda: click(1)).grid(row=3, column=0, padx=0, pady=0)

two = Button(buttons_frame, text="2", fg="#eee", width=50, height=50, bd=0, bg="#595960", takefocus=0,focuscolor="", activebackground="#bbbabf", command=lambda: click(2)).grid(row=3, column=1, padx=0, pady=0)

three = Button(buttons_frame, text="3", fg="#eee", width=50, height=50, bd=0, bg="#595960", takefocus=0,focuscolor="", activebackground="#bbbabf", command=lambda: click(3)).grid(row=3, column=2, padx=0, pady=0)

plus = Button(buttons_frame, text="+", fg="#eee", width=50, height=50, bd=0, bg="#ff9f0b", takefocus=0,focuscolor="", activebackground="#bbbabf", command=lambda: click("+")).grid(row=3, column=3, padx=0, pady=0)

cuberoot = Button(buttons_frame, text="∛", fg="#eee", width=50, height=50, bd=0, bg="#ff9f0b", takefocus=0,focuscolor="", activebackground="#bbbabf", command=lambda: cube_root()).grid(row=3, column=4, padx=0, pady=0)


# Fifth row

zero = Button(buttons_frame, text="0", fg="#eee", width=50, height=50, bd=0, bg="#595960", takefocus=0, focuscolor="",activebackground="#bbbabf", command=lambda: click(0)).grid(row=4, column=0, columnspan=1, padx=0, pady=0)

decimal = Button(buttons_frame, text=".", fg="#eee", width=50, height=50, bd=0, bg="#595960", takefocus=0,focuscolor="", activebackground="#bbbabf", command=lambda: click(".")).grid(row=4, column=1, padx=0, pady=0)

backspace = Button(buttons_frame, text="⌫", fg="#eee", width=50, height=50, bd=0, bg="#595960", takefocus=0, focuscolor="",activebackground="#bbbabf", command=lambda: delete()).grid(row=4, column=2, columnspan=1, padx=0, pady=0)

equals = Button(buttons_frame, text="=", fg="#eee", width=100, height=50, bd=0, bg="#ff9f0b", takefocus=0, focuscolor="",activebackground="#bbbabf", command=lambda: calc()).grid(row=4, column=3, padx=0, pady=0, columnspan=2)

win.mainloop()