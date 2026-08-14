class TemperatureConverter:
# Initialize the temperature converter with the user's input
    def __init__(self, temperature):
        self.temperature = temperature

# Check whether the user's input has a valid format
    def is_valid(self):
        return (
            len(self.temperature) >= 2
            and self.temperature[0] in ["F", "C"]
            and self.temperature[1:].replace(".", "", 1).replace("-", "", 1).isdigit()
        )

 # Convert Celsius to Fahrenheit
    def celsius_to_fahrenheit(self):
        temperature = float(self.temperature[1:])
        fahrenheit = round((temperature * 9 / 5) + 32, 2)
        return f"{self.temperature} degrees Celsius is converted to {fahrenheit} degrees Fahrenheit"

# Convert Fahrenheit to Celsius
    def fahrenheit_to_celsius(self):
        temperature = float(self.temperature[1:])
        celsius = round((temperature - 32) * 5 / 9, 2)
        return f"{self.temperature} degrees Fahrenheit is converted to {celsius} degrees Celsius"

# Determine which conversion to perform
    def convert(self):
        if not self.is_valid():
            return "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."
        if self.temperature[0] == "C":
            return self.celsius_to_fahrenheit()
        else:
            return self.fahrenheit_to_celsius()


def main():
 # Keep asking for input until the user enters a valid temperature
    while True:
        temperature = input("Enter a temperature (e.g., F51 or C11): ")

        converter = TemperatureConverter(temperature)

        print(converter.convert())

        if converter.is_valid():
            break

if __name__ == "__main__":
    main()