# Eddie Tran
#
# Main module of the sudoku solver.
from csp import CSP
import ac3
import backtrack


if __name__ == '__main__':
    filename = input('Enter filename of sudoku puzzle: ')
    puzzle = CSP(filename)
    ac3.ac3(puzzle) # Run AC-3 before backtracking
    if not ac3.complete(puzzle):
        backtrack.backtracking_search(puzzle)
    puzzle.display()

