FILENAME = "todos.txt"

#print(__name__)


def convert_to_metres(feet, inches):
    num_metres = float(feet)*0.3048 + float(inches)*0.0254
    return num_metres


def my_file(filename,operation):
    with open(filename, operation) as file:
        file_content = file.readlines()
        return file_content


def get_todos():
    with open(FILENAME, "r") as file:
        file_content = file.readlines()
        return file_content


def write_todos(listitems):
    with open(FILENAME, "w") as file:
        file_content = file.writelines(listitems)
        return file_content

