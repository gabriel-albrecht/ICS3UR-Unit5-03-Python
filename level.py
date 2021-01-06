#!/usr/bin/env python3

# Created by Gabriel A
# Created on Jan 2021
# This program converts levels into percentages


def grade_mark(level):
    # calculate area

    # process
    if level == "4+":
        percentage = float(97.5)
    elif level == "4":
        percentage = float(90.5)
    elif level == "4-":
        percentage = float(83)
    elif level == "3+":
        percentage = float(78)
    elif level == "3":
        percentage = float(74.5)
    elif level == "3-":
        percentage = float(71)
    elif level == "2+":
        percentage = float(68)
    elif level == "2":
        percentage = float(64.5)
    elif level == "2-":
        percentage = float(61)
    elif level == "1+":
        percentage = float(58)
    elif level == "1":
        percentage = float(54.5)
    elif level == "1-":
        percentage = float(51)
    elif level == "R":
        percentage = float(24.5)
    elif level == "r":
        percentage = float(24.5)
    else:
        percentage = float(-1)

    # output
    return percentage


def main():
    # this function gets length and width

    # input
    level_from_user = input("Enter a mark: ")

    # call functions
    mark = grade_mark(level_from_user)

    # output
    if mark == -1:
        print("\nThat is an invalid mark.")
    else:
        print("\n{} is on average a {}%.".format(level_from_user, mark))


if __name__ == "__main__":
    main()
