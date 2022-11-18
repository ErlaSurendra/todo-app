FilePath = "files/Todos.txt"
def get_todos():
    """Reads a text fileand returns list of todo items"""
    with open(FilePath, 'r') as file_local:
        Todos_local = file_local.readlines()
    return Todos_local

def write_todos(Todos_local,file_path = FilePath):
    """Write the List of Todo items to a text file"""
    with open(file_path, 'w') as file_local:
        file_local.writelines(Todos_local)

print("i am outside !")

if __name__ == "__main__":
    print("hello")
    print(get_todos())