from tkinter import *
from tkinter import ttk
# style.theme_names()
#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

home_page = Tk()
style = ttk.Style()
style.theme_use('clam')

style.configure('TButton', foreground='gray', background='black', )
#font=('Arial', 10, 'bold')
entry1 = ttk.Entry(home_page, width=15)
entry1.pack()

button1 = ttk.Button(home_page, text="Enter", width=10)
button1.pack()
button2 = ttk.Button(home_page, text="click Me", width=10)
button2.pack()
button3 = ttk.Button(home_page, text="click Me", width=10)
button3.pack()

style.configure('b1.TButton', foreground='yellow', background='pink')
button1.configure(style='b1.TButton')
style.configure('b2.TButton', background='green', font=('Arial', 14))
button2.configure(style='b2.TButton')
style.configure('b3.TButton', foreground='blue', background='orange', font=('Arial', 10, 'bold'))
button3.configure(style='b3.TButton')
style.configure('TEntry', foreground='gray')


def enter_function():
    print(entry1.get(), "\nThe button Clicked")
    entry1.delete(0, END)


def button_clicked(x):
    print("Button {} clicked".format(x))


def enter(event):
    print(entry1.get(), "\nThe button Clicked")
    entry1.delete(0, END)


entry1.bind('<q>', enter)

button1.config(command=lambda: enter_function())  # zed shake 3la lambda
button2.config(command=lambda: button_clicked(2))
button3.config(command=lambda: button_clicked(3))

home_page.mainloop()
