FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """This function allows users to open file path and read the contents of it!"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """"This function allows users to edit the filepath by writing the text in the variables onto new lines!"""
    with open(filepath, 'w') as file_local:
        todos_local = file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("hello")
    print(get_todos())
