#!/bin/bash
from datetime import datetime, timedelta
def display_current_datetime():
  current_date = datetime.now()
  formated_daytime = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(formated_daytime)

def calculate_future_date():
  added_days = int(input("enter the futur date"))
  curnt_day= datetime.now()
  future_date = curnt_day + timedelta(days=added_days)
  formated_future_date = future_date.strftime("%Y-%m-%d")
  print(formated_future_date)

display_current_datetime()
calculate_future_date()


