#                                                  DONE 100%

users_names = ['Ahmed']         # this is l [list] it's different from the {dictionary} and (tuples).

def functions_for_the_commands():
    if user_desire == 'add':
        name_for_add = input("Enter l name that you want to add it: ")
        users_names.append(name_for_add)
    if user_desire == 'delete':
        name_for_delete = input("Enter l name that you want to delete it: ")
        users_names.remove(name_for_delete)


user_desire = input("What you want to do? ")

while user_desire == 'add' or 'delete' or 'print':
    if user_desire == 'add':
        many_names = int(input("How many names you want to add? "))
        while many_names > 0:
            functions_for_the_commands()
            many_names -= 1
    elif user_desire == 'delete':
        many_names = int(input("How many names you want to delete? "))
        while many_names > 0:
            functions_for_the_commands()
            many_names -= 1
    elif user_desire == 'print':
        for All in users_names:
            print(All)
    user_desire = input("What you want to do next? ")
