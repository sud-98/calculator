from tkinter import *

root = Tk()
root.title("My Calculator")

e = Entry(root, width=50, borderwidth=10, fg="white",
          bg="black")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# defining command


def click(num):

    if(e.get()):
        curr = int(e.get())
        e.delete(0, END)
        n = (curr * 10) + num
        e.insert(0, n)
    else:
        e.insert(0, num)


def clear():
    e.delete(0, END)


def add():
    if(e.get()):
        prev = e.get()
        global exp
        global math
        math = "+"
        exp = prev
        e.delete(0, END)


def subtract():
    if(e.get()):
        prev = e.get()
        global exp
        global math
        math = "-"
        exp = prev
        e.delete(0, END)


def mult():
    if(e.get()):
        prev = e.get()
        global exp
        global math
        math = "*"
        exp = prev
        e.delete(0, END)


def div():
    if(e.get()):
        prev = e.get()
        global exp
        global math
        math = "/"
        exp = prev
        e.delete(0, END)


def equals():
    if e.get():
        next = e.get()
        e.delete(0, END)
        e.insert(0, str(eval(exp + math + next)))


# Adding buttons(numerics)
b9 = Button(root, text="9", padx=40, pady=10,
            command=lambda: click(9)).grid(row=1, column=2)
b8 = Button(root, text="8", padx=40, pady=10,
            command=lambda: click(8)).grid(row=1, column=1)
b7 = Button(root, text="7", padx=40, pady=10,
            command=lambda: click(7)).grid(row=1, column=0)

b6 = Button(root, text="6", padx=40, pady=10,
            command=lambda: click(6)).grid(row=2, column=2)
b5 = Button(root, text="5", padx=40, pady=10,
            command=lambda: click(5)).grid(row=2, column=1)
b4 = Button(root, text="4", padx=40, pady=10,
            command=lambda: click(4)).grid(row=2, column=0)

b3 = Button(root, text="3", padx=40, pady=10,
            command=lambda: click(3)).grid(row=3, column=2)
b2 = Button(root, text="2", padx=40, pady=10,
            command=lambda: click(2)).grid(row=3, column=1)
b1 = Button(root, text="1", padx=40, pady=10,
            command=lambda: click(1)).grid(row=3, column=0)

b0 = Button(root, text="0", padx=40, pady=10,
            command=lambda: click(0)).grid(row=4, column=0)

# adding buttons(operators)
b_add = Button(root, text="+", padx=40, pady=10,
               command=add).grid(row=2, column=3)

b_equal = Button(root, text="=", padx=40, pady=10,
                 command=equals).grid(row=4, column=3)

b_subtract = Button(root, text="-", padx=40, pady=10,
                    command=subtract).grid(row=3, column=3)

b_mult = Button(root, text="*", padx=40, pady=10,
                command=mult).grid(row=4, column=1)

b_div = Button(root, text="/", padx=40, pady=10,
               command=div).grid(row=4, column=2)

b_clear = Button(root, text="C", padx=40, pady=10,
                 command=clear).grid(row=1, column=3)

root.mainloop()
