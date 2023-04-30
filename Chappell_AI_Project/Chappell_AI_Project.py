from queue import Empty
import random

#Actions for the robot hand
def peek(stack):        
    if stack:
        return stack[-1]
    else:
        return None

#Returns the table index of the block
def get_table_index(block, stack, index):
    if block in stack[index]:
        return(index)
    
#Returns the number of blocks to unstack
def search_block(stack, element):
        for i in range(len(stack)):
            if stack[i] is element:
                element_index = (len(stack) - stack.index(element))-1
                break
        
        return element_index


#The operation for removing the number of blocks
#for pick_and_place() to take over later
def unstack_phase(i_table, num_of_blocks, index):    
    #Decisions for choosing a stack
    match index:
        case 0:
            random_stack = random.choice([1,2])
        case 1:
            random_stack = random.choice([0,2])
        case 2:
            random_stack = random.choice([0,1])
    
    if num_of_blocks == None:
        print("No blocks to move.")
    else:    
        if num_of_blocks == 0:
            return
        else:
            #Chose a stack - if stack is empty put it in immediately       
                if i_table[random_stack] == []:
                    i_table[random_stack].append(i_table[index].pop())
                else:
                    i_table[random_stack].append(i_table[index].pop())
                    #i_table[random_stack].append(i_table[index].pop())
                unstack_phase(i_table, num_of_blocks - 1, index)

#The desired index is cleared for placing the chosen block
# def clear_index(table, element,s1_available, s2_available, s3_available):
#     #Handling availability
#     match index:
        
#     if num == 0:
#         pass
    
#     return

# The main placement operation
def pick_and_place(table, r_table,s):
    
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
                        chosen_stack = random.choice([1,2])
                    case 1:
                        chosen_stack = random.choice([0,2])
                    case 2:
                        chosen_stack = random.choice([0,1])
                        
                table[chosen_stack].append(table[x].pop())
                    
                # The state and placements
                print(f"State {s}: ",table)
                print(f"PICK UP(L{x})")
                print(f"MOVE(L{x},L{chosen_stack})")
                print(f"PUTDOWN(L{chosen_stack})")
                print(f"STACK(L{chosen_stack})")
                print(f"UNSTACK(L{x}, L{chosen_stack})")
                print("")
                
                # The relations
                print("Relations:")
                if search_block(table[chosen_stack],peek(table[chosen_stack])) == 0:
                    print(f"TABLE({peek(table[chosen_stack])})")
                if search_block(table[chosen_stack],peek(table[chosen_stack])) != 0:
                    print(f"ON({peek(table[chosen_stack])})")
                if search_block(table[chosen_stack],peek(table[chosen_stack])) == len(table[chosen_stack]):
                    print(f"CLEAR({peek(table[chosen_stack])})")
                if search_block(table[chosen_stack],peek(table[chosen_stack])) == None:
                    print(f"ABOVE({peek(table[chosen_stack])})")
                    
                print("")
                
                s+=1
                # Check to see if current state matches final state
                if (table[0] == r_table[0]) and (table[1] == r_table[1]) and (table[0] == r_table[0]):
                    break
    print("Finished Process")
    print(table)


#List
table = []
r_table = []

#3 Stacks
stack1 = []
stack2 = []
stack3 = []

#3 resulting stacks
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

# State counter
s = 0

# User input values for the initial state
loc1 = input("Enter values for Location 1:")
loc2 = input("Enter values for Location 2:")
loc3 = input("Enter values for Location 3:")

print("")

# User input values for the output
output_L1 = input("Enter values for output location 1:")
output_L2 = input("Enter values for output location 2:")
output_L3 = input("Enter values for output location 3:")

print("")

# Concatenation stage for Location 1
for block in loc1:
    stack1.append(block)

# Concatenation stage for Location 2
for block in loc2:
    stack2.append(block)

# Concatenation stage for Location 3
for block in loc3:
    stack3.append(block)

# print("Initial State")    
# print(table)

# Concatenation stage for Location 1
for block in output_L1:
    r_stack1.append(block)

# Concatenation stage for Location 2
for block in output_L2:
    r_stack2.append(block)

# Concatenation stage for Location 3
for block in output_L3:
    r_stack3.append(block)

# The main operation of Block World
#pick_and_place(table, r_table,s)

for x in range(len(table)):
    h = get_table_index('b',table,x)
    if h == None:
        pass
    else:
        print(h)
        break

sb = search_block(table[0],'a')

print(sb)

print("Unstack Phase")

#Unstack Phase
unstack_phase(table, sb, 0)
print(table)

#Clear Index
for x in range(len(table)):
    if 'a' not in table[x] and :
        print("Index is okay to unstack")
        print(x)
        break
