import random
from tkinter import *
from tkinter import messagebox
import time

root_memory = Tk()
root_memory.title("Proje 2")
canvas_width = 500
canvas_height = 500

w = Canvas(root_memory,
           width=canvas_width,
           height=canvas_height)
w.pack()
w.create_rectangle(0, 0, canvas_width, canvas_width-70, fill="purple")

level = 5
x = 0
DELAY = 375
memory_number = []
input_1 = Entry(root_memory)
w.create_window(150, 455, window=input_1)


def getnumbers():
    input_1.config(state='disabled')
    for x in range(0, level):
        number = random.randint(0, 9)
        w.create_text(random.randint(30, 430),
                      random.randint(30, 375),
                      font=("family ", 50),
                      text=number, tag="number"+str(x))
        w.itemconfigure("number"+str(x), state='hidden')
        memory_number.append(number)


def clear():
    for x in range(0, level):
        w.delete("number"+str(x))


def show_numbers(c=0):
    if c <= level:
        w.itemconfigure("number"+str(c), state="normal")
        root_memory.after(DELAY, hide_numbers, c)
    if c == level:
        input_1.config(state='normal')


def hide_numbers(c=0):
    if c <= level:
        w.itemconfigure("number"+str(c), state="hidden")
        root_memory.after(DELAY, show_numbers, c+1)
    if c == level:
        input_1.config(state='normal')


def start():

    getnumbers()
    show_numbers()


start()


def checkpoint():
    global level
    answer = []

    for ch in input_1.get():
        if ch.isdigit():
            answer.append(int(ch))

    if answer == memory_number:
        memory_number.clear()
        clear()
        input_1.delete(0, 'end')
        messagebox.showinfo(
            "Sonuç", f"DOĞRU! \n{level+1}. Seviyeye geçtiniz ")
        level += 1
        getnumbers()
        show_numbers()
    else:
        root_memory.quit()


button2 = Button(root_memory, text="Cevap gönder", command=checkpoint)
button2.configure(width=10, background="#990005",fg="black", activebackground="#545454")
button2_window = w.create_window(41, 455, window=button2)
mainloop()
