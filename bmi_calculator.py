print("Let's calculate the BMI:")
height = input("Please enter your height in centimeter: ")
intHei = int(height)
height_in_meter = intHei/100
weight = input("Please enter your weight in kilogram: ")
floWei = float(weight)

bmi = floWei/(height_in_meter*height_in_meter)
formatBmi = "{:.2f}".format(bmi)

print("The BMI of your body is " + str(formatBmi) + "kg/m^2")

if(float(formatBmi) > 18.4 and float(formatBmi) < 25):
    print("Your BMI falls in Normal range\nThank you!")
else:
    print("Your BMI falls in Abnormal range\nThank you!")