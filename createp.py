import sys
import os

# print('Number of arguments: ', len(sys.argv), ' arguments')
# print ('Argument List: ', str(sys.argv))
path = "C:/Users/jp-ro/Desktop/Projects/"


def create():
    try:
        argument = str(sys.argv[1])
        if argument == '-h':
            print('createp <File Name>')

        else:
            print(argument)

            try:
                os.mkdir(path+argument)
            except OSError:
                print(f"Creation of the directory {path+argument} failed ")
            else:
                print(f"Successfully created the directory {path+argument}")

    except IndexError:
        print("Please enter an argument, '-h' for help")
        sys.exit()


if __name__ == "__main__":
    create()
