# Eddie Tran
#
# Representation of the sudoku puzzle as a constraint satisfaction problem.


class CSP:


    __slots__ = ['cells', 'neighbors', 'domain', 'constraints']


    def __init__(self, filename):
        """ Takes a puzzle file in the format specified in the homework. """
        # Cells of the sudoku puzzle
        self.cells = list(x+y for x in 'ABCDEFGHI' for y in '123456789')
        # Domain of each cell in the puzzle
        self.domain = self._parsePuzzle(filename)
        # Initialize neighbors (constraints) assigned to each variable
        self.neighbors = {x: {y for y in self.cells if (x != y and (x[0] == y[0] or x[1] == y[1]))} for x in self.cells}
        # Add neighbors (constraints) for boxes
        for cell in self.cells:
            row, col = tuple(cell)
            if row in 'ABC':
                if col in '123': self.neighbors[cell].update(x+y for x in 'ABC' for y in '123' if x+y != cell)
                if col in '456': self.neighbors[cell].update(x+y for x in 'ABC' for y in '456' if x+y != cell)
                if col in '789': self.neighbors[cell].update(x+y for x in 'ABC' for y in '789' if x+y != cell)
            if row in 'DEF':
                if col in '123': self.neighbors[cell].update(x+y for x in 'DEF' for y in '123' if x+y != cell)
                if col in '456': self.neighbors[cell].update(x+y for x in 'DEF' for y in '456' if x+y != cell)
                if col in '789': self.neighbors[cell].update(x+y for x in 'DEF' for y in '789' if x+y != cell)
            if row in 'GHI':
                if col in '123': self.neighbors[cell].update(x+y for x in 'GHI' for y in '123' if x+y != cell)
                if col in '456': self.neighbors[cell].update(x+y for x in 'GHI' for y in '456' if x+y != cell)
                if col in '789': self.neighbors[cell].update(x+y for x in 'GHI' for y in '789' if x+y != cell)
        # Arcs (Alldiff constraints) of each variable
        self.constraints = {(var, neighbor) for var, neighbors in self.neighbors.items() for neighbor in neighbors}


    def _parsePuzzle(self, filename):
        """ Parses a puzzle file and returns a dictionary representing the domain of each cell. 
            Domain is represented with a string since it is only the digits 1-9.
        """
        with open(filename) as f:
            vals = f.read().split()
            return {key: val if val != '0' else '123456789' for key, val in zip(self.cells, vals)}


    def display(self):
        """ Displays the puzzle. """
        i = 1
        for cell in self.cells:
            print(self.domain[cell], end=" ")
            if i % 9 == 0:
                print()
            i += 1


    def valid(self):
        """ Returns True if the puzzle solution is valid. """
        return all(len(self.domain[cell]) == 1 and self.domain[cell] != self.domain[neighbor] for cell in self.cells for neighbor in self.neighbors[cell])

