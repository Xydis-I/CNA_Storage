# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:10:01 2023

@author: christian.barrett
"""

invalidInputs = [(None,None,None),("","","")]
testInputs = [(100,12,1),(110,12,2),(120,12,3),(130,12,4)]
validInputs = [1280.932804, 2996.751945, 5220.917657, 8038.528400]

def calculate_future_value(monthly_investment, yearly_interest, years):
    
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12
    
    future_value = 0.0
    for i in range(1, months + 1):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
        
    return future_value

print("%f" % calculate_future_value(130, 12, 4))

def main():
    for num in range(0, 3):
        print("Test %d: %r" % (num + 1, round(calculate_future_value(testInputs[num][0],testInputs[num][1],testInputs[num][2]), 2) == round(validInputs[num], 2)))
        
if __name__ == "__main__":
    main()