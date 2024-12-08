import tkinter as tk
from tkinter import *


def manual(main_window):
    m_text = """\t\t\t\t\t\tBlocks World\n\n
    Introduction
    The Blocks World project was done for the sole purpose of emulating the changing of location of 
    each block according to what the content of the final state. Not only, the program will show each 
    different state of change, but also report on the different commands manipulating certain blocks 
    and print what location the robot hand is at and the next location the robot hand will go. The 
    number of states will be printed alongside the list of commands for the state and relations for the 
    block. This feature is to keep track of the number of possible steps for the blocks going from
    initial state to final state.
 
    Process
    The simulation process will require a bit of imagination. As you look at the simulator, picture the 
    Start Location column as a table with the 3 stack locations turned 90 degrees counterclockwise, 
    the leftmost edges of the text boxes being the table and the rightmost edges of the stacks being
    the top of the stacks. Then, as you enter character values try to keep in mind that the first
    character is on the table and the rightmost character is the top of the stack.
    Apply the same principal to the Output column.
    
    Step 1:
    For step 1, enter any number of characters you wish at each location without entering repeated 
    values. Next, enter those same characters at each location in the Output Column. Click “Enter” 
    and press “OK” on the prompt to proceed.
    
    Step 2:
    Click the “Run” button to start the simulation. The “Moves in Action” window showing the
    step-by-step process of the picking and placing of the characters as though they are blocks being
    moved by a robot hand. The first action represented by State 0 is the initial state with
    nothing moved just yet. The moves made for the state are listed below the initial state.
    L0 is Location 1, L1 is Location 2 and L2 is Location 3. The corresponding relationships
    are displayed, and the new state of the stacks are shown after the operations and relationships.
    NOOP stands for no operation.
    
    Step 3: 
    Before you put in a new set of values, click on “Clear” to not only clear all entries
    but also empty all the stacks saved within the program.
    
    NOTE: If you want speedy results, it is highly recommended that no more than 6 characters should 
    be used for the simulation due to the complexity of its algorithm. You can still use more than 6 
    characters if the long wait time is not inconvenient for you.\n"""
    
    
    man = Toplevel(main_window)
    man.geometry("850x450")
    man.resizable(False,False)
    man.title('Manual')
       
    m_widget = Text(man, height=370, width=500)
    scrollbar = Scrollbar(man)
    scrollbar.pack(side=RIGHT, fill=Y)
    m_widget.insert(tk.END, m_text)
    m_widget.config()
    m_widget.config(state=DISABLED)
    m_widget.config(yscrollcommand=scrollbar.set)
    m_widget.pack()    
    scrollbar.config(command=m_widget.yview)