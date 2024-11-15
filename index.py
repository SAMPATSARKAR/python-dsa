# year = int(input("Enter the year "))

# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print(year,"is a leap year")
#         else:
#             print(year,"is not a leap year")
#     else:
#         print(year,"is a leap year")

# else:
#     print(year,"is not a leap year")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
a = input("enter operation (+,-,/,*): ")

if a == "+":
    result= num1 + num2
elif a == "-":
    result= num1-num2
elif a == "*":
    result= num1* num2
elif a == "/":
    if num2!=0:
        result=num1/num2
    else:
        result="Invalid, Division by Zero"
else:
    result = "invalid operation"

print(result)