from tkinter import *
from tkinter import ttk
import random
import time
list_one = range(50)
list_two = range(50)
list_three = ["+", "-", "X", "/"]

def generate_function():
    global third
    global first
    global second
    global value
    third = random.choice(list_three)
    first = random.choice(list_one)
    second = random.choice(list_one)
    if third == "-":
        second = random.randint(0, first)
    elif third == "/":
        second = random.randint(1, 10)
        while first % second != 0:
            first = random.randint(1,100)
    elif third == "X":
        second = random.randint(1, 10)
        first = random.randint(1,12)

    string = str(first)+ third + str(second)
    lab1.config(text = string)
    clear_text()
    switch_on()
    try:
        value= value+1
    except NameError:
        value = 1
    update_progress(value)

    return (first, second, third)

   




window = Tk()
window.configure(bg='lightgreen')
window.title("First One")
window.minsize(width=200, height = 400)
window.maxsize(width=400, height = 700)

progress_bar = ttk.Progressbar(window, length=50, mode="determinate", orient="horizontal")
progress_bar.pack(pady=(10, 10))  



B1  = Button(window, text ="generate", command = generate_function)
B1.pack()
text1 = "Please \n press generate"

lab1 = Label(window, text= text1, font = 15, fg = "#ff0", bg = "#000000")
lab1.pack(pady=(20, 20))

input = Entry(window)
input.pack()

def clear_text():
    input.delete(0, END)

def switch_off():
    B2["state"] = "disabled"
    
def switch_on():
    B2["state"] = "normal"

def update_progress(value):
    progress_bar["value"] = value
    window.update()



def helloCallBack():

    a = first
    b = third
    c = second
    if b == "+":
        ans = a+c
    elif b == "-":
        ans = a-c
    elif b == "X":
        ans = a*c
    else:
        ans = a//c
    return ans
bg_color = "black"
def baba():
    ans = helloCallBack()
    global bg_color
    if str(ans) == str(input.get()):
        final_ans = "Good"
        print(ans)
        print(input.get())
        if bg_color == "black":
            bg_color = "blue"
        else:
            bg_color = "black"
        lab2.config(text = final_ans, fg='lightgreen', bg = bg_color)
    else:
        final_ans = "A Not Good"
        print(ans)
        print(input.get())
        lab2.config(text = final_ans, fg = "red")
    switch_off()



B2  = Button(window, text ="validate", command= baba)
B2.pack()

text2 = "success or \nTry again"

lab2 = Label(window, text= text2, font = 15, fg = "#ff0", bg = "#000000")
lab2.pack(pady=(20, 20))

window.mainloop()
