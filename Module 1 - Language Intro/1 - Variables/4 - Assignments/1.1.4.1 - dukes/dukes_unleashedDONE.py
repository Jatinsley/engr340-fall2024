"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""
"Interest Rate = 5%"
"In-State Cost = $33,276"
"Out-of-State Cost = $50,630"
interest_rate = 0.05
instatecost = 33276
outofstatecost = 50630

"How many years since 2024-2025 Data?"
years = (1)

"In-state Inflation Adjustment"
instatecostadjusted = ( instatecost * .05 * years ) + instatecost
in_state_gift = instatecostadjusted
print("Cost for an In-State student for", (2023+years),"-",(2024+years), "is approximately $",in_state_gift)
"Out-of-State Inflation Adjustment"
outofstatecostadjusted = ( outofstatecost * .05 * years ) + outofstatecost
out_state_gift = outofstatecostadjusted
print("Cost for an Out-Of-State student for", (2023+years),"-",(2024+years), "is approximately $", out_state_gift)