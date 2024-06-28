#!/bin/bash
size = int(input("Enter the size of the pattern:"))
i =1
j = 1
while i <= size:
  for j in range(0,size):
    print("*", end= "")
    j +=1
  print()
  i +=1
