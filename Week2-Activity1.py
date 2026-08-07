class BMI:
    def calculate(self):
        bmi = self.weight / (self.height * self.height)
        return bmi
    def display(self):
        print("Your BMI is:", round(self.calculate(), 2))
        print(self.category())
    def category(self):
            bmi = self.calculate()
            if bmi < 18.5:
                return "You are underweight."
            elif 18.5 <= bmi < 25:
                return "You have a normal weight."
            elif 25 <= bmi < 30:
                return "You are overweight."
            else:
                return "You are obese."

def main():
    person = BMI()

    #Get the user's weight in kilograms
    person.weight = float(input("Enter your weight (kg): "))
    #Get the user's height in metres
    person.height = float(input("Enter your height (m): "))
    person.display()
    #Calculate BMI，BMI = weight ÷ height²
    #bmi = weight / (height * height)
    # Display the BMI rounded to 2 decimal places
    #print("Your BMI is:", round(bmi, 2))

    # Determine BMI category
    #if bmi < 18.5:
        #print("You are underweight.")
    #elif 18.5 <= bmi < 25:
        #print("You have a normal weight.")
    #elif 25 <= bmi < 30:
        #print("You are overweight.")
    #else:
        #print("You are obese.")
main()