#       DONE   100%
import datetime

your_age = input("Enter your birth year: ")
Now_time = datetime.datetime.now().year
age = Now_time - int(your_age)


if age >= 18:
    print(
        f"your age is {age} year, you are old and I'm sure you had so experience, don't keep to yourself and share it "
        f"with who need.")
    quit()
else:
    print(f"your age is {age} year, you still young don't afraid from life and just keep going.")