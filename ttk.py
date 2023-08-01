import tkinter
from tkinter import ttk

root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)   # make sure it fills the root window
ttk.Label(big_frame, text="Hello World!").pack()
root.mainloop()

