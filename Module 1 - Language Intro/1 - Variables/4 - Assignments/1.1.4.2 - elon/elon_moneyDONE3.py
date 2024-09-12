"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 1-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""
from array import array
### all your code below ###
Principal = 33
ten_year_interest = .0396
twenty_year_interest = .0432

"Setting up for 10-year-rate"
"number of subperiods and years"
number = 1
t = 10

"Compounding Interest 10Y"
Ten_Year_Compound_Interest = [(1+(ten_year_interest/number))**(t*number)-1]
"Final Value 10Y"
Ten_Year_Compound_Interest = Ten_Year_Compound_Interest[0]
ten_year_final = 1000000000 * (33 * Ten_Year_Compound_Interest)

"Setting up for 20-year-rate"
"number of subperiods and years"
n = 1
t2 = 20

"Compounding Interest 20Y"
Twenty_Year_Compound_Interest = [(1+(twenty_year_interest/number))**(t2*number)-1]
"Final Value 20Y"
Twenty_Year_Compound_Interest = Twenty_Year_Compound_Interest[0]
twenty_year_final = 1000000000 * (33 * Twenty_Year_Compound_Interest)

# final answer for 10-year
print("Ten year final is $",ten_year_final)
# final answer for 20-year
print("Twenty year final is $",twenty_year_final)