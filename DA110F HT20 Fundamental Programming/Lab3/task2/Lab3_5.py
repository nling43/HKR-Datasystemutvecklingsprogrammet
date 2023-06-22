import sys
import pickle

"""
~~The one with the order numbers~~
"""


def read_orders(filename):
    pass


def read_words(filename):
    pass


def find_all_possible_combinations(order_number):
    pass


def add_digit(digit, combinations):

    e_161 = {'2': ("a", "b", "c"),
             '3': ("d", "e", "f"),
             '4': ("g", "h", "i"),
             '5': ("j", "k", "l"),
             '6': ("m", "n", "o"),
             '7': ("p", "q", "r", "s"),
             '8': ("t", "u", "v"),
             '9': ("w", "x", "y", "z")
             }
    
    if len(combinations) == 0 :
        combinations.append(e_161.get('digit'))
    else:
        pass

    return combinations


def filter_valid_words(possible_combinations, valid_words):
    pass


def display_possible_words(order_number, words):
    pass


def main():
    list1 = []
    list1 = add_digit("2", list1)
    list1 = add_digit("3", list1)



if __name__ == "__main__":
    main()
