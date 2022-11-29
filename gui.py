import Functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("Todos.txt"):
    with open("Todos.txt","w") as file:
        pass

clock = sg.Text("",key="clock")

label = sg.Text("Type TODO")
input_txt = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button(size=1,image_source="add.png",mouseover_colors="LightBlue2",tooltip="Add Todo",key="ADD")
list_box = sg.Listbox(values=Functions.get_todos(),key="todos",enable_events=True,size=[45,10])
edit_button = sg.Button("EDIT")
complete_Button = sg.Button("complete")
Exit_Button = sg.Button("Exit")

window = sg.Window("My ToDo App",layout=[[clock],[label],[input_txt,add_button],[list_box,edit_button,complete_Button],[Exit_Button]], font=("Helvetice",10))

while True:
    event,value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(value)
    match event:
        case "ADD":
            Todos = Functions.get_todos()
            new_todo = value['todo']+"\n"
            Todos.append(new_todo)
            Functions.write_todos(Todos)
            window['todos'].update(values=Todos)
        case "EDIT":
            try:
                ToDO_Edit = value['todos'][0]
                new_todo = value['todo'] + "\n"
                Todos = Functions.get_todos()
                index = Todos.index(ToDO_Edit)
                Todos[index] = new_todo
                Functions.write_todos(Todos)
                window['todos'].update(values=Todos)
            except IndexError:
                sg.popup("Please select an Item")

        case "complete":
            try:
                Todo_complete = value['todos'][0]
                Todos = Functions.get_todos()
                Todos.remove(Todo_complete)
                Functions.write_todos(Todos)
                window['todos'].update(values=Todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an Item")

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=value['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()



