# String Reversal

def string_reversor(data):
    # this function collects the input 
    # then reverses the string by slicing it
    return data[::-1]

data = str(input("Enter a string: "))
reversed_string = string_reversor(data)
print(f"Original Data: {data}")
print(f"Reversed Data: {reversed_string}")