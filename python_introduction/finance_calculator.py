#!/bin/bash
monthly_income = int(input("Enter your monthly income:"))
monthly_expence = int(input("Enter your total monthly expenses:"))
monthly_saving = monthly_expence - monthly_income
Projected_Savings = monthly_savings * 12 + (monthly_saving * 12 * 0.05)
print("Your monthly savings are ${}".format(monthly_saving))
print("Projected savings after one year, with interest, is: ${}".format(Projected_Savings))
