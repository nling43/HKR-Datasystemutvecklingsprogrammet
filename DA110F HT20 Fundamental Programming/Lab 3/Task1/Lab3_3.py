import sys
import pickle

"""
~~The one where we help the police~~
"""


def cross_reference(files):
    # first we need to create the main set and a temp list
    set_to_return = set()
    temp_list = []
    # extracting content of files with file error handling
    try:
        for x in files:
            # open all the files in list and store content in temp list
            with open(x) as xfile:
                temp_list = temp_list + xfile.readlines()

    except FileNotFoundError:
        print("Error: There was a problem with at least one of the files.")

        sys.exit()

    while len(temp_list) >= len(files):
        # move phone number from list to varible
        phone_number = temp_list[0]
        # check if the phone numbers occurs in all files
        if temp_list.count(phone_number) == len(files):
            # asuming the number wont be in the same file twice
            # add the number to set and remove whitespaces and newline
            set_to_return.add(phone_number.rstrip())

        while temp_list.count(phone_number) > 0:
            # remove duplicate
            temp_list.remove(phone_number)

    return set_to_return


def display_menu():
    print('1. Add file\n2. Calculate ')


def display_suspects(names):
    print("The following persons was present on all crime scenes:\n" +
          "------------------------------------------------------")
    for name in names:
        print(name)


def map_numbers_to_names(numbers, filename):

    list_to_return = []

    try:
        with open(filename, 'rb') as pickle_f:
            pickle_dic = pickle.load(pickle_f)
    except FileNotFoundError:
        print("Error: There was a problem with at least one of the files.")
        sys.exit()

    for x in numbers:
        name = pickle_dic.get(x)

        if name is None:
            # none = add (unknown + phone)
            list_to_return.append(f'Unknown ({x})')

        else:
            # add only name
            list_to_return.append(name)
    return list_to_return


def main():
    files = []
    while True:
        display_menu()
        case = input('Enter choice: ')

        if case == '1':
            files.append(input("Input full path to file >>> "))
        elif case == '2':
            break

    numbers = cross_reference(files)
    try:
        names = map_numbers_to_names(numbers, sys.argv[1])
        display_suspects(names)

    except IndexError:
        print("no argument?")


if __name__ == "__main__":
    main()
