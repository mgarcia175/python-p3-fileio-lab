def write_file(file_name, file_content):
    txt_file = str(file_name) + '.txt'

    with open(txt_file, mode='w') as file:
        file.write(file_content)







def append_file(file_name, append_content):
    txt_file = str(file_name) + '.txt'

    with open(txt_file, mode='a') as file:
        file.write(append_content)






def read_file(file_name):
    txt_file = str(file_name) + '.txt'

    with open(txt_file, mode='r') as file:
        content = file.read()
        return content
