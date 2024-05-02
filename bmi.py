def calculate_bmi(height, weight):
    print("Height=" +str(height))
    print("Weight=" +str(weight))
    
    bmi=(weight)/(height*height)
    print("BMI=" +str(bmi))

    # BMI RANGE
    if bmi>25.0:
        print("OVER WEIGHT LOSE WEIGHT CUNT")
    elif bmi>=18.5 and bmi<=25.0:
        print("GOOD KEEP IT UP")
    else:
        print("UNDER WEIGHT EAT MORE U CUNT")



calculate_bmi(weight=57,height=1.73)