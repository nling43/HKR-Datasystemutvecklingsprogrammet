import sys


def read_file(filename):

    numbers = []
    temp_numbers = []
    try:

        with open(filename) as f:   # open file
            for line in f:
                temp_numbers = temp_numbers+line.split(" ")  # remove whitespace
            # no longer need file

    except IOError:
        print(f"Error: The file '{filename }' could not be found.")
        sys.exit()

    for x in temp_numbers:
        # filter away \n & add them to a list as integers
        numbers.append(int(x))

    return numbers


def filter_odd_or_even(numbers, odd):

    numbers_to_return = []
    if(odd):
        for x in numbers:  # for each number
            if (x % 2) != 0:  # number is odd
                numbers_to_return.append(x)  # append

    else:
        for x in numbers:  # for each number
            if (x % 2) == 0:  # number is even?
                numbers_to_return.append(x)  # append

    return numbers_to_return


def swap(numbers, index1, index2):  # hide messy code
    temp = numbers[index1]
    numbers[index1] = numbers[index2]
    numbers[index2] = temp


def reversed_bubble_sort(numbers):
    swapped = True
    while(swapped):  # did we swap
        swapped = False
        for j in range(len(numbers)-1):

            if(numbers[j] < numbers[j+1]):  # compare pair
                swap(numbers, j, j+1)  # swap if needed
                swapped = True  # we did swap


if __name__ == "__main__":
    # do main stuff and what not

    list1 = filter_odd_or_even(read_file(
        sys.argv[1]), True) + filter_odd_or_even(
        read_file(sys.argv[2]), False)
    reversed_bubble_sort(list1)
    print(list1)
