import streamlit as st
import Functions

def add_todo():
    todos = Functions.get_todos()
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    Functions.write_todos(todos)
st.title("My Todoo App")
st.subheader("This is my todo app.")
st.write("This improves your produtivity")

todos=Functions.get_todos()
for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="",placeholder="Add a new todo...",on_change=add_todo,key="new_todo")
