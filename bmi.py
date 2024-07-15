def BMI(weight, height):
    bmi = (weight / (height * height)) * 10000
    return bmi

def category(bmi):
    if bmi <= 18.4:
        return "under weight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal"
    elif bmi >= 25 and bmi <= 39.9:
        return "over weight"
    else:
        return "obesity"

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    
    if weight < 0 or height < 0:
        print("Please enter valid input")
    else:
        bmi = BMI(weight, height)
        print("Your body mass index is:", bmi)
        print("Category:", category(bmi))
except ValueError:
    print("Value error")
