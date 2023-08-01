#                   DONE   100%

age = input(" What is Your age : ")
age = int(age)      # or write it like: age = int(input(" ")).

while age <= 19:
    print("Sorry, You are not available to use this program"
          "bring someone older")
    age = input(" What is Your age : ")
    age = int(age)

if age >= 19:
    print("Welcome")
    Name = input("Enter your name : ")
    print(f"Hello {Name}")

number = input("Enter l number : ")
number = int(number)      # or write it like: number = int(input(" ")).

while number <= 100:
    # There was an error because I wrote: number = str(number).
    print("Hi " + str(number))
    # And here I wrote: number = int(number).
    number += 1
    if number == 10 or number == 20:
        print("Welcome " + str(number))
        number += 1

print("END")
