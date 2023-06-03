# Stream lit is becoming popular for the interface
# It's easy to deploy the apps so everyone can use them
# For starting the webpage we have to write code lines in terminal
# Streamlit run "filename" i.e. web.py is the command to start running streamlit on webpage on local host
# This takes us to localhost webpage showing the output directly
# After running in console if we enter new code in the .py file it just gets updated
# We just have to refresh the webpage
# So the code is updated on the UI
# For every reload the entire code is executed and output is shown on webpage
"""
Now, it's important to note that the web app, your web app, when it's public, it can have.Many users at the same time or at different times.
And you should know that each session, each user session is separate from other user sessions.
That means when you refresh your page somewhere in India and someone else refreshes the page somewhere
in New York at the same time or at different times, the script is executed separately for each of those
users.
So when we deploy the app somewhere on a web server, that means that CPU of the web server is going to handle those requests.
And it's important that if your app, if your web app has lots of visitors, it's important to have.
Sufficient hardware so RAM and CPU to handle many users.
Nowadays there are good options which are scalable, so you can start with less CPU and RAM.
And then as you see that your web app is becoming popular, you can increase, you can upgrade to more
RAM and CPU on your web server where your app is going to be hosted.
For now though, the app is hosted on your computer, so performance is not an issue for now.
"""
import streamlit as st
import functions



todos = functions.get_todos()


def add_todo():
    # This function is called when user makes any input to the input label because in st.text_input
    # We have given on change = add_todo which mean on any change in the input it calls this function
    # st.session_state this returns an array of data in dictionary
    # which is unstructured data we have to structure in data engineering
    # we will have the user entered data in UI in form of dictionary.
    # we extracted the data with "new_todo" is input keyname and value is the data user entered


    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("this is my todo app")
st.write("This app is to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()
st.text_input(label="Enter a todo", placeholder="Add  a new todo..",
              on_change=add_todo, key='new_todo')

#print("hello")

