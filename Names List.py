names = ["Evi", "Madeleine", "Dan", "Kelsey", "Cayden", "Hayley", "Darian"]
user_name = input("Enter a name")
if user_name in names:
    print("That name is already on the list!")
else:
    print("The name you chose is not on the list.")
if user_name != names:
    replace = input("Would you like to replace one of the names on the list with the name you picked? yes or no.")
    if replace.lower() == "yes":
        names = ["Evi", "Madeleine", user_name, "Kelsey", "Cayden", "Hayley", "Darian"]
        print("We have replaced Dan with the name you have chosen. You are now on the list.")
        print(names)
    elif replace.lower() == "no":
        print("You have chosen to not replace a name on the list.\n")
        add = input("Would you like to add the name you picked to the list? yes or no.")
        if add.lower() == "yes":
            names = ["Evi", "Madeleine", "Dan", "Kelsey", "Cayden", "Hayley", "Darian", user_name]
            print("The name you picked has been added to the list.")
            print(names)
        elif add.lower() == "no":
            print("You have chosen to not add the name to the list.")

