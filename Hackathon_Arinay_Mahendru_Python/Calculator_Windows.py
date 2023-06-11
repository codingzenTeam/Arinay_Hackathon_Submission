#Please only run this file on a windows machine

#-----------------------#

from tkinter import *
import tkinter as tk
import re
import pywhatkit as kt #Please install pywhatkit module
import urllib.parse

#-----------------------#

splash = tk.Tk()
splash.geometry("420x690")
splash.overrideredirect(True)
splash.geometry("420x690")
splash.configure(bg="#595960")
bgimg= tk.PhotoImage(file = "Splash_Screen_Windows.png")
limg= Label(splash, i=bgimg)
limg.pack()

#-----------------------# Initialising of main calculator window

def main():
    splash.destroy()
    main_calc = Tk()
    main_calc.geometry("420x690")
    main_calc.title("Calculator")
    img = PhotoImage(file = "icon.png")
    main_calc.iconphoto(False,img)
    main_calc.attributes('-alpha', 0.95)
    main_calc.resizable(0,0)
    main_calc.configure(bg="#393940")

    global expression        
    expression = "0"

    #-----------------------# Functions for main calculator :

    def click(cont): # Deals with clicks of buttons
        global expression
        expression = str(expression)
        if expression == 0 or expression == "0":
            expression = ""

        valid_operators = ("+", "-", "×", "÷")

        if cont in valid_operators and expression[-1] in valid_operators:
            expression = expression[:-1]
        
        expression = expression + str(cont)
        input_var.set(expression)

    def clear(): #Deals with the click of the clear button
        global expression
        expression = "0"
        input_var.set("0")

    def sign(): #Changes the sign of the last number in the expression
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
        input_var.set(expression)

    def percentage(): # Gets the percentage of the result of the expression
        global expression
        expression = str((expression)).replace("²", "**2")
        expression = str((expression)).replace("³", "**3")
        expression = str((expression)).replace("÷", "/")
        expression = str((expression)).replace("×", "*")
        expression = str(expression)
        expression = str(eval(expression))
        expression = str(float(expression) / 100)
        input_var.set(expression)

    def square(): # Squares the last number of the expression
        global expression
        expression = str(expression)
        if expression and expression[-1].isdigit():
            expression = expression + "²"
        input_var.set(expression)

    def square_root(): # Finds the square root of the last number in the expression

        global expression
        expression = str(expression)
        fake_expression = expression
        expression = str(expression)
        if expression == "0" or expression == "":
            expression = ""
        elif expression[-1] in "+-×÷":
            fake_expression = fake_expression[:-1]
        else:
            last_num = re.findall(r'\d*\.?\d+', expression)[-1]
            fake_expression = fake_expression.replace(last_num, f"√({last_num})")

        expression = expression + "**(1/2)"
        input_var.set(fake_expression)
         
    def cube(): #Cubes the last number of the expression
        global expression
        expression = str(expression)
        if expression and expression[-1].isdigit():
            expression = expression + "³"
        input_var.set(expression)

    def cube_root(): #Finds the cube root of the last number in the expression
        global expression
        expression = str(expression)
        fake_expression = expression
        expression = str(expression)
        if expression == "0" or expression == "":
            expression = ""
        elif expression[-1] in "+-*/":
            fake_expression = fake_expression[:-1]
        else:
            last_num = re.findall(r'\d*\.?\d+', expression)[-1]
            fake_expression = fake_expression.replace(last_num, f"∛({last_num})")

        expression = expression + "**(1/3)"
        input_var.set(fake_expression)

    def delete(): # Deals with the backspace button
        global expression
        expression = str(expression)
        if expression == "0" or 0:
            expression = "0"
        else:
            expression = expression[:-1]
            if expression[:1] == "":
                expression = "0"
        input_var.set(expression)

    def calc(): # Calculates the expression
        global expression
        expression = str((expression)).replace("²", "**2")
        expression = str((expression)).replace("³", "**3")
        expression = str((expression)).replace("÷", "/")
        expression = str((expression)).replace("×", "*")
        result = eval(expression)
        input_var.set(result)
        expression = result
    
    #-----------------------# Input Field code :
        
    input_var = StringVar()

    input_frame = Frame(main_calc, width=312, height=200, bd=-20, highlightbackground="black",highlightcolor="black", highlightthickness=2, padx=10, pady=0,background="#393940",bg = "#393940")

    input_frame.pack(side=TOP)

    input_field = Entry(input_frame, font=('arial', 30), width=420, textvariable=input_var,
    justify=RIGHT, bd=0, border=0, borderwidth=0,state = 'disabled')
    input_field.configure(disabledbackground="#595960",disabledforeground = "#eee")
    input_var.set("0")

    input_field.grid(row=0, column=0)
    input_field.pack(ipady=10)
    input_var.set(expression)

    buttons_frame = tk.Frame(main_calc, width=236, height=272, padx=0, pady=0, bd=-20)
    buttons_frame.pack()

    #-----------------------# Buttons :

    # First row

    CA = Button(buttons_frame, text="AC", fg="#eee", width=6, height=3, bd=0, bg="#393940", activebackground="#bbbabf", takefocus=0, command=lambda: clear()).grid(row=0, column=0, padx=0, pady=0)

    negative_positive = Button(buttons_frame, text="-/+", fg="#eee", width=6, height=3, bd=0, bg="#393940", activebackground="#bbbabf", takefocus=0, command=lambda: sign()).grid(row=0, column=1, padx=0, pady=0)

    percentage_calc = Button(buttons_frame, text="%", fg="#eee", width=6, height=3, bd=0, bg="#393940", activebackground="#bbbabf", takefocus=0, command=percentage).grid(row=0, column=2, padx=0, pady=0)

    divide = Button(buttons_frame, text="÷", width=6, fg="#eee", height=3, bd=0, bg="#ff9f0b", activebackground="#bbbabf", takefocus=0, command=lambda: click("÷")).grid(row=0, column=3, padx=0, pady=0)

    sqr = Button(buttons_frame, text="x²", width=6, fg="#eee", height=3, bd=0, bg="#ff9f0b", activebackground="#bbbabf", takefocus=0, command=lambda: square()).grid(row=0, column=4, padx=0, pady=0)

    # Second row

    seven = Button(buttons_frame, text="7", fg="#eee", width=6, height=3, bd=0, bg="#595960", takefocus=0, activebackground="#bbbabf", borderwidth=0, command=lambda: click(7)).grid(row=1, column=0, padx=0, pady=0)

    eight = Button(buttons_frame, text="8", fg="#eee", width=6, height=3, bd=0, bg="#595960", takefocus=0, activebackground="#bbbabf", borderwidth=0, command=lambda: click(8)).grid(row=1, column=1, padx=0, pady=0)

    nine = Button(buttons_frame, text="9", fg="#eee", width=6, height=3, bd=0, bg="#595960", takefocus=0, activebackground="#bbbabf", borderwidth=0, command=lambda: click(9)).grid(row=1, column=2, padx=0, pady=0)

    multiply = Button(buttons_frame, text="×", fg="#eee", width=6, height=3, bd=0, bg="#ff9f0b", takefocus=0, activebackground="#bbbabf", borderwidth=0, command=lambda: click("×")).grid(row=1, column=3, padx=0, pady=0)

    squareroot = Button(buttons_frame, text="√ ", width=6, fg="#eee", height=3, bd=0, bg="#ff9f0b", takefocus=0, activebackground="#bbbabf", command=lambda: square_root()).grid(row=1, column=4, padx=0, pady=0)

    # Third row
    four = Button(buttons_frame, text="4", fg="#eee", width=6, height=3, bd=0, bg="#595960", takefocus=0, activebackground="#bbbabf", command=lambda: click(4)).grid(row=2, column=0, padx=0, pady=0)

    five = Button(buttons_frame, text="5", fg="#eee", width=6, height=3, bd=0, bg="#595960", takefocus=0, activebackground="#bbbabf", command=lambda: click(5)).grid(row=2, column=1, padx=0, pady=0)

    six = Button(buttons_frame, text="6", fg="#eee", width=6, height=3, bd=0, bg="#595960", takefocus=0, activebackground="#bbbabf", command=lambda: click(6)).grid(row=2, column=2, padx=0, pady=0)

    minus = Button(buttons_frame, text="-", fg="#eee", width=6, height=3, bd=0, bg="#ff9f0b", takefocus=0, activebackground="#bbbabf", command=lambda: click("-")).grid(row=2, column=3, padx=0, pady=0)

    cube_ = Button(buttons_frame, text="x³", fg="#eee", width=6, height=3, bd=0, bg="#ff9f0b", takefocus=0, activebackground="#bbbabf", command=lambda: cube()).grid(row=2, column=4, padx=0, pady=0)

    # Fourth row

    one = Button(buttons_frame, text="1", fg="#eee", width=6, height=3, bd=0, bg="#595960", takefocus=0, activebackground="#bbbabf", command=lambda: click(1)).grid(row=3, column=0, padx=0, pady=0)

    two = Button(buttons_frame, text="2", fg="#eee", width=6, height=3, bd=0, bg="#595960", takefocus=0, activebackground="#bbbabf", command=lambda: click(2)).grid(row=3, column=1, padx=0, pady=0)

    three = Button(buttons_frame, text="3", fg="#eee", width=6, height=3, bd=0, bg="#595960", takefocus=0, activebackground="#bbbabf", command=lambda: click(3)).grid(row=3, column=2, padx=0, pady=0)

    plus = Button(buttons_frame, text="+", fg="#eee", width=6, height=3, bd=0, bg="#ff9f0b", takefocus=0, activebackground="#bbbabf", command=lambda: click("+")).grid(row=3, column=3, padx=0, pady=0)

    cuberoot = Button(buttons_frame, text="∛", fg="#eee", width=6, height=3, bd=0, bg="#ff9f0b", takefocus=0, activebackground="#bbbabf", command=lambda: cube_root()).grid(row=3, column=4, padx=0, pady=0)

    # Fifth row

    zero = Button(buttons_frame, text="0", fg="#eee", width=6, height=3, bd=0, bg="#595960", takefocus=0, activebackground="#bbbabf", command=lambda: click(0)).grid(row=4, column=0, padx=0, pady=0)

    decimal = Button(buttons_frame, text=".", fg="#eee", width=6, height=3, bd=0, bg="#595960", takefocus=0, activebackground="#bbbabf", command=lambda: click(".")).grid(row=4, column=1, padx=0, pady=0)

    backspace = Button(buttons_frame, text="⌫", fg="#eee", width=6, height=3, bd=0, bg="#595960", takefocus=0, activebackground="#bbbabf", command=lambda: delete()).grid(row=4, column=2, padx=0, pady=0)

    equals = Button(buttons_frame, text="=", fg="#eee", width=6, height=3, bd=0, bg="#ff9f0b", takefocus=0, activebackground="#bbbabf", command=lambda: calc()).grid(row=4, column=3, padx=0, pady=0)
    
    problem = Button(buttons_frame, text="Prob", fg="#eee", width=6, height=3, bd=0, bg="#ff9f0b", takefocus=0,activebackground="#bbbabf", command=lambda: problem_calc()).grid(row=4, column=4, padx=0, pady=0)

    #-----------------------# Initialsing of the problem calculator:

    def problem_calc():
        prob_calc = Toplevel(main_calc)
        prob_calc.title("Problem Calculator")
        prob_calc.geometry("660x720")
        prob_calc.attributes('-alpha', 0.95)
        prob_calc.configure(bg="#595960")
        prob_calc.iconphoto(False,img)
        global  prob_expression
        prob_expression = "0"

        #-----------------------# Function for problem calculator :

        def prob_clear(): #Clears the expression

            global prob_expression
            prob_expression = "0"
            prob_input_var.set("0")

        def prob_click(cont): # Deals with clicks of buttons

            global prob_expression
            prob_expression = str(prob_expression)
            if prob_expression == 0 or prob_expression == "0":
                prob_expression = ""

            valid_operators = ("+", "-", "×", "÷")

            if cont in valid_operators and prob_expression[-1] in valid_operators:
                prob_expression = prob_expression[:-1]
            prob_expression = prob_expression + str(cont)
            prob_input_var.set(prob_expression)

        def prob_sign(): # Chnages the sign of the last number of the expression

            global prob_expression
            prob_expression = str(prob_expression)
            prob_expression = list(prob_expression)
            prob_constant_index = len(prob_expression) - 1
            while prob_constant_index >= 0 and prob_expression[prob_constant_index] in "1234567890.":
                prob_constant_index -= 1
            prob_constant_index += 1
            if prob_constant_index > 0 and prob_expression[prob_constant_index - 1] == "-":
                expression.pop(prob_constant_index - 1)
            else:
                prob_expression.insert(prob_constant_index, "-")
                prob_expression = "".join(prob_expression)
                prob_input_var.set(prob_expression)

        def percentage(): # Gets the percentage of the result of the expression

            global prob_expression
            prob_expression = str(eval(prob_expression))
            prob_expression = str(float(prob_expression) / 100)
            prob_input_var.set(prob_expression)

        def prob_square_root(): # Gets the square root of the last number in the expression

            global prob_expression
            prob_expression = str(prob_expression)
            prob_expression = str(prob_expression)
            if prob_expression == "0" or prob_expression == "":
                prob_expression = ""
                prob_expression = str(prob_expression)
            elif expression[-1] in "+-×÷=":
                prob_expression = str(prob_expression)
                prob_expression = prob_expression[:-1]
            else:
                last_num = re.findall(r'\d*\.?\d+|\D$', prob_expression)[-1]
                prob_expression = prob_expression.replace(last_num, f"√({last_num})")
                prob_input_var.set(prob_expression)

        def prob_cube_root(): # Gets the cube root of the last number in the expression

            global prob_expression
            prob_expression = str(prob_expression)
            prob_expression = prob_expression + "^(1/3)"
            prob_input_var.set(prob_expression)

        def delete(): # Deals with the backspace button

            global prob_expression
            if prob_expression == "0" or 0:
                prob_expression = "0"
            else:
                prob_expression = prob_expression[:-1]
            if prob_expression[:1] == "":
                prob_expression = "0"
            prob_input_var.set(prob_expression)

        def prob_search(): #Searches the exprssion on google

            global prob_expression
            prob_expression = str((prob_expression)).replace("𝑥", "x")         
            prob_expression_parsed = urllib.parse.quote(prob_expression)
            kt.search(prob_expression_parsed)
        
        def update_expression(event):
            global prob_expression
            prob_expression = prob_input_field.get()

        #-----------------------# Code for the label and input field:

        Label(prob_calc,text ="Enter your problem statement",background="#595960",fg = "white").pack()
        prob_input_var = StringVar()

        prob_input_frame = Frame(prob_calc, width=312, height=100, bd=-20, highlightbackground="#595960",
                            highlightcolor="black", highlightthickness=2, padx=0, pady=0)
        prob_input_field = prob_input_frame

        prob_input_frame.pack(side=TOP)

        prob_input_field = Entry(prob_input_frame, font=('arial', 30), width=312, textvariable=prob_input_var,justify=RIGHT, bd=0, border=0, borderwidth=0,background="#595960",fg="white",foreground="white")

        prob_input_field.grid(row=0, column=0)
        prob_input_field.pack(ipady=10)

        prob_input_var.set("0")

        prob_input_field.bind('<KeyRelease>', update_expression)

        #-----------------------# Buttons:

        prob_buttons_frame = Frame(prob_calc, width=236, height=272, padx=0, pady=0, bd=-20)
        prob_buttons_frame.pack()

        # First row

        prob_AC = Button(prob_buttons_frame, text="AC", fg="#eee",  width=8, height = 3, bd=0, bg="#393940", activebackground="#bbbabf", takefocus=0,   command=lambda: prob_clear()).grid(row=0, column=2, padx=0, pady=0)

        prob_negative_positive = Button(prob_buttons_frame, text="-/+", fg="#eee",  width=8, height = 3, bd=0, bg="#393940", activebackground="#bbbabf", takefocus=0,   command=lambda: prob_sign()).grid(row=0, column=3, padx=0, pady=0)

        prob_percentage_calc = Button(prob_buttons_frame, text="%", fg="#eee",  width=8, height = 3, bd=0, bg="#393940", activebackground="#bbbabf", takefocus=0,   command=percentage).grid(row=0, column=4, padx=0, pady=0)

        prob_bracket_left = Button(prob_buttons_frame, text="(",  width=8, fg="#eee", height = 3, bd=0, bg="#ff9f0b", activebackground="#bbbabf", takefocus=0,   command=lambda: prob_click("(")).grid(row=0, column=0, padx=0, pady=0)

        prob_bracket_right = Button(prob_buttons_frame, text=")",  width=8, fg="#eee", height = 3, bd=0, bg="#ff9f0b", activebackground="#bbbabf", takefocus=0,   command=lambda: prob_click(")")).grid(row=0, column=1, padx=0, pady=0)

        prob_divide = Button(prob_buttons_frame, text="÷",  width=8, fg="#eee", height = 3, bd=0, bg="#ff9f0b", activebackground="#bbbabf", takefocus=0,   command=lambda: prob_click("÷")).grid(row=0, column=5, padx=0, pady=0)

        # Second row
        prob_pi = Button(prob_buttons_frame, text="π", fg="#eee",  width=8, height = 3, bd=0, bg="#ff9f0b", takefocus=0,   activebackground="#bbbabf", borderwidth=0, command=lambda: prob_click(3.14)).grid(row=1, column=0, padx=0, pady=0)

        prob_sqr = Button(prob_buttons_frame, text="x²",  width=8, fg="#eee", height = 3, bd=0, bg="#ff9f0b", activebackground="#bbbabf", takefocus=0,   command=lambda: prob_click("^2")).grid(row=1, column=1, padx=0, pady=0)

        prob_seven = Button(prob_buttons_frame, text="7", fg="#eee",  width=8, height = 3, bd=0, bg="#595960", takefocus=0,   activebackground="#bbbabf", borderwidth=0, command=lambda: prob_click(7)).grid(row=1, column=2, padx=0, pady=0)

        prob_eight = Button(prob_buttons_frame, text="8", fg="#eee",  width=8, height = 3, bd=0, bg="#595960", takefocus=0,   activebackground="#bbbabf", borderwidth=0, command=lambda: prob_click(8)).grid(row=1, column=3, padx=0, pady=0)

        prob_nine = Button(prob_buttons_frame, text="9", fg="#eee",  width=8, height = 3, bd=0, bg="#595960", takefocus=0,   activebackground="#bbbabf", borderwidth=0, command=lambda: prob_click(9)).grid(row=1, column=4, padx=0, pady=0)

        prob_multiply = Button(prob_buttons_frame, text="×", fg="#eee",  width=8, height = 3, bd=0, bg="#ff9f0b", takefocus=0,   activebackground="#bbbabf", borderwidth=0, command=lambda: prob_click("×")).grid(row=1, column=5, padx=0, pady=0)

        # Third row
        prob_squareroot = Button(prob_buttons_frame, text="√ ",  width=8, fg="#eee", height = 3, bd=0, bg="#ff9f0b", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_square_root()).grid(row=2, column=1, padx=0, pady=0)

        prob_raised_to_power = Button(prob_buttons_frame, text="xʸ",  width=8, fg="#eee", height = 3, bd=0, bg="#ff9f0b", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click("^")).grid(row=2, column=0, padx=0, pady=0)

        prob_four = Button(prob_buttons_frame, text="4", fg="#eee",  width=8, height = 3, bd=0, bg="#595960", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click(4)).grid(row=2, column=2, padx=0, pady=0)

        prob_five = Button(prob_buttons_frame, text="5", fg="#eee",  width=8, height = 3, bd=0, bg="#595960", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click(5)).grid(row=2, column=3, padx=0, pady=0)

        prob_six = Button(prob_buttons_frame, text="6", fg="#eee",  width=8, height = 3, bd=0, bg="#595960", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click(6)).grid(row=2, column=4, padx=0, pady=0)

        prob_minus = Button(prob_buttons_frame, text="-", fg="#eee",  width=8, height = 3, bd=0, bg="#ff9f0b", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click("-")).grid(row=2, column=5, padx=0, pady=0)

        # Fourth row
        prob_cube_ = Button(prob_buttons_frame, text="x³", fg="#eee",  width=8, height = 3, bd=0, bg="#ff9f0b", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click("^³")).grid(row=3, column=1, padx=0, pady=0)

        prob_x = Button(prob_buttons_frame, text="𝑥", fg="#eee",  width=8, height = 3, bd=0, bg="#ff9f0b", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click("𝑥")).grid(row=3, column=0, padx=0, pady=0)

        prob_one = Button(prob_buttons_frame, text="1", fg="#eee",  width=8, height = 3, bd=0, bg="#595960", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click(1)).grid(row=3, column=2, padx=0, pady=0)

        prob_two = Button(prob_buttons_frame, text="2", fg="#eee",  width=8, height = 3, bd=0, bg="#595960", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click(2)).grid(row=3, column=3, padx=0, pady=0)

        prob_three = Button(prob_buttons_frame, text="3", fg="#eee",  width=8, height = 3, bd=0, bg="#595960", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click(3)).grid(row=3, column=4, padx=0, pady=0)

        prob_plus = Button(prob_buttons_frame, text="+", fg="#eee",  width=8, height = 3, bd=0, bg="#ff9f0b", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click("+")).grid(row=3, column=5, padx=0, pady=0)

        # Fifth row
        prob_isequalto = Button(prob_buttons_frame, text="=", fg="#eee",  width=8, height = 3, bd=0, bg="#ff9f0b", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click("=")).grid(row=4, column=0, padx=0, pady=0)

        prob_cuberoot = Button(prob_buttons_frame, text="∛", fg="#eee",  width=8, height = 3, bd=0, bg="#ff9f0b", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_cube_root()).grid(row=4, column=1, padx=0, pady=0)

        prob_zero = Button(prob_buttons_frame, text="0", fg="#eee",  width=8, height = 3, bd=0, bg="#595960", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click(0)).grid(row=4, column=2, padx=0, pady=0)

        prob_decimal = Button(prob_buttons_frame, text=".", fg="#eee",  width=8, height = 3, bd=0, bg="#595960", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_click(".")).grid(row=4, column=3, padx=0, pady=0)

        prob_backspace = Button(prob_buttons_frame, text="⌫", fg="#eee",  width=8, height = 3, bd=0, bg="#595960", takefocus=0,   activebackground="#bbbabf", command=lambda: delete()).grid(row=4, column=4, padx=0, pady=0)

        prob_calc = Button(prob_buttons_frame, text="Search!", fg="#eee",  width=8, height = 3, bd=0, bg="#ff9f0b", takefocus=0,   activebackground="#bbbabf", command=lambda: prob_search()).grid(row=4, column=5, padx=0, pady=0)

#-----------------------------------------------------------------# Code for calling the main function which destroys the splash window and initialises the main calculator window

splash.after(3000,main)
splash.mainloop()