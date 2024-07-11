try:
    with open('exclusive_mode.txt', 'x') as file:
        file.write("Add this exclusive text.\n")
    except FileExistsError:
        print("This file already exists")
