import tkinter as tk
import random

class MinesweeperGUI:
    def __init__(self, master, rows, cols, mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [['E' for _ in range(cols)] for _ in range(rows)]
        self.placed_mines = set()
        self.revealed = set()
        self.create_widgets()

    def create_widgets(self):
        self.tiles = [[tk.Button(self.master, text='', width=2, height=1,
                                 command=lambda r=r, c=c: self.click_tile(r, c))
                       for c in range(self.cols)] for r in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                self.tiles[r][c].grid(row=r, column=c)

    def place_mines(self, click_r, click_c):
        while len(self.placed_mines) < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if abs(r - click_r) <= 1 and abs(c - click_c) <= 1:
                continue
            self.placed_mines.add((r, c))
            self.board[r][c] = 'M'

    def reveal(self, r, c):
        if (r, c) in self.placed_mines:
            for mine_r, mine_c in self.placed_mines:
                self.tiles[mine_r][mine_c].config(text='X')
            self.master.after(1000, self.end_game)
            return
        count = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) in self.placed_mines:
                    count += 1
        if count > 0:
            self.tiles[r][c].config(text=str(count))
        else:
            self.tiles[r][c].config(text='1')
            self.revealed.add((r, c))
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in self.revealed:
                        self.reveal(nr, nc)

    def click_tile(self, r, c):
        if self.board[r][c] == 'M':
            self.reveal(r, c)
        else:
            self.reveal(r, c)

    def end_game(self):
        self.master.destroy()

def play_minesweeper_gui(rows, cols, mines):
    root = tk.Tk()
    root.title("Minesweeper")
    game = MinesweeperGUI(root, rows, cols, mines)
    click_r, click_c = random.randint(0, rows - 1), random.randint(0, cols - 1)
    game.place_mines(click_r, click_c)
    root.mainloop()

# Example usage:
play_minesweeper_gui(12, 12, 15)
