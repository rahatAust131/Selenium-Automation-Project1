
def write_in_file(file_name, data):
    with open(file_name, 'a') as file:
        file.write(data + "\n")
        file.close()
