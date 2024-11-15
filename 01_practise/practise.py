# a=input("Enter : ")
# b=sum(int(digit) for digit in str(a))
# print(b)

# def sum_of_digits(n):
#     # Convert the number to a string to iterate through each digit
#     return sum(int(digit) for digit in str(n))

# # Test cases
# print(sum_of_digits(123))  # Expected Output: 6
# print(sum_of_digits(896))  # Expected Output: 23

with open(example.txt, 'r') as file:
    lines = file.readlines()

print(lines)
