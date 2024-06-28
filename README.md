# Blocks World

The Blocks World project was done for the sole purpose of emulating the changing of location of each block according to what the content of the final state. Not only the program will show each different state of change, but also report on the different commands manipulating certain blocks and print what location the robot hand is at and the next location the robot hand will go. The number of states will be printed alongside the list of commands for the state and relations for the block. This feature is to keep track of the number of possible steps for the blocks going from initial state to final state.

The goal of Blocks World is to get a report of how many steps it takes to get from an initial state to final state and to show that even though the program may be inefficient and that it takes a long time, the program still works. Another goal is to get the number of states, all the possible commands for each state at a time and relations of one block as it is moved from one location to another. The results will have two trials of inputs to confirm that the program works. The results will only have the first three stages from the initial state and three states before the final state because of the large length of the process.


Summary of the Process

Input: First, the user will input the blocks for the initial state in all three locations.

Output: Next, the user will enter the blocks for the final state.

Concatenation: After the inputs and output have been entered, concatenation will take place for the locations.

The Movement Process: The blocks will then be moced the simulated robot arm, the states and commands will be printed until the desired state is reached.


The process goes as followed:
- First the user will input blocks for the initial state in all three locations.
- Next, the user will be prompted to enter the blocks for the final state.
- After the inputs and outputs are entered, the concatenation of the strings entered will take place and fill the letters in the chosen locations.
- The three locations of the states are represented in stack. The leftmost character represents the bottom of the stack, and the rightmost character represents the top of the stack.
- If all locations are not equal to the final state, then enter the while loop to proceed with the operation within the while loop.
- If all locations are equal, then the process is completed.
- If a stack is empty, then the robot hand will do nothing.
- When a non-empty location is detected, a decision of where to put a block will be made.
- The blocks will be moved and placed based on the decided location.
- Once the placing of the block is finished, the status will print, and the process will start again until the final stage is reached.



