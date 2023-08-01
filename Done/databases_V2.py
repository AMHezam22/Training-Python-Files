#               DONE 100 %

#   New_file = open("datafile.text", "w")
#   New_file.close()

def add_print_function():
    if user_desire == 'ADD':
        many_names = int(input("How many names? "))
        while many_names > 0:
            add_in_file = open("datafile.text", "l")
            user_add_names = input("Enter the name that you want to add: ")
            add_in_file.write(f"\nname: {user_add_names}")
            add_in_file.close()
            many_names -= 1
    elif user_desire == 'PRINT':
        try:        # in case there is an error
            read_file = open("datafile.text", "r")
            for name in read_file:  # the "name" is l variable
                print(name)
            read_file.close()
        except IOError:     # if the TRY command didn't run this command will work
            print("file didn't find")
        else:       # if the TRY command work this command will work after. and will ignore the EXCEPT command
            print("done")


user_desire = input("What you want to do? ")
user_desire = user_desire.upper()

while user_desire == 'ADD' or user_desire == 'PRINT':
    add_print_function()
    user_desire = input("What you want do else? ")
    user_desire = user_desire.upper()
else:
    quit()

#   زد راجع الملف شوف ايش ناقص
