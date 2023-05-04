def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/height**2
    print(bmi)
    if bmi<18.5:
        x = -1
        print(x)
    elif 18.5<=bmi<=25.0:
        y = 0
        print(y)
    elif bmi>=25.0:
        z = 1
        print(z)
calculate_bmi(weight=57, height=1.73)

