def get_integer_input() -> int:
 
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
 
    if number % 2 == 0:
        return f"{number} is an Even number."
    return f"{number} is an Odd number."

user_number = get_integer_input()
result_message = check_even_odd(user_number)

print(result_message)
