"""Russell Deady
Project to perform different weight conversions
1/28/22"""


def convertWeight(weight, str1, str2):
    if (str1 == "pounds"):
        if (str2 == "kilograms"):
            weight = weight * 0.453592
            return weight
        if (str2 == "grams"):
            weight = weight * 453.592
            return weight
        if (str2 == "milligrams"):
            weight = weight * 453592
            return weight
        if (str2 == "stones"):
            weight = weight * 0.0714286
            return weight
        if (str2 == "ounces"):
            weight = weight * 16
            return weight
    elif (str1 == "kilograms"):
        if (str2 == "pounds"):
            weight = weight * 2.20462
            return weight
        if (str2 == "grams"):
            weight = weight * 1000
            return weight
        if (str2 == "milligrams"):
            weight = weight * 1000000
            return weight
        if (str2 == "stones"):
            weight = weight * 0.157473
            return weight
        if (str2 == "ounces"):
            weight = weight * 35.274
            return weight
    elif (str1 == "grams"):
        if (str2 == "pounds"):
            weight = weight * 0.00220462
            return weight 
        if (str2 == "kilograms"):
            weight = weight * 0.001
            return weight
        if (str2 == "milligrams"):
            weight = weight * 1000
            return weight
        if (str2 == "stones"):
            weight = weight * 0.000157473
            return weight 
        if (str2 == "ounces"):
            weight = weight * 0.035274
            return weight
    elif (str1 == "milligrams"):
        if (str2 == "pounds"):
            weight = weight * 0.000002204622622
            return weight 
        if (str2 == "kilograms"):
            weight = weight / 1000000
            return weight 
        if (str2 == "grams"):
            weight = weight * 0.001
            return weight 
        if (str2 == "stones"):
            weight = weight * 0.001
            weight = weight * 0.000157473
            return weight 
        if (str2 == "ounces"):
            weight = weight * 0.001
            weight = weight * 0.035274
            return weight 
    elif (str1 == "stones"):
        if (str2 == "pounds"):
            weight = weight * 14
            return weight 
        if (str2 == "kilograms"):
            weight = weight * 6.35029
            return weight 
        if (str2 == "grams"):
            weight = weight * 6350.29
            return weight 
        if (str2 == "milligrams"):
            weight = weight * 6350.29
            weight = weight * 1000
            return weight 
        if (str2 == "ounces"):
            weight = weight * 224
            return weight 
    elif (str1 == "ounces"):
        if (str2 == "pounds"):
            weight = weight * 0.0625
            return weight 
        if (str2 == "kilograms"):
            weight = weight * 0.0283495
            return weight
        if (str2 == "grams"):
            weight = weight * 28.3495
            return weight
        if (str2 == "milligrams"):
            weight = weight * 28349.5
            return weight
        if (str2 == "stones"):
            weight = weight * 0.00446429
            return weight
    else:
        return 0



def main():

    currentWeight = 0
    convertedWeight = 0
    userInput = ""
    currentTypeOfWeight = ""
    desiredTypeOfWeight = ""

    print("Welcome to the weight converter!")
    print("When entering the kind of unit you would like, include the s at the end (enter grams instead of gram")
    print("This program handles pounds, kilograms, grams, milligrams, ounces, and stones.")
    
    while (userInput != 'q'):
        currentTypeOfWeight = input("Enter the unit of weight you are currently using such as pounds or grams: ")
        currentWeight = input("Enter the amount that you are converting, positive numbers only: ")
        currentWeight = float(currentWeight)
        desiredTypeOfWeight = input("Enter the unit of weight you want to convert to: ")

        convertedWeight = convertWeight(currentWeight, currentTypeOfWeight,desiredTypeOfWeight)
        if (convertedWeight == 0):
            print("Some of your input was invalid this time, so the conversion couldn't be made.")
        else:
            print("The weight is now",convertedWeight,"and is in the unit",desiredTypeOfWeight)
        userInput = input("Enter q if you are done converting, or anything else to continue: ")

    print()
    print("Thank you for using the program!")
    print()


main()
