
''' 	SAT solver based on DPLL and Jeroslow Wang 2 heuristic branch
        CS500-Logic in Computer-Fall Semester 2021 
        Mahdi Ali pour

'''

import timeit
import sys
import os
import matplotlib.pyplot as plt
from satSolver1 import *

# Unit propagation 
def unitPro(formula):
    assignment = []
    unit_clauses = [c for c in formula if len(c) == 1]
    while unit_clauses:
        unit = unit_clauses[0]
        formula = boolConstPro(formula, unit[0])
        assignment += [unit[0]]
        if formula == -1:
            return -1, []
        if not formula:
            return formula, assignment
        unit_clauses = [c for c in formula if len(c) == 1]
    return formula, assignment


# Boolean Constraint Propagation (boolConstPro)
# to simplify the set of clauses
def boolConstPro(formula, unit):
    simplified = []
    for clause in formula:
        if unit in clause:
            continue
        if -unit in clause:
            new_clause = [x for x in clause if x != -unit]
            if not new_clause:
                return -1
            simplified.append(new_clause)
        else:
            simplified.append(clause)
    return simplified



def backtracking(formula, assignment):
    formula, unit_assignment = unitPro(formula)
    assignment = assignment + unit_assignment 
    if formula == -1:
        return []
    if not formula:
        return assignment
    if hiur == 'mostAppear':
        variable1 = mostAppear(formula)
    else:
        variable1 = jeroslow_wang_2_sided(formula)
    solution = backtracking(boolConstPro(formula, variable1), assignment + [variable1])
    if not solution:
        solution = backtracking(boolConstPro(formula, -variable1), assignment + [-variable1])
    return solution


# Find the variable that appears more 
def jeroslow_wang_2_sided(formula):
    counter = get_weighted_abs_counter(formula)
    return max(counter, key=counter.get)

def get_weighted_abs_counter(formula, weight=2):
    counter = {}
    for clause in formula:
        for literal in clause:
            literal = abs(literal)
            if literal in counter:
                counter[literal] += weight ** -len(clause)
            else:
                counter[literal] = weight ** -len(clause)
    return counter


# Reading from CNF file and returns a set of clauses
def parseCnfFile(cnf_file):
    clauses = []
    for line in open(cnf_file):
        if line.startswith('c') or line.startswith('p'):
            continue
        clause = [int(x) for x in line[:-2].split()]
        clauses.append(clause)
    return clauses
    
def main():
    
    clauses = parseCnfFile('cnf/'+entry)
    solution = backtracking(clauses, [])

    if solution:
        print('Formula '+entry+' is SATISFIABLE')        
    else:
        print('Formula '+entry+' is UNSATISFIABLE')

def parse(filename):
    for line in open(filename):
        if line.startswith('p'):
            return line.split()[2]
            
                     
if __name__ == '__main__':
    
    entries = os.listdir('cnf/')
    
    timespent = []
    numVar = []
    hiur = 'jw'
    print('\n==========================\n',
    'SAT Solver 2 result: \n==========================')
    for entry in entries:
        timespent.append(timeit.timeit(setup = '',
                     stmt = main,
                     number = 1))
        numVar.append(parse('cnf/'+entry))            
      
      
    y1 = timespent
    x1 = numVar
    plt.plot(x1, y1, label = "Jeroslow Wang 2")    
    timespent = []
    numVar = []
    hiur = 'mostAppear'
    print('\n==========================\n',
    'SAT Solver 1 result: \n==========================')
    for entry in entries:
        timespent.append(timeit.timeit(setup = '',
                     stmt = main,
                     number = 1))
        numVar.append(parse('cnf/'+entry))
    
    y2 = timespent
    x2 = numVar
    plt.plot(x2, y2, label = "most appear")

    plt.xlabel('number of variables')
    plt.ylabel('time in second')

    plt.title('Time spent on heuristic branch')

    plt.legend()
    plt.show()
