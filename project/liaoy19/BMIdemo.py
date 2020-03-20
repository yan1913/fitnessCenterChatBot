def fun(BMI):
    if BMI < 15:
        return "Very severely underweight"
    elif 15 < BMI < 16:
        return "Severely underweight"
    elif 16 < BMI < 18.5:
        return "Underweight"
    elif 18.5 < BMI < 25:
        return "Normal (healthy weight)	"
    elif 25 < BMI < 30:
        return "Overweight"
    elif 30 < BMI < 35:
        return "Obese Class I (Moderately obese)"
    elif 35 < BMI < 40:
        return "Obese Class II (Severely obese)	"
    else:
        return "Obese Class III (Very severely obese)	"


def calBMI(weight,height ):
    BMI = weight / (height * height)
    return BMI

