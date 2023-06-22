import sys


def read_file(filename):

    return_list = []
    try:
        temp_list = []
        with open(filename) as f:   # open file
            temp_list = f.readlines()  # copy file into list
        # no longer need file
    except IOError:
        print(f"Error: The file '{filename }' could not be found.")
        sys.exit()

    for index in range(0, (len(temp_list)-1), 2):
        message = (temp_list[index].rstrip('\n'),
                   temp_list[index+1].rstrip('\n'))
        return_list.append(message)

    return return_list


def display_entry(name, message):
    print(f'[{name}] {"-->"} {message}')


if __name__ == "__main__":
    # do main stuff and what not

    list1 = read_file(sys.argv[1])
    name_search = input("Enter name to search for: ")
    for message in list1:
        if(message[0].upper() == name_search.upper()):
            display_entry(message[0], message[1])
