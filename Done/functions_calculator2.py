#                   DONE 100%

name = input("Welcome, Enter your surname please : ")
user_gender = input("write your gender : ")

if user_gender[0] == 'm':
    gender = "Mr."       # I DON'T KNOW WHT THIS LINE CANT WORK RIGHT______________
elif user_gender[0] == 'f':
    gender = "Mrs."
else:                   # In case the user didn't write the gender right.
    gender = ""

print(f"Welcome {gender}{name} in AMH calculator")

answer = input("Would you start? ")


def calculator():
    num1 = int(input("please, Enter your first number : "))
    num2 = int(input("second number : "))
    sign = input("enter your sign : ")

    # add function
    def add(A, B):
        result = int(A) + int(B)
        print(result)

    # mines function
    def mines(A, B):
        result = int(A) - int(B)
        print(result)

    # * function
    def darb(A, B):
        result = int(A) * int(B)
        print(result)

    # / function
    def ism(A, B):
        result = int(A) / int(B)
        print(result)

    if sign == '+':
        add(num1, num2)
    elif sign == '*':
        darb(num1, num2)
    elif sign == '-':
        mines(num1, num2)
    elif sign == '/':
        ism(num1, num2)
    elif not sign == '+' and not sign == '-' and not sign == '*' and not sign == '/':
        print("sorry, this equation doesn't available yet ")


while answer[0] == 'y' or answer[0] == 'Y':
    calculator()
    answer = input("Would you start again? ")
else:
    print("End")
    quit()
