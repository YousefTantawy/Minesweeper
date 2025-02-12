# Minesweeper
Minesweeper is a popular single-player puzzle game that originated in the 1960s and gained significant popularity with the inclusion of the game in the Microsoft Windows operating system.
The objective of Minesweeper is to clear a rectangular grid of hidden tiles or cells without uncovering any mines. The grid represents a minefield, and each tile can either be empty or contain a hidden mine. The player's task is to reveal all the empty tiles without triggering any mines.
How to use.
At the beginning of the game, the player is presented with a grid of covered tiles. By clicking on a tile, the player reveals its content. If the revealed tile contains a mine, the game ends, and the player loses. However, if the revealed tile is empty, it displays a number indicating the number of neighboring tiles that contain mines. Using this information, the player can deduce the locations of mines and safely reveal adjacent tiles. The player can also flag tiles they suspect to contain mines to avoid accidental clicks.
The game continues until the player successfully reveals all the empty tiles, uncovering the entire minefield, or until the player triggers a mine. The player's performance is typically measured by the time taken to complete the game or the number of flags used.
neighbouring_tiles_around: This function takes two parameters x and y, which represent the coordinates of a tile on the game board. It calculates and returns a list of the neighboring tiles around the given coordinates. It does this by defining a list of directions (directions) representing the eight possible directions (top-left, top, top-right, left, right, bottom-left, bottom, bottom-right). For each direction, it calculates the new coordinates (cx and cy) by adding the direction values to the given coordinates. It then checks if the new coordinates are within the board boundaries (0 <= cx < board_size and 0 <= cy < board_size), and if so, it appends the corresponding tile value from the board matrix to the tiles list. Finally, it returns the list of neighboring tiles.


neighbouring_mines_around: This function takes two parameters x and y, representing the coordinates of a tile on the game board. It calls the neighbouring_tiles_around function, passing the coordinates, to obtain a list of neighboring tiles. It then counts the number of empty strings ("") in the neighboring tiles list using the count method. This count represents the number of mines in the neighboring tiles. The function returns the count of mines.
reveal: This function takes two parameters x and y, representing the coordinates of a tile on the game board. It is responsible for revealing the tile and its neighboring tiles.
It first checks if the tile has already been revealed (player_board[y][x] != '-') or flagged (player_board[y][x] == 'F'). If so, it returns without making any changes.
If the tile represents a mine (board[y][x] == ''), it sets the corresponding tile in the player_board to 'B', indicating a revealed mine, and returns.
If the tile is not a mine, it sets the corresponding tile in the player_board to the string representation of the number of neighboring mines (board[y][x]).
If the tile has no neighboring mines (i.e., board[y][x] == 0), it recursively calls the reveal function for each neighboring tile (excluding the current tile itself) to reveal them as well.
The function is called recursively, which means it can lead to a chain of tile revelations if there are multiple tiles with no neighboring mines.
flag: This function takes two parameters x and y, representing the coordinates of a tile on the game board. It is responsible for flagging/unflagging a tile.
If the tile is currently unflagged (player_board[y][x] == '-'), it sets the corresponding tile in the player_board to 'F', indicating a flagged tile.
If the tile is currently flagged (player_board[y][x] == 'F'), it sets the corresponding tile in the player_board back to '-' to remove the flag.
draw_board(): This function is responsible for drawing the game board on the GUI canvas.
It iterates over each cell in the player_board matrix using nested loops.
For each cell, it determines the color based on its value ('-', 'F', 'B', or a number) and assigns it to the color variable.
It then creates a rectangle on the canvas representing the cell, using the appropriate coordinates and color.
If the cell contains a number, it adds text inside the rectangle to display the number.
This function is called to draw the initial game board and update it after tile revelations or flagging/unflagging.
handle_click(event): This function is the event handler for mouse clicks on the GUI canvas.
It takes an event parameter representing the mouse click event.
It extracts the coordinates (x and y) of the clicked tile based on the event's x and y attributes and the tile_size.
If the left mouse button is clicked (event.num == 1), it calls the reveal function passing the tile coordinates to reveal the clicked tile and its neighboring tiles. It then checks for win or loss conditions by checking the state of the player_board matrix.
If the right mouse button is clicked (event.num == 3), it calls the flag function passing the tile coordinates to flag/unflag the clicked tile.
This function is bound to the left and right mouse button events on the canvas and is triggered when a user clicks on a tile.
restart_game(): This function is responsible for restarting the game by resetting the game board and bomb placement.
It reinitializes the board, player_board, and bombs_placed variables.
It then proceeds to place the bombs randomly on the game board as before.
After bomb placement, it calculates the number of neighboring mines for each non-mine cell in the board matrix.
Finally, it calls the draw_board() function to update the GUI with the new game board.






