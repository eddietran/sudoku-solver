# Eddie Tran
#
# Implementation of the backtracking search algorithm in the textbook.
#
# Backtracking algorithm employs the minimum remaining values (most
# constrained variable) heuristic.
#
# Inference step is based on the Maintaining Arc Consistency algorithm
# in the textbook.
from copy import deepcopy

from csp import *
from ac3 import ac3


def backtracking_search(csp):
    """Implementation of the backtracking search algorithm in the textbook.
    
    Returns a solution or no solution (empty dictionary).
    """
    assignment = {var: value for var, value in csp.domain.items() if len(value) == 1} #  Pre-assign known values
    return backtrack(csp, assignment)


def backtrack(csp, assignment):
    """Implementation of the backtracking algorithm in the textbook.
    
    Returns a solution or no solution (empty dictionary).
    """
    if complete(assignment): return assignment
    var = select_unassigned_variable(csp, assignment)
    for value in order_domain_values(csp, var, assignment):
        if consistent(csp, var, value, assignment):
            original_domain = deepcopy(csp.domain) #  Copy original csp state
            assignment[var] = value
            inferences = inference(csp, assignment, var, value)
            if inferences != False:
                #  Inferences are already added to csp during the inference step
                result = backtrack(csp, assignment)
                if result != {}: return result
            csp.domain.update(original_domain) #  Remove inferences from csp if inconsistency detected
            del assignment[var]
    return {}


def complete(assignment):
    """ Returns True if every variable is assigned a value (domain is of size 1). """
    return len(assignment.keys()) == 81 and all(len(domain) == 1 for domain in assignment.values())


def select_unassigned_variable(csp, assignment):
    """Returns an unassigned variable using the minimum remaining values
    (also known as most constrained variable) heuristic.
        
    Degree (most constraining variable) heuristic was not used since
    every variable has an equal number of constraints (20).
    """
    unassigned_vars = {var: len(domain) for var, domain in csp.domain.items() if var not in assignment.keys()}
    return min(unassigned_vars, key=unassigned_vars.get)


def order_domain_values(csp, var, assignment):
    """ Returns an order for the assigned variable.
    
    Least constraining value heuristic was not used because it was slower
    than using no heuristic.
    """
    return csp.domain[var]

    #  Least constraining value heuristic
    #value_count = {value: 0 for value in '123456789'}
    #for neighbor in csp.neighbors[var]:
        #for value in csp.domain[neighbor]:
            #value_count[value] += 1
    #return sorted((value for value in value_count.keys()), key=value_count.get)


def consistent(csp, var, value, assignment):
    """ Returns True if the value satisfies the Alldiff constraint
    with the constraints of the variable.
    """
    return all(assignment[neighbor] != value for neighbor in csp.neighbors[var] if neighbor in assignment.keys())


def inference(csp, assignment, var, value):
    """ Implementation of the Maintaining Arc Consistency (MAC) algorithm specified in the textbook. """
    csp.domain[var] = value
    arcs = {(Xj, Xi) for Xj, Xi in csp.constraints if Xi == var and Xj not in assignment}
    return ac3(csp, arcs)

