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
for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add a new todo...",on_change=add_todo,key="new_todo")
