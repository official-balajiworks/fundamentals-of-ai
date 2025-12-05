variables = ["X", "Y", "Z"]
domains = {
    "X": [1, 2, 3],
    "Y": [1, 2, 3],
    "Z": [1, 2, 3]
}
def check_constraints(assign):
    if "X" and "Y" in assign:
        if assign["X"] == assign["Y"]:
                return False
    if "Y" and "Z" in assign:
        if assign["Y"] >= assign["Z"]:
            return False
    if "X" and "Z" in assign:
        if assign["X"] + assign["Z"] != 4:
            return False
    return True
def backtrack(assignment, solutions):
    if len(assignment) == len(variables):
        solutions.append(assignment.copy())
        return
    var = next(v for v in variables if v not in assignment)
    for value in domains[var]:
        assignment[var] = value
        if check_constraints(assignment):
            backtrack(assignment, solutions)
        del assignment[var]
solutions = []
backtrack({}, solutions)
for sol in solutions:
    print(sol)