# we gave parameter to the function where while function call
# we have to call it with the argument which we inserted as a parameter we are assigning a value to the parameter as an argument from the function call

FILEPATH="todos.txt" #we used FILEPATH in uppercase because anyone outside comes to this code they know that this file path is same for entire code and it is being reused for the code
def get_todos(filepath=FILEPATH):
    """ read a text file
    and return list of todo items in the file
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local

# this is used to go through your documentataion of that function print(help(get_todos))

# if we use 2 parameters and one parameter is default in those. make sure that default parameter goes first int he parametrization
# def write_todos(todos_arg,filepath="todos.txt")

def write_todos(todos_arg,filepath= FILEPATH):
    """
    write todo items list in files in a text file

    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
"""
if the import is executed this print is shown as 'functions'
but if we print in this file it shows this file name as 'main'
this allows us to use this code in if statement only in this file

"""
"""
    if we give this conditonal
    it just brings the output containing in the if conditon
    only if the file is processed in the same file 
    without the import statement containing file
    once we import a file in a different file this entire file is executed
    when the other file is executed
    so we can stop this unwanted lines of code which we don't want to get executed 
    by using if conditional like this 
"""
if __name__=="__main__":
    print("hello")
    print(get_todos())

def count(phrase):
    return phrase.count('.')

#modules are nothihng but python file which we have all the functions
#paremeters and arguments are similar words