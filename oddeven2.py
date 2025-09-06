def check_parity(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = 7
parity = check_parity(num)
print(f"The number {num} is {parity}.")
