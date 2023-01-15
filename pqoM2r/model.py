from cashflower import assign, ModelVariable

from pqoM2r.input import policy, runplan


calendar_month = ModelVariable(modelpoint=policy)
calendar_year = ModelVariable(modelpoint=policy)


@assign(calendar_month)
def calendar_month_formula(t):
    valuation_month = runplan.get("valuation_month")

    if t == 0:
        return valuation_month
    else:
        if calendar_month(t-1) == 12:
            return 1
        else:
            return calendar_month(t-1) + 1


@assign(calendar_year)
def calendar_year_formula(t):
    valuation_year = runplan.get("valuation_year")

    if t == 0:
        return valuation_year
    else:
        if calendar_month(t-1) == 12:
            return calendar_year(t-1) + 1
        else:
            return calendar_year(t-1)
