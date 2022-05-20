# Eddie Tran
# 
# Implementation of the AC-3 algorithm specified in the textbook.
from queue import Queue

from csp import *


def ac3(csp, arcs={}):
    """ Implementation of the AC-3 algorithm specified in the textbook. 
        
        Returns False if an inconsistency is found and True otherwise.
    """
    # Initialize arcs to all arcs in CSP if empty
    if len(arcs) == 0:
        arcs = csp.constraints
    # Initialize queue
    q = Queue()
    for arc in arcs:
        q.put(arc)

    while not q.empty():
        (Xi, Xj) = q.get()
        if revise(csp, Xi, Xj):
            if len(csp.domain[Xi]) == 0: return False
            for Xk in csp.neighbors[Xi] - {Xj}:
                q.put((Xk, Xi))
    return True


def revise(csp, Xi, Xj):
    """ Implementation of the revise function used in the AC-3 algorithm
        specified in the textbook.
        
        Returns True iff we revise the domain of Xi.
    """
    revised = False
    for x in csp.domain[Xi]:
        if not consistent(csp, x, Xi, Xj):
            csp.domain[Xi] = csp.domain[Xi].replace(x, '')
            revised = True
    return revised


def consistent(csp, x, Xi, Xj):
    """ Returns False if no value y in the domain of Xj allows (x,y) to
        satisfy the Alldiff constraint between Xi and Xj, True otherwise.
    """
    return any(y != x for y in csp.domain[Xj])


def complete(csp):
    """ Returns True if every variable is assigned a value (domain is of size 1). """
    return all(len(domain) == 1 for domain in csp.domain.values())

