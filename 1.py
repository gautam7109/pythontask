# task-1
data = [['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]


def align_right(arr):
    max_len = [0]*len(arr[0])
    for row in arr:
        for word in row:
            if len(word) > max_len[row.index(word)]:
                max_len[row.index(word)] = len(word)

    for row in arr:
        for word in row:
            if len(word) < max_len[row.index(word)]:
                arr[arr.index(row)][row.index(word)] = " " * \
                    (max_len[row.index(word)]-len(word))+word

    for row in arr:
        print_row = ""
        for word in row:
            print_row += " "+word
        print(print_row)


align_right(data)

# task-2

str_ = "XC"


def roman_to_decimal(roman_str):
    roman_numerals = {"I": 1, "V": 5, "X": 10,
                      "L": 50, "C": 100, "D": 500, "M": 1000}

    decimal = roman_numerals[roman_str[-1]]

    for i in range(len(roman_str)-2, -1, -1):
        if roman_numerals[roman_str[i]] < roman_numerals[roman_str[i+1]]:
            decimal -= roman_numerals[roman_str[i]]
        else:
            decimal += roman_numerals[roman_str[i]]

    return decimal


print(roman_to_decimal(str_))

# Task3


query = 'February'


def get_days(month_str):
    month = {'Janauary': 31,
             'February': 28,
             'March': 31,
             'April': 30,
             'May': 31,
             'June': 30,
             'July': 31,
             'August': 31,
             'September': 30,
             'October': 31,
             'November': 30,
             'December': 31		}

    if(month_str not in month):
        return 'Error'
    else:
        return(month[month_str])


print(get_days(query))


# Task4

food = ['apples', 'bananas', 'tofu', 'soya']


def to_str(arr):
    result = ''
    if(len(arr)):
        for word in arr:
            if arr.index(word) == len(arr)-2:
                result += word+" and "
            elif arr.index(word) == len(arr)-1:
                result += word
            else:
                result += word+", "
    return result


print(to_str(food))
