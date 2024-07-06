import tkinter as tk
from tkinter import messagebox


class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for row in range(9):
            for col in range(9):
                self.cells[row][col] = tk.Entry(frame, width=5, font=('Arial', 18), justify='center', borderwidth=1,
                                                relief="solid")
                self.cells[row][col].grid(row=row, column=col, padx=5, pady=5)

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        solve_button = tk.Button(button_frame, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=0, column=0, padx=10)

        clear_button = tk.Button(button_frame, text="Clear", command=self.clear_grid)
        clear_button.grid(row=0, column=1, padx=10)

    def clear_grid(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)

    def solve_sudoku(self):
        grid = self.get_grid()
        if self.is_valid_grid(grid):
            if self.solve(grid):
                self.display_solution(grid)
            else:
                messagebox.showerror("Error", "No solution exists for the given puzzle")
        else:
            messagebox.showerror("Error", "Invalid Sudoku puzzle")

    def get_grid(self):
        grid = [[0 for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                val = self.cells[row][col].get()
                if val.isdigit():
                    grid[row][col] = int(val)
        return grid

    def is_valid_grid(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] != 0:
                    num = grid[row][col]
                    grid[row][col] = 0
                    if not self.is_safe(grid, row, col, num):
                        return False
                    grid[row][col] = num
        return True

    def display_solution(self, grid):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].insert(0, str(grid[row][col]))

    def is_safe(self, grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num or grid[x][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_safe(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
