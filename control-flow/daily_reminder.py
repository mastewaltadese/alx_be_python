#!/bin/bash
task = input("Enter your task:").lower()
Priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()
match Priority:
  case "high":
    if time_bound == "yes":
      print(f"Reminder: {task} is a {Priority} priority task that requires immediate attention today!")
    elif time_bound == "no":
      print(f"Reminder: {task} is a {Priority} priority task. Consider completing it when you have free time.")
  case "medium":
    if time_bound == "yes":
      print(f"Reminder: {task} is a {Priority} priority task that requires immediate attention today!")
    elif time_bound == "no":
      print(f"Reminder: {task} is a {Priority} priority task. Consider completing it when you have free time.")
  case "low":
    if time_bound == "yes":
      print(f"Note: {task} is a {Priority} priority task that requires immediate attention today!")
    elif time_bound == "no":
      print(f"Note: {task} is a {Priority} priority task. Consider completing it when you have free time.")
