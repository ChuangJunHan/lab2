def calculate_bmi(height, weight):
    print("Height=" +str(height))
    print("Weight=" +str(weight))
    
    bmi=(weight)/(height*height)
    print("BMI=" +str(bmi))

    # BMI RANGE
    if bmi>25.0:
        print("OVER WEIGHT LOSE WEIGHT CUNT")
        return 1
    elif bmi>=18.5 and bmi<=25.0:
        print("GOOD KEEP IT UP")
        return 0
    else:
        print("UNDER WEIGHT EAT MORE U CUNT")
        return -1



calculate_bmi(weight=57,height=1.73)