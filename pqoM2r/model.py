from cashflower import assign, ModelVariable

from pqoM2r.input import policy, runplan


calendar_month = ModelVariable(modelpoint=policy)
calendar_year = ModelVariable(modelpoint=policy)


@assign(calendar_month)
def calendar_month_formula(t):
    # PLACE FOR YOUR CODE
    pass


@assign(calendar_year)
def calendar_year_formula(t):
    # PLACE FOR YOUR CODE
    pass
