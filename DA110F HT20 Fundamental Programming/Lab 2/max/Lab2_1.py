import sys


def read_file(input_filename):
    file_list = []
    # opens the file input by the user
    try:
        with open(input_filename, 'r') as open_file:
            # reads the data from the file to a variable
            data = open_file.read()
            # splits and stores the text data for every newline ("Anna", "Hello".. and so on)
            data = (data.split('\n'))
            # len() length of the list, range() how many times the loop will run, x pluses 1 every loop
            # this runs the loop as long as the length of the data file
            for x in range(len(data)-1):
                # as long as x % 2 == 0 we store the contents, this means that only when the number is equal it is saved.
                # the code will only work as long as a message isn't taking up two lines in the text file.
                if (x % 2) == 0:
                    # puts the name(first line) on spot [0] and message(second line) on spot [1] in to a tuple
                    thisTuple = (data[x], data[x + 1])
                    # puts the tuple at the bottom of the list
                    file_list.append(thisTuple)
    except FileNotFoundError:
        print(f'Error: The file {input_filename} could not be found.')
        sys.exit(0)
    except IOError:
        print(f'Error: The file {input_filename} could not be found.')
        sys.exit(0)
    # returns the file_list to the read_file function so it can be used in the formatting function
    return file_list
# create formatmessage function, the file_list is added when function is called in the main function


def formatmessage(file_list, personname):
    # loops and checks every line from top to bottom if it matches the personname variable
    for start in file_list:
        if(start[0] == personname):
            # prints personname and the following line if a match is made on start[0]
            print(personname + " ---> " + start[1])


if __name__ == "__main__":
    # user enters text file location
    # call the read_file function with the filename as argument
    # give the returned file_list from read_file to a variable
    file_list = read_file(sys.argv[1])
    # user enters the name they want to search for
    personname = input('Enter a name to search for: ')
    # call the formatmessage function with the file_list as argument
    formatmessage(file_list, personname)
    # create read_file function, it holds the input_filename argument from before
    # in this function we open the text file and return the data needed to the file_list variable

