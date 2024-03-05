def convert_temperature(value, unit):
    if unit.lower() == 'celsius':
        fahrenheit = value * 9/5 + 32
        kelvin = value + 273.15
    elif unit.lower() == 'fahrenheit':
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
    elif unit.lower() == 'kelvin':
        celsius = value - 273.15
        fahrenheit = celsius * 9/5 + 32
    else:
        print("Invalid unit. Please enter 'celsius', 'fahrenheit', or 'kelvin'.")
        return None, None
    return fahrenheit, kelvin

def main():
    value = float(input("Enter a temperature value: "))
    unit = input("Enter the original unit of measurement (celsius, fahrenheit, or kelvin): ")
    fahrenheit, kelvin = convert_temperature(value, unit)
    if fahrenheit and kelvin:
        print(f"{value} degrees {unit} is {fahrenheit} degrees Fahrenheit and {kelvin} degrees Kelvin.")
    else:
        print("Invalid unit. Please enter 'celsius', 'fahrenheit', or 'kelvin'.")

if __name__ == "__main__":
    main()