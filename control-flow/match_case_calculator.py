#!/bin/bash
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = (input("hoose the operation (+, -, *, /):"))
result = 0
match operation:
  case "+":
    result= num1 + num2
  case "-":
    result= num1 - num2
  case "*":
    result= num1 * num2
  case "/":
    if num2 == 0:
        print(f"{num1} can't be divided by 0")
    elif num2 != 0:
        result = num1 / num2
print(f"result is {result}.")

