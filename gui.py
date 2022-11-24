import Functions
import PySimpleGUI as sg

label = sg.Text("Type TODO")
input_txt = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("ADD")
list_box = sg.Listbox(values=Functions.get_todos(),key="todos",enable_events=True,size=[45,10])
edit_button = sg.Button("EDIT")

window = sg.Window("My ToDo App",layout=[[label],[input_txt,add_button],[list_box,edit_button]], font=("Helvetice",20))

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
            window['todos'].update(values=Todos)
        case "EDIT":
            ToDO_Edit = value['todos'][0]
            new_todo = value['todo']+"\n"
            Todos = Functions.get_todos()
            index = Todos.index(ToDO_Edit)
            Todos[index] = new_todo
            Functions.write_todos(Todos)
            window['todos'].update(values=Todos)
        case "todos":
            window['todo'].update(value=value['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()



