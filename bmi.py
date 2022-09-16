import sys

# User need to input these 3 parameteres
height = float(input("Enter height in meters: "))
# weight = float(input("Enter weight in kg: "))
bmi = float(input("Enter BMI score: "))

if height <= 0 or bmi <= 0:
   print("the input value need to be higher than 0 and positive number"
   sys.exit()


# the formula to calculate bmi value
# bmi = weight/(height**2) 
weight = bmi * (height**2) 

print("Your BMI is: {0} and you are: ".format(bmi), end='')
print(f"Your height is: {height}", end='')
print(f"Your weight is: {weight}", end='')

#conditions
print("Checking condition .....!")
if ( bmi < 16):
   print(f"BMI: {bmi} | condition: severely underweight")
   print(f"You'll have to weight {weight}")

elif ( bmi >= 16 and bmi < 18.5):
   print(f"BMI: {bmi} | condition: underweight")
   print(f"You'll have to weight {weight}")

elif ( bmi >= 18.5 and bmi < 25):
   print(f"BMI: {bmi} | condition: Healthy")
   print(f"You'll have to weight {weight}")

elif ( bmi >= 25 and bmi < 30):
   print(f"BMI: {bmi} | condition: overweight")
   print(f"You'll have to weight {weight}")

elif ( bmi >=30):
   print(f"BMI: {bmi} | condition: severely overweight")
   print(f"You'll have to weight {weight}")
