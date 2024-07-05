#!/bin/bash
def perform_operation(num1, num2, operation):
  if operation == "add":
    return num1 +num2
  elif operation == "subtract":
    return num1 - num2
  elif operation == "multiply":
    return num1 * num2
  elif operation == "divide":
    if num2 == 0:
      print(f"{num1} can't be divide by 0 ")
    elif num2 != 0:
      return num1 / num2

