#!/bin/bash
number = int(input("Enter a number to see its multiplication table:"))
for i in range(1,11):
  Y = number * i
  print(f"{number} * {i} = {Y}")
