from cashflower import assign, ModelVariable

from pqoM2r.input import policy


age = ModelVariable(modelpoint=policy)


@assign(age)
def age_formula(t):
    # PLACE FOR YOUR CODE
    pass
