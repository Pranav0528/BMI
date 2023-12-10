height = input('Enter the height in meters: ')
weight = input('Enter the weight in kg: ')

# BMI = weight(kg)/square(height) m**2

n_height = float(height)
n_weight = float(weight)
BMI = n_weight / (n_height ** 2)
if BMI <18.5:
    print(f"your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"your BMI is {BMI}, you have a normal weight")
elif BMI < 30:
    print(f"your BMI is {BMI}, you are slightly overweight")
elif BMI < 35:
    print(f"your BMI is {BMI}, you are obese.")
else:
    print(f"your BMI is {BMI}, you are clinicallt obese")