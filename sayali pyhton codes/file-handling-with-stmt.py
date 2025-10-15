with open("myfile.txt", "w+") as file:
    file.write("This is text from file1 \nHello world!")
    file.seek(0)
    content = file.read()
    print(content)
    file.close()