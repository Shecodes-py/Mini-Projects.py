# Fibonacci series

def Fibonnaci_series(count: int):
    first_term , second_term = 0 ,1 
    series = [first_term, second_term]
    for i in range(count - 2):
        temp = second_term
        second_term = second_term + first_term
        first_term = temp
        series.append(second_term)
    
    return series

user_input = int(input("Welcome to the Fibonacci Series Program,\nWhere would you like me to stop?: "))
series = Fibonnaci_series(user_input)
print(series)