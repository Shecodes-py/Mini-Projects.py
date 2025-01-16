#  Temperature Converter
print("The Temperature Converter!")
def C_to_F(temp: int, unit: str) -> str:
    if unit.lower() == "f": 
        # Converts from Fahrenheit to Celsuis
        data = (5/9) * (temp - 32)
        return f"{data:.3f}°C"
    elif unit.lower() == "c":
        # Converts from Celsius to Fahrenheit
        data = (temp * (9/5)) + 32
        return f"{data:.2f}°F"
    else:
        return "Invalid unit. Please input 'C' or 'F'."
    
# User's Input
unit = input("Input the Temperature's unit (C/F): ")
temperature = float(input("Input Temperature: "))
Results = C_to_F(temperature, unit)
print(Results)
