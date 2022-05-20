from pathlib import Path
from time import time

import ac3
from csp import CSP
import backtrack

if __name__ == '__main__':
    p = Path('.').rglob('*.txt')
    easy_count = 0
    med_count = 0
    hard_count = 0
    verified_count = 0
    total_time = 0
    ac3_solved = 0
    
    for path in p:
        puzzle = CSP(str(path))
        start = time()
        ac3.ac3(puzzle)
        if not ac3.complete(puzzle):
            backtrack.backtracking_search(puzzle)
        end = time()
        total_time += end - start
        
        if puzzle.valid():
            if str(path.parent) == 'easy': easy_count += 1
            if str(path.parent) == 'medium': med_count += 1
            if str(path.parent) == 'hard': hard_count += 1
            
    print(easy_count, 'out of 15 easy puzzles solved')
    print(med_count, 'out of 15 medium puzzles solved')
    print(hard_count, 'out of 16 hard puzzles solved')
    print(easy_count + med_count + hard_count, 'out of 46 puzzles solved')
    print('Average time:', total_time / 46)

