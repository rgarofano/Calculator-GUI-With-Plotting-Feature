# Calculator
# Ryan Garofano
# June 27th, 2020

""" USER INFORMATION
	
	Button Functions:

	0,1,2,3,4,5,6,7,8,9 -> Inputs number into calculator
	+ -> addition operator
	- -> subtraction operator
	* -> multiplication operator
	/ -> division operatorr
	^ -> exponent operator (will appear as ** in console)
	() -> inputs brackets into the calculator (open bracket on first click, closed on second)
	C -> clears the console
	x -> inputs a variable x into the console (used for plotting)
	P -> plots function (x variable must be present to plot)
		-> proper syntax must be used for plot to be created
		-> Follow MATLAB syntax for example 2x must be inputted as 2*x
	= -> evaluates expression
"""
#~~~~~ Imports ~~~~~#
from tkinter import *
import numpy
import matplotlib.pyplot as matlab
import math
#~~~~~ Functions ~~~~~#

def click_button(number):

	# update display with the user input
	global operation
	operation = operation + str(number)
	user_input.set(operation)


def equals():

	# evaluate the operation
	global operation
	result = str(eval(operation))
	user_input.set(result)

	operation = ""


def clear():

	# clear screen
	global operation
	operation = ""
	user_input.set(operation)


def add_brackets():

	global operation
	global switcher

	# create a switching algorithm so that the brackets can work as intended
	if switcher == 0:

		operation = operation + "("
		switcher = 1

	elif switcher == 1:

		operation = operation + ")"
		switcher = 0

	user_input.set(operation)

def create_plot():

	global operation

	# create vectors
	x = numpy.linspace(1,100,1000)
	y = eval(bytes([ord(p) for p in operation]))

	# plot function
	matlab.plot(x,y)

	# format plot figure window and display the figure
	matlab.xlabel('x-axis')
	matlab.ylabel('y-axis')
	matlab.title('Plot from x = 0 to 100')
	matlab.grid()
	matlab.legend()
	matlab.show()


#~~~~~ Main Code ~~~~~#

# initialize GUI
calculator = Tk()

# provide a title for the window
calculator.title("Calculator")

# initialize a string variable for storing button information
user_input = StringVar()
operation = ""

# initialize switching variable (see add_brackets() definition)
switcher = 0

# Create calculator "console screen"
console = Entry(calculator, width =50, borderwidth = 5, bg = "grey", textvariable = user_input)
console.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

# Create number buttons and assign functions to them
Button_0 = Button(text = "0", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "powder blue", bd = 5, command = lambda: click_button(0)).grid(row=4,column=0)
Button_1 = Button(text = "1", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "powder blue", bd = 5, command = lambda: click_button(1)).grid(row=3,column=0)
Button_2 = Button(text = "2", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "powder blue", bd = 5, command = lambda: click_button(2)).grid(row=3,column=1)
Button_3 = Button(text = "3", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "powder blue", bd = 5, command = lambda: click_button(3)).grid(row=3,column=2)
Button_4 = Button(text = "4", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "powder blue", bd = 5, command = lambda: click_button(4)).grid(row=2,column=0)
Button_5 = Button(text = "5", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "powder blue", bd = 5, command = lambda: click_button(5)).grid(row=2,column=1)
Button_6 = Button(text = "6", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "powder blue", bd = 5, command = lambda: click_button(6)).grid(row=2,column=2)
Button_7 = Button(text = "7", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "powder blue", bd = 5, command = lambda: click_button(7)).grid(row=1,column=0)
Button_8 = Button(text = "8", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "powder blue", bd = 5, command = lambda: click_button(8)).grid(row=1,column=1)
Button_9 = Button(text = "9", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "powder blue", bd = 5, command = lambda: click_button(9)).grid(row=1,column=2)

# Create operator buttons and assign them functions
Button_add = Button(text = "+", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "light green", bd = 5, command = lambda: click_button("+")).grid(row=1,column=3)
Button_sub = Button(text = "-", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "light green", bd = 5, command = lambda: click_button("-")).grid(row=2,column=3)
Button_multiply = Button(text = "*", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "light green", bd = 5, command = lambda: click_button("*")).grid(row=3,column=3)
Button_divide = Button(text = "/", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "light green", bd = 5, command = lambda: click_button("/")).grid(row=4,column=3)
Button_exponent = Button(text = "^", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "light green", bd = 5, command = lambda: click_button("**")).grid(row=4,column=1)
Button_brackets = Button(text = "()", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "light green", bd = 5, command = lambda: add_brackets()).grid(row=5,column=0)
Button_variable = Button(text = "x", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "light green", bd = 5, command = lambda: click_button("x")).grid(row=4,column=2)
Button_equal = Button(text = "=", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "light green", bd = 5, command = lambda: equals()).grid(row=5,column=3)
Button_clear = Button(text = "C", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "light green", bd = 5, command = lambda: clear()).grid(row=5,column=1)
Button_plot = Button(text = "P", font = ("arial",12,"bold"), padx = 40, pady = 20, bg = "light green", bd = 5, command = lambda: create_plot()).grid(row=5,column=2)

calculator.mainloop()