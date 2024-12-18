# Blocks World Simulator

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



![Description of Methodology](https://github.com/user-attachments/assets/525e7ffe-da8a-437c-aed1-d0b8c703f99d)


![flow chart of states](https://github.com/user-attachments/assets/18037209-6b90-45cb-853f-676102abba4b)


![Format of States of and Commands](https://github.com/user-attachments/assets/86695e8f-6437-4b9b-b8ae-50c55c9092cf)


![Initial State and Final State](https://github.com/user-attachments/assets/f67aaf0c-8919-4fb4-a8a2-e5fc5a77eb82)





For the GUI version

To run the simulator in Windows use the Blocks_World_GUI.exe. For MacOS and Linux, go to the dist directory in Linux/ and click on the Blocks_World_GUI file. The simulation process will require a bit of imagination. As you look at the simulator, picture the
Start Location column as a table with the 3 stack locations turned 90 degrees counterclockwise,
the leftmost edges of the text boxes being the table and the rightmost edges of the stacks being the
top of the stacks. Then, as you enter character values try to keep in mind that the first character is
on the table and the rightmost character is the top of the stack. Apply the same principal to the
Output column.

Step 1

![BW_sim_step1](https://github.com/user-attachments/assets/be19a253-97bb-4ec5-bbb2-47d3df91879c)

For step 1, enter any number of characters you wish at each location without entering repeated
values. Next, enter those same characters at each location in the Output Column. Click “Enter”
and press “OK” on the prompt to proceed.

![BW_sim_step2](https://github.com/user-attachments/assets/2656ca34-2cef-4e38-b068-0e2f8630e956)

Step 2

Click the “Run” button to start the simulation. The “Moves in Action” window showing the step-by-step process of the picking and placing of the characters as though they are blocks being moved by a robot hand. The first action represented by State 0 is the initial state with nothing moved just yet. The moves made for the state are listed below the initial state. L0 is Location 1, L1 is Location 2 and L2 is Location 3. The corresponding relationships are displayed, and the new state of the stacks are shown after the operations and relationships. NOOP stands for no operation.

![BW_sim_step3](https://github.com/user-attachments/assets/b1407a34-18ed-47b2-b30d-6146342a6819)

Step 3
Before you put in a new set of values, click on “Clear” to not only clear all entries but also empty all the stacks saved within the program.

![BW_sim_step4](https://github.com/user-attachments/assets/1394cb24-c776-4d97-899f-8a2b39a63502)

NOTE: If you want speedy results, it is highly recommended that no more than 6 characters should be used for the simulation due to the complexity of its algorithm. You can still use more than 6 characters if the long wait time is not inconvenient for you.

