#             DONE  100%
#             I edited in 31\1\2021
num1 = int(input("Enter your First number : "))
num2 = int(input("Enter your second number : "))
sing = input("Enter the Mathematical Sign : ")

if sing == '+':
    New_number = num1 + num2
    print(New_number)
elif sing == '*':         # I wrote it if
    New_number = num1 * num2
    print(New_number)
elif sing == '/':
    New_number = num1 / num2
    print(New_number)
elif sing == '-':
    New_number = num1 - num2
    print(New_number)
