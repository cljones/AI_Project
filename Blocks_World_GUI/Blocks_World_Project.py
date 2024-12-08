import tkinter as tk
from tkinter import *
from Manual import manual
from RobotActions import *


main_window = tk.Tk()
main_window.geometry("550x350")

main_window.title("Blocks World Simulator")
main_window.resizable(False, False)

menu = Menu(main_window)
main_window.config(menu=menu)

# Menu
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Manual', command = lambda: manual(main_window))
filemenu.add_command(label='Exit', command=main_window.quit)

# Location string variables
loc1 = tk.StringVar()
loc2 = tk.StringVar()
loc3 = tk.StringVar()

# Resulting locations
loc1R = tk.StringVar()
loc2R = tk.StringVar()
loc3R = tk.StringVar()

# List
table = []
r_table = []

# 3 Stacks
stack1 = []
stack2 = []
stack3 = []

# 3 resulting stacks
r_stack1 = []
r_stack2 = []
r_stack3 = []

# Initialization of the Initial State
table.append(stack1)
table.append(stack2)
table.append(stack3)

# Initialization of the Initial State
r_table.append(r_stack1)
r_table.append(r_stack2)
r_table.append(r_stack3)

# Starting Stack 1
location1 = tk.Label(main_window, text="Start Location 1")
location1.place(x=50, y=25)
loc_entry1 = tk.Entry(textvariable=loc1)
loc_entry1.place(x=30, y=50)
loc_entry1.focus()

# Starting Stack 2
location2 = tk.Label(main_window, text="Start Location 2")
location2.place(x=50, y=75)
loc_entry2 = tk.Entry(textvariable=loc2)
loc_entry2.place(x=30, y=100)
loc_entry2.focus()

# Starting Stack 3
location3 = tk.Label(main_window, text="Start Location 3")
location3.place(x=50, y=125)
loc_entry3 = tk.Entry(textvariable=loc3)
loc_entry3.place(x=30, y=150)
loc_entry3.focus()

# Resulting Stack 1
out1 = tk.Label(main_window, text="Output Location 1")
out1.place(x=360, y=25)
loc_entry1R = tk.Entry(textvariable=loc1R)
loc_entry1R.place(x=350, y=50)
loc_entry1R.focus()

# Resulting Stack 2
out2 = tk.Label(main_window, text="Output Location 2")
out2.place(x=360, y=75)
loc_entry2R = tk.Entry(textvariable=loc2R)
loc_entry2R.place(x=350, y=100)
loc_entry2R.focus()

# Resulting Stack 3
out3 = tk.Label(main_window, text="Output Location 3")
out3.place(x=360, y=125)
loc_entry3R = tk.Entry(textvariable=loc3R)
loc_entry3R.place(x=350, y=150)
loc_entry3R.focus()

# Buttons
enter_button = tk.Button(main_window, text="Enter", command=lambda:
    get_entries(loc1,loc2,loc3,loc1R,loc2R,loc3R,stack1,stack2,stack3,r_stack1,r_stack2,r_stack3))
enter_button.place(x=155, y=300)

run_button = tk.Button(main_window, text="Run", command=lambda:run(main_window,table,r_table))
run_button.place(x=225, y=300)

clear_button = tk.Button(main_window, text="Clear", command=lambda:
    clear_entries(loc1,loc2,loc3,loc1R,loc2R,loc3R,stack1,stack2,stack3,r_stack1,r_stack2,r_stack3))
clear_button.place(x=285, y=300)

cancel_button = tk.Button(main_window, text="Cancel", command= lambda: main_window.destroy())
cancel_button.place(x=350, y=300)

main_window.mainloop()