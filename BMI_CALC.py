height = input('Enter the height in meters: ')
weight = input('Enter the weight in kg: ')

# BMI = weight(kg)/square(height) m**2

n_height = float(height)
n_weight = float(weight)
BMI = n_weight / (n_height ** 2)
print("BMI is", BMI)
