from tkinter import *
from tkinter import ttk 
import tkinter as tk
import random
import time
import turtle

##### numbers and operators to be used in generating equations
operand_one = range(50)
operand_two = range(50)
operators = ["+", "-", "X", "/"]

#######





def clear_text():
    input.delete(0, END)

def switch_off():
    validate_button["state"] = "disabled"
    
def switch_on():
    validate_button["state"] = "normal"

def update_progress(value):
    progress_bar["value"] = value
    window.update()



def internal_equation_solver():

    first1 = first
    second2 = second
    operator1 = operator
    
    if operator1 == "+":
        ans = first1+second2
    elif operator1 == "-":
        ans = first1-second2
    elif operator1 == "X":
        ans = first1*second2
    else:
        ans = first1//second2
    return ans

bg_color = "black"
def validate_function():
    ans = internal_equation_solver()
    global bg_color
    if str(ans) == str(input1.get()):
        final_ans = "Good"
        print(ans)
        print(input1.get())
        if bg_color == "black":
            bg_color = "blue"
        else:
            bg_color = "black"
        success_or_not_frontend.config(text = final_ans, fg='lightgreen', bg = bg_color)
    else:
        final_ans = "A Not Good"
        print(ans)
        print(input1.get())
        success_or_not_frontend.config(text = final_ans, fg = "red")
    switch_off()

#####this function generates the equation
def generate_function():
    global value
    global first
    global second
    global operator
    
    
    first = random.choice(operand_one)
    second = random.choice(operand_one)
    operator = random.choice(operators)
    if operator == "-":
        second = random.randint(0, first)
    elif operator == "/":
        second = random.randint(1, 10)
        while first % second != 0:
            first = random.randint(1,100)
    elif operator == "X":
        second = random.randint(1, 10)
        first = random.randint(1,12)

    string = str(first)+ operator + str(second)
    frontend_equation.config(text = string)
    clear_text()     
    switch_on()
    try:
        value= value+1
    except NameError:
        value = 1
    update_progress(value)

    return (first, second, operator)

def generate_sequence_for_quiz():
    start_of_sequence = random.randint(0,50)
    increment = random.randint(1, 12)
    sequence_length = random.randint(4,7)
    sequence = []
    sequence.append(start_of_sequence)
    next = start_of_sequence + increment
    sequence.append(next)
    for i in range(sequence_length-1):
        next = next + increment  
        sequence.append(next)
    return sequence








   


#####Frontend

window = Tk()
window.configure(bg='lightgreen')
window.title("MathQuizzer")
width = 600
height = 500
window.minsize(width=width, height = height)
window.maxsize(width=width, height = height)   
screen_width = window.winfo_screenwidth()  # Width of the screen
screen_height = window.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 
window.geometry('%dx%d+%d+%d' % (width, height, x, y))

def ArithmeticWindow():
    global frontend_equation
    global success_or_not_frontend
    global input1
    window1 = Toplevel(window)
    window1.configure(bg='lightgreen')
    window1.title("Arithmetic")
    width = 600
    height = 500
    window1.minsize(width= width, height = height)
    window1.maxsize(width= width, height = height)
    screen_width = window1.winfo_screenwidth()  # Width of the screen
    screen_height = window1.winfo_screenheight() # Height of the screen
 
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
 
    window1.geometry('%dx%d+%d+%d' % (width, height, x, y))

    buttons = ttk.Frame(window1)
    buttons.pack(pady = 5)
    text_for_progress_bar = "Progress_bar:"
    label_for_progress_bar = Label(buttons, text= text_for_progress_bar, font = 15, fg = "black", bg = "lightgreen")
    label_for_progress_bar.pack(side = LEFT)  
    progress_bar = ttk.Progressbar(buttons, length=50, mode="determinate", orient="horizontal")
    progress_bar.pack()   
    generate_button  = Button(window1, text ="generate", command = generate_function)
    generate_button.pack()
    text1 = "Please \n press generate"
    
    frontend_equation = Label(window1, text= text1, font = 15, fg = "#ff0", bg = "#000000")
    frontend_equation.pack(pady=(20, 20))

    input1 = Entry(window1)
    input1.pack()

    validate_button  = Button(window1, text ="validate", command= validate_function)
    validate_button.pack()

    text2 = "success or \nTry again"

    success_or_not_frontend = Label(window1, text= text2, font = 15, fg = "#ff0", bg = "#000000")
    success_or_not_frontend.pack(pady=(20, 20))


def SequenceWindow():
    global sequence_question
    window2 = Toplevel(window)
    window2.configure(bg='lightgreen')
    window2.title("Sequence")
    width = 600
    height = 500
    window2.minsize(width= width, height = height)
    window2.maxsize(width= width, height = height)
    screen_width = window2.winfo_screenwidth()  # Width of the screen
    screen_height = window2.winfo_screenheight() # Height of the screen
 
    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
 
    window2.geometry('%dx%d+%d+%d' % (width, height, x, y))
    generate_button  = Button(window2, text ="generate", command = generate_sequence_after_button_click)
    generate_button.pack()

    sequence_question = ttk.Frame(window2)
    sequence_question.pack(pady = 5)



def generate_sequence_after_button_click():
    for widget in sequence_question.winfo_children():
        widget.destroy()
    generate_sequence = generate_sequence_for_quiz()
    sequence_number_to_miss = random.randint(0, len(generate_sequence))
    for i in range(len(generate_sequence)):
        if i != sequence_number_to_miss:
            label_of_seq_question = Label(sequence_question, text= str(generate_sequence[i]), font = 15, fg = "black", bg = "lightgreen")
            label_of_seq_question.pack(side = LEFT, padx = 1)
        else:
            input = Entry(sequence_question, width= 4, font = 15)
            input.pack(side = LEFT, padx = 1)




arithmetic_button = Button(window, text ="Arithmetic_questions", command = ArithmeticWindow)
arithmetic_button.pack()  
sequence_button = Button(window, text ="Sequence_questions", command = SequenceWindow)
sequence_button.pack()




# menubar = Menu(window)
# window.config(menu=menubar)

# # create a menu
# file_menu = Menu(menubar)
# menubar.add_command(label="quiz_type", command=donothing)








window.mainloop()


#C:\Users\rajim\Anaconda3\Scripts\pyinstaller.exe --noconsole -F tkinter1.py








