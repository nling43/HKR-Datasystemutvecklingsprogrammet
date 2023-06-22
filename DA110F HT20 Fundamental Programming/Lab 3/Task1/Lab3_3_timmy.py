import sys
import pickle


def main():
    try:
        bin_file = sys.argv[1]
        file_path = []
        choice = 0
        while choice != 2:
            display_menu()
            choice = int(input('Enter choice: '))
            if choice == 1:
                listing_file = input('Enter a filename (include full path): ')
                file_path.append(listing_file)
        set1 = cross_reference(file_path)
        names = map_numbers_to_names(set1, bin_file)
        display_suspects(names)
    except (FileNotFoundError):
        print('Error: There was a problem with at least one of the files.')
    except (EOFError):
        print("problems with Eof error")
    except(IndexError):
        print("problems with Sys.args")


def display_menu():
    print('1. Add file')
    print('2. Calculate')


def cross_reference(files):
    set_list = []
    for i in files:
        with open(i, 'r') as infile:
            name = infile.readline().rstrip('\n')
            lst = []
            while name != '':
                lst.append(name)
                name = infile.readline().rstrip('\n')
            set_list += [lst]
    common_num = set(set_list[0]).intersection(*set_list)
    return common_num


def map_numbers_to_names(numbers, filename):
    with open(filename, 'rb') as dictionary:
        read_name = pickle.load(dictionary)
    lst = []
    for number in numbers:
        check = read_name.get(number, (f'Unknown {number}'))
        lst.append(check)

    return lst


def display_suspects(names):
    print('The following persons was present on all crime scenes:')
    print('------------------------------------------------------')
    if names == []:
        print('No matches')
    else:
        for person in names:
            print(person)


if __name__ == '__main__':
    main()
