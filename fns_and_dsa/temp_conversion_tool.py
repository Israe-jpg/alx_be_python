FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 \/ 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
         temperature = float(input("Enter the temperature to convert: "))
         temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
         if temp_type == 'C':
             converted_temp = convert_to_fahrenheit(temperature)
             print(f"{temperature}°C is {converted_temp}°F")
         elif temp_type == 'F':
             converted_temp = convert_to_celsius(temperature)
             print(f"{temperature}°F is {converted_temp}°C")
         else:
             raise ValueError("Invalid temperature type. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
         
    except ValueError as e:
        print(f"Invalid temperature. Please enter a numeric value. Error: {e}")

if __name__ == "__main__":
    main()
                  
