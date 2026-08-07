def main():
    #Get the user's weight in kilograms
    weight = float(input("Enter your weight (kg): "))
    #Get the user's height in metres
    height = float(input("Enter your height (m): "))
    #Calculate BMI，BMI = weight ÷ height²
    bmi = weight / (height * height)
    # Display the BMI rounded to 2 decimal places
    print("Your BMI is:", round(bmi, 2))

    # Determine BMI category
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 25:
        print("You have a normal weight.")
    elif 25 <= bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")
main()

if __name__ == "__main__":
    main()