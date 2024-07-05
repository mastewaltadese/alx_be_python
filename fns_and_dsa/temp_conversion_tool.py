#!/bin/bash
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
   result = (fahrenheit + 32) *  FAHRENHEIT_TO_CELSIUS_FACTOR 
   print(f"{tempreture}°F is {result}°C ")
def convert_to_fahrenheit(celsius):
   result =(celsius - 32) *  CELSIUS_TO_FAHRENHEIT_FACTOR 
   print(f"{tempreture}°C is {result}°F ")
tempreture = int(input("Enter the temperature to convert:"))
convert_to = input("Is this temperature in Celsius or Fahrenheit? (C/F):").lower()
if convert_to == "f":
   convert_to_celsius(tempreture)
elif convert_to == "c":
   convert_to_fahrenheit(tempreture)
else:
   print("Invalid temperature. Please enter a numeric value.")      
