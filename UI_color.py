#       Done 100 %

from tkinter import *
from tkinter import ttk

home_page = Tk()
style= ttk.Style()
style.theme_use('clam')

""""
ttk.Label(home_page, background='green', text='green').grid(row=0, column=0, sticky='snew')
ttk.Label(home_page, background='yellow', text='yellow').grid(row=0, column=1, sticky='snew')
ttk.Label(home_page, background='blue', text='blue').grid(row=1, column=0, columnspan=2, sticky='snew')
ttk.Label(home_page, background='orange', text='orange').grid(row=0, column=2, rowspan=2, sticky='snew')
ttk.Label(home_page, background='red', text='red').grid(row=0, column=4, sticky='snew')
ttk.Label(home_page, background='pink', text='pink').grid(row=1, column=4, sticky='snew')
"""
"""
ttk.Label(home_page, background='yellow', text='yellow').grid(row=0, column=0, rowspan=2, sticky='snew')
ttk.Label(home_page, background='orange', text='orange').grid(row=0, column=1, rowspan=2, sticky='snew')
ttk.Label(home_page, background='blue', text='blue').grid(row=0, column=2, rowspan=2, sticky='snew')
ttk.Label(home_page, background='pink', text='Pink').grid(row=2, column=0, columnspan=3, sticky='snew')
ttk.Label(home_page, background='green', text='green').grid(row=0, column=3, rowspan=3, sticky='snew')
ttk.Label(home_page, background='red', text='red').grid(row=3, column=0, columnspan=4, sticky='snew')
#ttk.Label(home_page, background='pink', text='Pink').grid(row=0, column=0, sticky='snew')
#green
"""
""""
ttk.Label(home_page, background='yellow', text='yellow').grid(row=0, column=0, columnspan=3, sticky='snew')
ttk.Label(home_page, background='red', text='red').grid(row=1, column=0, columnspan=3, sticky='snew')
ttk.Label(home_page, background='blue', text='blue').grid(row=2, column=0, rowspan=2, sticky='snew')
ttk.Label(home_page, background='orange', text='orange').grid(row=2, column=1, columnspan=2, sticky='snew')
ttk.Label(home_page, background='green', text='green').grid(row=0, column=3, rowspan=3, sticky='snew')
ttk.Label(home_page, background='pink', text='pink').grid(row=3, column=1, columnspan=3, sticky='snew')
"""


#  تقدر تبسطها بال class راجعها
yellow_label= ttk.Label(home_page, background='yellow', text='yellow')
yellow_label.grid(row=0, column=0, rowspan=2, sticky='snew')
orange_label=ttk.Label(home_page, background='orange', text='orange', font=('Arial', 10, 'bold'))
orange_label.grid(row=0, column=1, rowspan=2, sticky='snew')
blue_label=ttk.Label(home_page, background='blue', text='blue')
blue_label.grid(row=4, column=0, rowspan=2, sticky='snew', padx=10, pady=10)
pink_label=ttk.Label(home_page, background='pink', text='Pink')
pink_label.grid(row=2, column=0, columnspan=3, sticky='snew')
green_label=ttk.Label(home_page, background='green', text='green')
green_label.grid(row=0, column=3, rowspan=3, sticky='snew')
red_label=ttk.Label(home_page, background='red', text='red')
red_label.grid(row=3, column=0, columnspan=4, sticky='snew', ipadx=15, ipady=0)
black_label=ttk.Label(home_page, background='black', text='black', foreground='white')
black_label.grid(row=0, column=2, rowspan=2, sticky='snew')
white_label=ttk.Label(home_page, background='white', text='white', font=('Arial', 10, 'bold'))
white_label.grid(row=4, column=1, columnspan=2, sticky='snew')
brown_label=ttk.Label(home_page, background='brown', text='brown')
brown_label.grid(row=5, column=1, columnspan=2, sticky='snew')
green_label2=ttk.Label(home_page, background='green', text='green')
green_label2.grid(row=4, column=3, rowspan=2, sticky='snew')
numcolu = 0
numrow = 0
while numrow < 6 and numcolu <4:
    home_page.rowconfigure(numrow, weight=1)
    numrow += 1
    home_page.columnconfigure(numcolu, weight=1)
    numcolu += 1

""""
home_page.rowconfigure(0, weight=1)
home_page.rowconfigure(1, weight=1)
home_page.rowconfigure(2, weight=1)
home_page.rowconfigure(3, weight=1)
home_page.rowconfigure(4, weight=1)
home_page.rowconfigure(5, weight=1)
home_page.columnconfigure(0, weight=1)
home_page.columnconfigure(1, weight=1)
home_page.columnconfigure(2, weight=1)
home_page.columnconfigure(3, weight=1)
home_page
"""

home_page.mainloop()
