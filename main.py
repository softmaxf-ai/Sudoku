"""This project is a classic Sudoku Game,
    - Random configure a Sudoku Puzzle
    - Give Puzzle to an optimizer
    - Optimizer Solves Puzzle """
from random import sample
import numpy as np


class SudokuRiddler():
    def __init__(self, sudoku_base):
        self.solution = None
        self.sudoku_base = sudoku_base

    def setup_sudoku(self):
        # call Solution function
        self.setup_solution()

    def setup_solution(self):
        """ Source https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python """
        side = self.sudoku_base**2

        # pattern for a sudoku_baseline valid solution
        def pattern(r, c): return (sudoku_base * (r % sudoku_base) + r // sudoku_base + c) % side
        # randomize rows, columns and numbers (of valid sudoku_base pattern)
        def shuffle(s): return sample(s, len(s))

        rSudoku_base = range(sudoku_base)
        rows = [g * sudoku_base + r for g in shuffle(rSudoku_base) for r in shuffle(rSudoku_base)]
        cols = [g * sudoku_base + c for g in shuffle(rSudoku_base) for c in shuffle(rSudoku_base)]
        nums = shuffle(range(1, sudoku_base * sudoku_base + 1))

        # produce board using randomized sudoku_baseline pattern
        solution = [[nums[pattern(r, c)] for c in cols] for r in rows]
        self.solution = np.array(solution)


if __name__ == '__main__':
    sudoku_base = 3
    puzzler = SudokuRiddler(sudoku_base)
    puzzler.setup_sudoku()
