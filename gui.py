import Functions
import PySimpleGUI as sg

label = sg.Text("Type TODO")
input_txt = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("ADD")

window = sg.Window("My ToDo App",layout=[[label],[input_txt,add_button]], font=("Helvetice",20))

while True:
    event,value = window.read()
    print(event)
    print(value)
    match event:
        case "ADD":
            Todos = Functions.get_todos()
            new_todo = value['todo']+"\n"
            Todos.append(new_todo)
            Functions.write_todos(Todos)
        case sg.WIN_CLOSED:
            break
window.close()



