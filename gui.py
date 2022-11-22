import Functions
import PySimpleGUI as sg

label = sg.Text("Type TODO")
input_txt = sg.InputText(tooltip="Enter ToDo")
add_button = sg.Button("ADD")

window = sg.Window("My ToDo App",layout=[[label],[input_txt,add_button]])
window.read()
window.close()



