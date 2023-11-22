def writeFile(fileName, content):
    with open(fileName, 'a') as file:
        file.write(content + "\n")
