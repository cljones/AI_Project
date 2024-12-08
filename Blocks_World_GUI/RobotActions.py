import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sys


class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)

# Actions for the robot hand
def peek(stack):        
    if stack:
        return stack[-1]
    else:
        return None


def search_block(stack, element):
    for i in range(len(stack)):
        if stack[i] is element:
            element_index = (len(stack) - stack.index(element))-1
            return element_index
        else:
            return


# The main placement operation
def run(main_window,table, r_table):
    
    sim = Toplevel(main_window)
    sim.geometry("700x400")
    sim.resizable(False, False)
    sim.title('Moves in Actions')
        
    text_widget = tk.Text(sim)
    text_widget.pack()
        
    sys.stdout = StdoutRedirector(text_widget)

    # State counter
    s = 0
    
    while table != r_table:   
    
        for x in range(len(table)):
            if table[x] == []:
                
                print(table)
                print("NOOP") 
                print("")
                pass
            else:
                index = x
                match index:
                    case 0:
                        chosen_stack = random.choice([1, 2])
                    case 1:
                        chosen_stack = random.choice([0, 2])
                    case 2:
                        chosen_stack = random.choice([0, 1])
                        
                table[chosen_stack].append(table[x].pop())
                    
                # The state and placements
                print(f"State {s}: {table}")
                print(f"PICK UP(L{x})")
                print(f"MOVE(L{x},L{chosen_stack})")
                print(f"PUTDOWN(L{chosen_stack})")
                print(f"STACK(L{chosen_stack})")
                print(f"UNSTACK(L{x}, L{chosen_stack})")
                print("")
                
                # The relations
                print("Relations:")
                if search_block(table[chosen_stack], peek(table[chosen_stack])) == 0:
                    print(f"TABLE({peek(table[chosen_stack])})")
                if search_block(table[chosen_stack], peek(table[chosen_stack])) != 0:
                    print(f"ON({peek(table[chosen_stack])})")
                if search_block(table[chosen_stack], peek(table[chosen_stack])) == len(table[chosen_stack]):
                    print(f"CLEAR({peek(table[chosen_stack])})")
                if search_block(table[chosen_stack], peek(table[chosen_stack])) == None:
                    print(f"ABOVE({peek(table[chosen_stack])})")
                    
                print("")
                
                s += 1
                
                # Check to see if current state matches final state
                if (table[0] == r_table[0]) and (table[1] == r_table[1]) and (table[0] == r_table[0]):
                    break
    
    print("Finished Process")
    print(table)
    text_widget.config(state=DISABLED)
    messagebox.showinfo("Completed", "Desired state successfully reached!")



def get_entries(loc1,loc2,loc3,loc1R,loc2R,loc3R,stack1,stack2,stack3,r_stack1,r_stack2,r_stack3):

    loc1_value = loc1.get()       

    if str(loc1_value) != "":
        alert = f"{str(loc1_value)} in Start Location 1\n"

    loc2_value = loc2.get()

    if str(loc2_value) != "":            
        alert += f"{str(loc2_value)} in Start Location 2\n"

    loc3_value = loc3.get()

    if str(loc3_value) != "":           
        alert += f"{str(loc3_value)} in Start Location 3\n"

    loc1R_value = loc1R.get()

    if str(loc1R_value) != "":         
        alert += f"{str(loc1R_value)} in Output Location 1\n"

    loc2R_value = loc2R.get()

    if str(loc2R_value) != "":           
        alert += f"{str(loc2R_value)} in Output Location 2\n"

    loc3R_value = loc3R.get()
    if str(loc3R_value) != "":           
        alert += f"{str(loc3R_value)} in Output Location 3\n"

    messagebox.showinfo("Your Entries", alert)  

    # Concatenation stage for Location 1
    for block in loc1.get():
        stack1.append(block)

    # Concatenation stage for Location 2
    for block in loc2.get():
        stack2.append(block)

    # Concatenation stage for Location 3
    for block in loc3.get():
        stack3.append(block)

    # Concatenation stage for Location 1
    for block in loc1R.get():
        r_stack1.append(block)

    # Concatenation stage for Location 2
    for block in loc2R.get():
        r_stack2.append(block)

    # Concatenation stage for Location 3
    for block in loc3R.get():
        r_stack3.append(block)


def clear_entries(loc1,loc2,loc3,loc1R,loc2R,loc3R,stack1,stack2,stack3,r_stack1,r_stack2,r_stack3):
    messagebox.showinfo("Cleared", "All Entries cleared!")
    loc1.set("")
    loc2.set("")
    loc3.set("")
    loc1R.set("")
    loc2R.set("")
    loc3R.set("")

    stack1.clear()
    stack2.clear()
    stack3.clear()

    r_stack1.clear()
    r_stack2.clear()
    r_stack3.clear() 