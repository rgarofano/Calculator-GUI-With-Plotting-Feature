# Graphing Calculator
# Ryan Garofano
# June 27th, 2020

""" USER INFORMATION
	
	BTN Functions:

	0,1,2,3,4,5,6,7,8,9 -> Inputs number into calculator
	+ -> addition operator
	- -> subtraction operator
	* -> multiplication operator
	/ -> division operator
	^ -> exponent operator
	() -> inputs brackets into the calculator (open bracket on first click, closed on second)
	C -> clears the console
	x -> inputs a variable x into the console (used for plotting)
	P -> plots function (x variable must be present to plot)
		-> proper syntax must be used for plot to be created
		-> Follow MATLAB syntax for example 2x must be inputted as 2*x
	= -> evaluates expression
"""

# ~~~~~ Imports ~~~~~ #

import tkinter as tk

from tkinter import *
import numpy
import matplotlib.pyplot as plot

# ~~~~~ Constants ~~~~~ #

OPEN_BRACKET = 0
CLOSED_BRACKET = 1
CLEAR_CONSOLE = ""
BTN_0_TEXT = "0"
BTN_0_ROW = 4
BTN_0_COL = 0
BTN_1_TEXT = "1"
BTN_1_ROW = 3
BTN_1_COL = 0
BTN_2_TEXT = "2"
BTN_2_ROW = 3
BTN_2_COL = 1
BTN_3_TEXT = "3"
BTN_3_ROW = 3
BTN_3_COL = 2
BTN_4_TEXT = "4"
BTN_4_ROW = 2
BTN_4_COL = 0
BTN_5_TEXT = "5"
BTN_5_ROW = 2
BTN_5_COL = 1
BTN_6_TEXT = "6"
BTN_6_ROW = 2
BTN_6_COL = 2
BTN_7_TEXT = "7"
BTN_7_ROW = 1
BTN_7_COL = 0
BTN_8_TEXT = "8"
BTN_8_ROW = 1
BTN_8_COL = 1
BTN_9_TEXT = "9"
BTN_9_ROW = 1
BTN_9_COL = 2
BTN_ADD_TEXT = "+"
BTN_ADD_ROW = 1
BTN_ADD_COL = 3
BTN_SUB_TEXT = "-"
BTN_SUB_ROW = 2
BTN_SUB_COL = 3
BTN_MULT_TEXT = "*"
BTN_MULT_ROW = 3
BTN_MULT_COL = 3
BTN_DIV_TEXT = "/"
BTN_DIV_ROW = 4
BTN_DIV_COL = 3
BTN_EXP_TEXT = "^"
BTN_EXP_ROW = 4
BTN_EXP_COL = 1
BTN_BRACKETS_TXT = "()"
BTN_BRACKETS_ROW = 5
BTN_BRACKETS_COL = 0
BTN_VAR_TXT = "x"
BTN_VAR_ROW = 4
BTN_VAR_COL = 2
BTN_EQUAL_TXT = "="
BTN_EQUAL_ROW = 5
BTN_EQUAL_COL = 3
BTN_CLEAR_TXT = "C"
BTN_CLEAR_ROW = 5
BTN_CLEAR_COL = 1
BTN_PLOT_TXT = "P"
BTN_PLOT_ROW = 5
BTN_PLOT_COL = 2
NUMBER_BTN_COLOR = "powder blue"
OPERATOR_BTN_COLOR = "light green"
PLOT_BTN_COLOR = "purple"


# ~~~~~ Helper Functions ~~~~~#


def add_text_to_console(console_text, text_to_append):
    updated_text = console_text.get() + text_to_append
    console_text.set(updated_text)


def evaluate_input(console_text):
    try:
        evaluated_expression = str(eval(console_text.get()))

    except SyntaxError:
        clear(console_text)
        add_text_to_console(console_text, "ERROR")
        return

    console_text.set(evaluated_expression)


def clear(console_text):
    console_text.set(CLEAR_CONSOLE)


def add_brackets(console_text):
    global bracket_type

    if bracket_type == OPEN_BRACKET:
        add_text_to_console(console_text, "(")
        bracket_type = CLOSED_BRACKET

    elif bracket_type == CLOSED_BRACKET:
        add_text_to_console(console_text, ")")
        bracket_type = OPEN_BRACKET

    else:
        raise ValueError("Illegal bracket type specified")


def function_from_string(func_str):
    return lambda x: eval(func_str)


def create_plot(console_text):
    console_input = console_text.get()
    func_str = console_input.replace("^", "**")
    # create vectors
    x_values = numpy.linspace(1, 100, 1000)
    function = function_from_string(func_str)

    try:
        y_values = [function(x) for x in x_values]

    except SyntaxError:
        clear(console_text)
        add_text_to_console(console_text, "ERROR")
        return

    # create plot
    plot.plot(x_values, y_values)

    # format plot figure window and display the figure
    plot.xlabel("x-axis")
    plot.ylabel("y-axis")
    plot.title("y = " + console_input)
    plot.grid()
    plot.legend()
    plot.show()


def create_button(button_text, color, on_click_function, row, col):
    Button(text=button_text, font=("arial", 12, "bold"), padx=40, pady=20, bg=color, bd=5,
           command=on_click_function) \
        .grid(row=row, column=col)


def add_number_buttons(console_text):
    create_button(BTN_0_TEXT, NUMBER_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_0_TEXT),
                  BTN_0_ROW, BTN_0_COL)
    create_button(BTN_1_TEXT, NUMBER_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_1_TEXT),
                  BTN_1_ROW, BTN_1_COL)
    create_button(BTN_2_TEXT, NUMBER_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_2_TEXT),
                  BTN_2_ROW, BTN_2_COL)
    create_button(BTN_3_TEXT, NUMBER_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_3_TEXT),
                  BTN_3_ROW, BTN_3_COL)
    create_button(BTN_4_TEXT, NUMBER_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_4_TEXT),
                  BTN_4_ROW, BTN_4_COL)
    create_button(BTN_5_TEXT, NUMBER_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_5_TEXT),
                  BTN_5_ROW, BTN_5_COL)
    create_button(BTN_6_TEXT, NUMBER_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_6_TEXT),
                  BTN_6_ROW, BTN_6_COL)
    create_button(BTN_7_TEXT, NUMBER_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_7_TEXT),
                  BTN_7_ROW, BTN_7_COL)
    create_button(BTN_8_TEXT, NUMBER_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_8_TEXT),
                  BTN_8_ROW, BTN_8_COL)
    create_button(BTN_9_TEXT, NUMBER_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_9_TEXT),
                  BTN_9_ROW, BTN_9_COL)


def add_operator_buttons(console_text):
    create_button(BTN_ADD_TEXT, OPERATOR_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_ADD_TEXT),
                  BTN_ADD_ROW, BTN_ADD_COL)
    create_button(BTN_SUB_TEXT, OPERATOR_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_SUB_TEXT),
                  BTN_SUB_ROW, BTN_SUB_COL)
    create_button(BTN_MULT_TEXT, OPERATOR_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_MULT_TEXT),
                  BTN_MULT_ROW, BTN_MULT_COL)
    create_button(BTN_DIV_TEXT, OPERATOR_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_DIV_TEXT),
                  BTN_DIV_ROW, BTN_DIV_COL)
    create_button(BTN_EXP_TEXT, OPERATOR_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_EXP_TEXT),
                  BTN_EXP_ROW, BTN_EXP_COL)
    create_button(BTN_EQUAL_TXT, OPERATOR_BTN_COLOR, lambda: evaluate_input(console_text),
                  BTN_EQUAL_ROW, BTN_EQUAL_COL)


def add_brackets_button(console_text):
    create_button(BTN_BRACKETS_TXT, OPERATOR_BTN_COLOR, lambda: add_brackets(console_text),
                  BTN_BRACKETS_ROW, BTN_BRACKETS_COL)


def add_plot_buttons(console_text):
    create_button(BTN_VAR_TXT, PLOT_BTN_COLOR, lambda: add_text_to_console(console_text, BTN_VAR_TXT),
                  BTN_VAR_ROW, BTN_VAR_COL)
    create_button(BTN_PLOT_TXT, PLOT_BTN_COLOR, lambda: create_plot(console_text),
                  BTN_PLOT_ROW, BTN_PLOT_COL)


def add_clear_button(console_text):
    create_button(BTN_CLEAR_TXT, OPERATOR_BTN_COLOR, lambda: clear(console_text),
                  BTN_CLEAR_ROW, BTN_CLEAR_COL)


def initialize_gui(calculator_gui):
    calculator_gui.title("Graphing Calculator")

    console_text = tk.StringVar(master=calculator_gui, value=CLEAR_CONSOLE)
    console = Entry(calculator_gui, width=50, borderwidth=5, bg="grey", textvariable=console_text)
    console.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    add_number_buttons(console_text)
    add_operator_buttons(console_text)
    add_brackets_button(console_text)
    add_plot_buttons(console_text)
    add_clear_button(console_text)


# ~~~~~ Main Function ~~~~~#


def main():
    calculator = tk.Tk()
    initialize_gui(calculator)
    calculator.mainloop()


# ~~~~~ Run Program ~~~~~#

bracket_type = OPEN_BRACKET
main()
