import re
import time

set_a = [1, 3, 5, 6, 8]
set_b = [2, 3, 4, 7, 9]


def main():
    display_instructions()
    user_input = get_user_input()
    process_user_input(user_input)


def display_instructions():
    intro = "\nWelcome! \nYou have two sets. \nA = %s" % set_a + " \nB = %s" % set_b
    instruct = "\nPlease enter one of the following operations to perform on the sets"
    union = "Union"
    intersection = "Intersection"
    difference = "Difference Or (A - B)"

    print(intro)
    print(instruct)
    print(union)
    print(intersection)
    print(difference)


def display_keyboard_interrupt_message():
    message = "\nI suppose we'll just have to shut it down then. \nOne moment please."

    print(message)


def get_user_input():
    prompt = "\nPlease enter the opperation you would like to perform: "

    try:
        user_input = raw_input(prompt)
        return user_input
    except KeyboardInterrupt:
        display_keyboard_interrupt_message()
        time.sleep(3)
        exit(1)


def process_user_input(input_string):
    union_pattern = re.compile("[uU][nN][iI][oO][nN]")
    intersection_pattern = re.compile("[iI][nN][tT][eE][rR][sS][eE][cC][tT][iI][oO][nN]")
    difference_pattern = re.compile("[dD][iI][fF][fF][eE][rR][eE][nN][cC][eE]")
    alternate_difference_pattern = re.compile("[aA]-[bB]|[aA]\s*-\s*[bB]")
    quit_pattern = re.compile("[qQ][uU][iI][tT]|[eE][xX][iI][tT]")

    loop_prompt = "Enter another operation or enter Quit to end the program: "

    if union_pattern.search(input_string):
        print(get_union(set_a, set_b))
        try:
            input_string = raw_input(loop_prompt)
        except KeyboardInterrupt:
            display_keyboard_interrupt_message()
            time.sleep(3)
            exit(1)

    elif intersection_pattern.search(input_string):
        print(get_intersection(set_a, set_b))
        try:
            input_string = raw_input(loop_prompt)
        except KeyboardInterrupt:
            display_keyboard_interrupt_message()
            time.sleep(3)
            exit(1)
    elif difference_pattern.search(input_string) or alternate_difference_pattern.search(input_string):
        print(get_difference(set_a, set_b))
        try:
            input_string = raw_input(loop_prompt)
        except KeyboardInterrupt:
            display_keyboard_interrupt_message()
            time.sleep(3)
            exit(1)
    elif quit_pattern.search(input_string):
        exit(0)
    else:
        fail_prompt = "Sorry %s" % input_string + " is not a recognized command. Please enter Union, Intersection, or Difference (or Quit to exit): "
        try:
            input_string = raw_input(fail_prompt)
        except KeyboardInterrupt:
            display_keyboard_interrupt_message()
            time.sleep(3)
            exit(1)

    process_user_input(input_string)


def get_union(set_a, set_b):

    set_c = []

    for element in set_a:
        set_c.append(element)

    for element in set_b:
        set_c.append(element)

    return set_c
# end function


def get_intersection(set_a, set_b):

    set_c = []

    for element in set_a:
        if set_b.__contains__(element):
            set_c.append(element)

    for element in set_b:
        if set_a.__contains__(element):
            if set_c.__contains__(element):
                break
            else:
                set_c.append(element)

    return set_c
# end function


def get_difference(set_a, set_b):

    set_c = []

    for element in set_a:
        if set_b.__contains__(element):
            continue
        else:
            set_c.append(element)

    return set_c
# end of function


main()
