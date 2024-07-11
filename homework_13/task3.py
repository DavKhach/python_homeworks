try:
    with open('specific_position.txt', 'r+') as file:
        file.seek(10)
        file.write('Inserted text at position 10.\n')
except FileNotFoundError:
    with open('specific_position.txt', 'w') as file:
        file.write({"Initial text in file.\n")
    
    with open('specific_position.txt', 'r+') as file:
                   file.seek(10)
                   file.write("Inserted text at position 10.\n")
