print("welcome to kanna hospital,")
input("what is your name ")
height = float(input("what is your height ?"))
weight = int(input("what is your weight ?"))

bmi = weight / (height*height)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are under weight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly over weight.")
elif bmi < 35:
    print(f"Your BMI is{bmi}, You are obese.")
else:
    print(f"Your BMI is {bmi}, You are clinically obese.")
