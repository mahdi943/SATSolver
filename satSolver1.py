
''' 	SAT solver based on DPLL and Most Appear heuristic branch
        CS500-Logic in Computer-Fall Semester 2021 
        Mahdi Ali pour

'''

import timeit
import sys
import os


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
    variable = mostAppear(formula)
    solution = backtracking(boolConstPro(formula, variable), assignment + [variable])
    if not solution:
        solution = backtracking(boolConstPro(formula, -variable), assignment + [-variable])
    return solution


# Find the variable that appears more in clauses

def get_counter(formula):
    counter = {}
    for clause in formula:
        for literal in clause:
            if literal in counter:
                counter[literal] += 1
            else:
                counter[literal] = 1
    return counter

def mostAppear(formula):
    counter = get_counter(formula)
    return max(counter, key=counter.get)


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
        print('\nFormula '+entry+' is SATISFIABLE')        
    else:
        print('\nFormula '+entry+' is UNSATISFIABLE')
                     
if __name__ == '__main__':
    print('==========================\n',
    'SAT Solver 1 result: \n==========================')
    entries = os.listdir('cnf/')    
    for entry in entries:
        print ('Time spent: ' , timeit.timeit(setup = '',
                     stmt = main,
                     number = 1), ' sec')