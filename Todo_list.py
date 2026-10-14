with open("todo.txt", "a+") as file:
    file.seek(0)
    todo = file.read().splitlines()

menu = """
[1] Add a task
[2] Remove a task
[3] Display the task list
[4] Quit the app
"""
print(menu)
menu_response = int(input("Choose an option between 1 and 4: "))

if menu_response == 1:
    add = input("What would you like to add to the list? : ")
    todo.append(add)
    print(todo)

    with open("todo.txt", "a") as file:
        file.write(add + "\n")

elif menu_response == 2:
    delete = input("What would you like to remove? : ")

    if delete in todo:
        todo.remove(delete)
        print(todo)

        with open("todo.txt", "w") as file:
            for task in todo:
                file.write(task + "\n")
    else:
        print("You cannot remove an item that does not exist.")

elif menu_response == 3:
    print(todo)

elif menu_response == 4:
    print("Goodbye!")

else:
    print("Please choose an option between 1 and 4.")
