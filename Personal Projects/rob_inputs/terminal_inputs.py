def get_int(message, new_line=True):
    """# Forces Integer Input

    ---

    Forces an integer input. Input the question to ask the user, returns the inputted integer.


    You may also specify whether the input should be typed on a different line or not using new_line.
    Default is `True`."""

    if new_line:
        message += '\n'

    while True:
        inty = input(message)
        try:
            inty = int(inty)
            return inty
        except:
            print("\033[031mInvalid input, looking for an integer\033[00m")


def get_float(message, new_line=True):
    """# Forces Float Input

    ---
    
    Forces a float input. Input the question to ask the user, returns the inputted float.
    
    You may also specify whether the input should be typed on a different line or not using new_line.
    Default is `True`."""

    if new_line:
        message += '\n'

    while True:
        floaty = input(message)
        try:
            floaty = float(floaty)
            return floaty
        except:
            print('\033[31mInvalid input, looking for a float\033[00m')


def get_bool(message, new_line=True):
    """# Forces Boolean Input

    ---
    
    Forces a boolean input. Input the question to ask the user, returns the inputted boolean.

    Not case sensitive.
    
    Acceptable `True` answers are `y`, `yes`, `t`, `true`.
    
    Acceptable `False` answers are `n`, `no`, `f`, `false`.
    
    You may also specify whether the input should be typed on a different line or not using new_line.
    Default is `True`."""

    true = ['y', 'yes', 't', 'true']
    false = ['n', 'no', 'f', 'false']

    while True:
        booly = input(message).lower()
        if booly in true:
            return True
        elif booly in false:
            return False
        else:
            print("Invalid input, looking for a yes or no.")


def get_month():
    "Forces a month input. Returns month number."
    month_long = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")
    month_short = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
    
    while True:
        month = input("What month is it?\n").lower()

        try:
            month = int(month)
            if month >= 1 and month <= 12:
                return month
        except:
            if month in month_long:
                return month_long.index(month)+1
            elif month in month_short:
                return month_short.index(month)+1

        print("Invalid input, looking for a month name or number.")


def force_selection(choices):
    print('Please pick:')
    for x in range(len(choices)):
        print('{}: {}'.format(x+1, choices[x]))
    
    while True:
        choice = input('')

        try:
            if int(choice) >= 1 and int(choice) <= len(choices):
                return choices[int(choice)-1]
        except:
            if choice.title() in choices:
                return choice.title()
                
        if get_bool('Invalid Input, would you like the choices printed again?\n'):
            for x in range(len(choices)):
                print('{}: {}'.format(x+1, choices[x]))


def convert_to_dictionary(tup_list, index_one, index_two):
    "Takes a list of tuples, and creates a dictionary out of two specified tuples."
    dictionary = {}
    for x in tup_list:
        dictionary[x[index_one]] = x[index_two]

    return dictionary


def force_selection_dict(dictionary, text):
    keys = []
    x = 1
    print("Please pick:")
    for key, item in dictionary.items():
        print("{}:".format(x), text.format(key, item))
        keys.append(key)
        x += 1
    
    while True:
        choice = input('')

        try:
            if int(choice) >= 1 and int(choice) <= len(keys):
                return keys[int(choice)-1]
        except:
            if choice.title() in keys:
                return choice.title()

        print("Invalid Input, try again.")