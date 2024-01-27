# gamelife
The aim of the project is to implement the Conway's Game of Life.
The solution should contain at least three classes:
Cell - a single cell that can be alive or dead,
Generation - a set of cells for a given time step - a game board containing cols x rows of cells and methods enabling simulation, including:
• a method generating the board after passing a given number of simulation steps,
• constructor creating a random board with given dimensions and number of living
cells,
• constructor creating a random board with given dimensions and population density
(the ratio of the number of living cells to the board area),
• constructor creating a board based on a string of characters,
• overloaded == operator enabling the comparison of two boards, e.g. to check if
there was any change in the next step (whether a stable structure was created)
• ToString method that returns the board content in a text form,
Game - a class that supports the simulation, enabling its launch on the basis of data entered by the user, displaying the board, saving the game state to a file, reading it from a file.
The interface can be in any form, the program should be resistant to user errors.
