import streamlit as st
from modules import all_functions
from modules.all_functions import *
st.title("My ToDo web app")

def add_todo():
    newitem=st.session_state["newtodo"] + "\n"
    listitems.append(newitem)
    write_todos(listitems)


def complete_todo(item):
    if st.session_state[item]:
        return
    listitems=get_todos()
    listitems.remove(item)
    write_todos(listitems)


listitems = get_todos()

for index,item in enumerate(listitems):
    checkbox = st.checkbox(item,key=item)
    if checkbox:
        listitems.pop(index)
        write_todos(listitems)
        st.experimental_rerun()

st.text_input(label="",placeholder="Add a ToDo", on_change=add_todo,key="newtodo") + "\n"

st.session_state
