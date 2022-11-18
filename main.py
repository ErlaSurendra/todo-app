#from Functions import get_todos, write_todos
import Functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        ToDo = user_action[4:]+"\n"
        #ToDo = input("Enter a ToDo: ")+"\n"
        Todos = Functions.get_todos()
        Todos.append(ToDo)

        Functions.write_todos(Todos)

    elif user_action.startswith("show"):
        Todos = Functions.get_todos()
        for index,item in enumerate(Todos):
            item = item.upper()
            item = item.strip('\n')
            row = f"{index+1}){item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            Todos = Functions.get_todos()

            number = int(user_action[5:])
            number = number - 1
            New_ToDo = input("Please enter new ToDo: ")
            Todos[number] = New_ToDo + "\n"

            Functions.write_todos(Todos)

            print("Successfully edited New ToDo")
        except ValueError:
            print("your command is not valid")
            continue


    elif user_action.startswith("complete"):
        try:
            Todos = Functions.get_todos()
            number = int(user_action[9:])
            Todos.pop(number - 1)

            Functions.write_todos(Todos)

            print("Successfully removed the requested ToDo")
        except :
            print("There is no command with that num")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, You entered incorrect command:")
print("bye")