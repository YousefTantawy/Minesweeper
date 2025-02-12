#MineSweeper Project | Semester 2 SPRING2023

import sys #To exit code if a wrong choice was inputted
import random #To choose a random place for bombs to be placed
import tkinter as tk #GUI to be used for the MineSweeper game
from tkinter import messagebox #Since messagebox is a submodule, this line is required to access it

# Game Difficulty
gameDifficulty = input("Choose a Difficulty(E, M, H): ") 

if gameDifficulty.upper() == "E":
    board_size = 8
    num_bombs = 10
elif gameDifficulty.upper() == "M":
    board_size = 13
    num_bombs = 40
elif gameDifficulty.upper() == "H":
    board_size = 16
    num_bombs = 60
else:
    print("Error")
    sys.exit(1)

# Tile size
tile_size = 30

# Board Size and Bomb Placement
board = [[0 for _ in range(board_size)] for _ in range(board_size)]
player_board = [['-' for _ in range(board_size)] for _ in range(board_size)]

bombs_placed = 0

while bombs_placed < num_bombs:
    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)

    if board[y][x] != "":
        board[y][x] = ""
        bombs_placed += 1

# Number of mines in surrounding one tile

def neighbouring_tiles_around(x, y):
    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1, 0), (1, 0), (-1, 1),
                  (0, 1), (1, 1)]   
    tiles = []
    global board_size
    for d in directions:
        cx, cy = x + d[0], y + d[1]
        if 0 <= cy < board_size and 0 <= cx < board_size:
            tiles.append(board[cy][cx])
    return tiles


def neighbouring_mines_around(x, y):
    neighbouring = neighbouring_tiles_around(x, y)
    mines = neighbouring.count("")
    return mines


for i in range(board_size):
    for j in range(board_size):
        if board[i][j] == "":
            continue
        board[i][j] = neighbouring_mines_around(j, i)

# Reveal of Tiles
def reveal(x, y):
    if player_board[y][x] != '-':
        return
    if player_board[y][x] == 'F':
        return
    if board[y][x] == '':
        player_board[y][x] = 'B'
        return
    player_board[y][x] = str(board[y][x])
    if board[y][x] == 0:
        for i in range(max(0, y - 1), min(board_size, y + 2)):
            for j in range(max(0, x - 1), min(board_size, x + 2)):
                if i == y and j == x:
                    continue
                reveal(j, i)


# Flaging system

def flag(x, y):
    if player_board[y][x] == '-':
        player_board[y][x] = 'F'
    elif player_board[y][x] == 'F':
        player_board[y][x] = '-'
    draw_board()

# GUI Board Drawing

def draw_board():
    for i in range(board_size):
        for j in range(board_size):
            tile = player_board[i][j]
            if tile == '-':
                color = 'gray'
            elif tile == 'F':
                color = 'red'
            elif tile == 'B':
                color = 'black'
            else:
                color = 'lightgray'
            canvas.create_rectangle(j * tile_size, i * tile_size,
                                    (j + 1) * tile_size, (i + 1) * tile_size,
                                    fill=color, outline='white')
            if tile.isnumeric():
                canvas.create_text((j + 0.5) * tile_size, (i + 0.5) * tile_size,
                                    text=tile, fill='blue')

# Play Game Function
def restart_game():
    global board, player_board, bombs_placed
    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    player_board = [['-' for _ in range(board_size)] for _ in range(board_size)]
    bombs_placed = 0
    while bombs_placed < num_bombs:
        x = random.randint(0, board_size - 1)
        y = random.randint(0, board_size - 1)

        if board[y][x] != "":
            board[y][x] = ""
            bombs_placed += 1

    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == "":
                continue
            board[i][j] = neighbouring_mines_around(j, i)

    draw_board()

# Mouse use in GUI + Win or loss
def handle_click(event):
    x = event.x // tile_size
    y = event.y // tile_size
    if event.num == 1:  # Left click
        if player_board[y][x] != 'F':
            reveal(x, y)
            draw_board()
            if all('-' not in row for row in player_board) and any('B' not in row for row in player_board):
                messagebox.showinfo("Congratulations", "You won, congratulations!")
                restart_game()
            elif any('B' in row for row in player_board) :
                messagebox.showinfo("Game Over", "Game over!")
                restart_game()
    elif event.num == 3:  # Right click
        flag(x, y)


root = tk.Tk()
root.title("Minesweeper")

canvas = tk.Canvas(root, width=board_size * tile_size, height=board_size * tile_size)
canvas.pack()

canvas.bind("<Button-1>", handle_click)
canvas.bind("<Button-3>", handle_click)

draw_board()

root.mainloop()