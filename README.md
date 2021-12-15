# SAT Solver

Two SAT solvers based on the DPLL algorithm, which differ in the heuristic they use to select the variable to branch on. 

Both SAT solvers take their input in DIMACS CNF format. 

**SAT Solver 1** branchs on the unassigned variable that **appears in the most number of clauses**. 

**SAT Solver 2** uses a **Jeroslow Wang 2** heuristic branch choose the branching variable 

SAT Solver 2 outperforms SAT Solver 1 in most of the cases

## Running

For running both solvers. Simply copy cnf files in cnf directory and run satSolver2.py.
```
$ python satSolver2.py
```
