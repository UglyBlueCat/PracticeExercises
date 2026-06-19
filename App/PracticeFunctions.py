import re

# Create a function called `count_vowels` that returns the total amount of vowels in a string. (a, e, i, o, u)
def count_vowels(string):
    vowelCount = 0

    vowels = ['a','e','i','o','u']

    for char in string:
        print(char)
        if char.lower() in vowels:
            vowelCount += 1

    return vowelCount

# Write a function called `calc_discount` that accepts two parameters.
# The first should be the full price of an item as an integer.
# The second should be the discount percentage as an integer.
#
# The function should return the price of the item after the discount has been applied.
# For example, if the price is 50 and the discount is 20, the function should return 40.
def calc_discount(full_price, discount_percentage):
    discountedAmount = full_price*(discount_percentage/100)
    return full_price - discountedAmount

# Write a function called `double_characters` that accepts a string.
# The function should return a string, with each character in the original string doubled.
#
# If you send the function "now" as a parameter, it should return "nnooww"
# and if you send "123a!", it should return "112233aa!!"
def double_characters(string):
    doubledString = ""
    for char in string:
        doubledString += char + char

    return doubledString

# Write a function called `mood_today` that takes in a current mood and return a sentence in the following format:
# `Today, I am feeling {mood}.`
# However, if no argument is passed, return `Today, I am feeling neutral.`
def mood_today(mood = 'neutral'):
    return "Today, I am feeling " + mood

# The function `reverse` takes a string as input and returns that string in reverse order, with the opposite case.
#
# the following string method may help: `swapcase`
def reverse(txt):
    reversed_text = ''

    for char in txt:
        reversed_text = char + reversed_text

    return reversed_text.swapcase()

# Write a function called `reverse_bool` that reverses a boolean value
# and returns the string "boolean expected" if another variable type is given.
#
# The `type` or `isinstance` methods may help.
def reverse_bool(arg):
    if isinstance(arg, bool):
        return not arg
    else:
        return "boolean expected"

# Write a function called `num_layers` that returns the thickness (in meters)
# formatted as a string of a piece of paper after folding it n number of times.
# The paper starts off with a thickness of 0.0005m.
def num_layers(n):
    int_n = int(n)
    print(f'int_n: {int_n}')
    layer_count = pow(2, int(n))
    print(f'layer_count: {layer_count}')
    answer = layer_count * 0.0005
    print(f'answer: {answer}')
    formatted_answer = f'{answer:.4f}'
    print(f'formatted_answer: '+formatted_answer)
    stripped_answer = formatted_answer.rstrip('0')
    return stripped_answer+'m'

# Given a list of numbers, write a function that returns a list that has all duplicate elements removed
# and is sorted from least to greatest value.
def unique_sort(lst):
    print(f'lst: {lst}')
    stripped_list = list(dict.fromkeys(lst))
    print(f'stripped_list: {stripped_list}')
    print(f'stripped_list type: {type(stripped_list)}')
    stripped_list.sort()
    return stripped_list

# Write a function called index_of_caps that takes a single string as argument
# and returns an ordered list containing the indices of all capital letters in the string.
def index_of_caps(string):
    index_list = []

    for index, char in enumerate(string):
        print(f"Index {index}: {char}")
        if char.isupper():
            index_list.append(index)

    return index_list

# Luke Skywalker has family and friends.
# Help him remind them who is who.
# Given a string with a name, return the relation of that person to Luke.
#
# format the returned string as `Luke, I am your {relation}.`
def relation_to_luke(name):
    relation_table = {
        'Darth Vader': 'father',
        'Leia': 'sister',
        'Han': 'brother in law',
        'R2D2': 'droid'
    }

    return f"Luke, I am your {relation_table[name]}."

# Write a function called `is_palindrome` that takes in a string as input
# and returns True if the string is a palindrome and False otherwise.
#
# A palindrome is a word, phrase, number, or other sequence of characters
# that reads the same forward and backward, ignoring spaces, punctuation, and letter casing.
#
# Examples: `racecar`, b`ob, `A man, a plan, a canal, Panama!`, `12321`
def is_palindrome(string):
    stripped_string = re.sub(r'[^A-Za-z0-9]', '', string).lower()
    return stripped_string == stripped_string[::-1]

# Write a function called highest_frequency that takes a list of integers as input
# and returns a list of integers that have the highest frequency.
# If multiple integers have the same highest frequency, all of them should be included in the list.
#
# For example, given the list `[1, 3, 2, 2, 1, 1, 4, 2, 4, 3]`, the function should return `[1, 2]`,
# as both 1 and 2 appear 3 times in the list, which is the highest frequency among all integers.
def highest_frequency(lst):
    countDict = {}

    for i in lst:
        count = 0
        if i in countDict.keys():
            count = countDict[i]
        print(f'i: {i} count: {count}')
        countDict[i] = count + 1

    print(f'countDict: {countDict}')

    if countDict == {}:
        return []

    highestCountKey = max(countDict, key=countDict.get)
    print(f'highestCountKey: {highestCountKey}')
    highestCountValue = countDict[highestCountKey]
    print(f'highestCountValue: {highestCountValue}')

    highestCountList = []

    for k,v in countDict.items():
        print(f'k: {k} v: {v}')
        if v == highestCountValue:
            print(f'v: {v} == highestCountValue: {highestCountValue}')
            highestCountList.append(k)

    return highestCountList

# Write a function called "multiplication_table" that accepts a size parameter. Return a nested array to represent the table.
#
# Example: multiplication_table(5)
#
# [[0, 1, 2,  3,  4,  5],
#  [1, 1, 2,  3,  4,  5],
#  [2, 2, 4,  6,  8,  10],
#  [3, 3, 6,  9,  12, 15],
#  [4, 4, 8,  12, 16, 20],
#  [5, 5, 10, 15, 20, 25]]
def multiplication_table(size):
    print(f'size: {size}')
    table = []

    if not size:
        return table

    for i in range(size+1):
        subTable = []
        for j in range(size+1):
            print(f'i: {i} j: {j}')

            result = i*j
            if i == 0:
                result = j
            elif j == 0:
                result = i

            subTable.append(result)
            print(f'subTable: {subTable}')
        table.append(subTable)

        print(f'table: {table}')

    return table

# Someone has attempted to censor my strings by replacing every vowel with a "*".
# Write a function called uncensor which accepts a censored string and a string of the censored vowels,
# return the original uncensored string.
def uncensor(censored_string, vowels):
    if not censored_string:
        return ""
    if not vowels:
        return censored_string
    if len(vowels) < 1:
        return censored_string

    vowelPointer = 0
    uncensored_string = ""

    for character in censored_string:
        if character == '*':
            uncensored_string += vowels[vowelPointer]
            vowelPointer += 1
        else:
            uncensored_string += character

    return uncensored_string

# Create a function called fizz_buzz that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
#
#     If the number is a multiple of 3 the output should be "Fizz".
#     If the number given is a multiple of 5, the output should be "Buzz".
#     If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
#     If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the unit tests below.
#     The output should always be a string even if it is not a multiple of 3 or 5.
def fizz_buzz(num):
    response = ''

    if num % 3 == 0:
        response += 'Fizz'

    if num % 5 == 0:
        response += 'Buzz'

    if num % 3 > 0:
        if num % 5 > 0:
            response = str(num)

    return response

# Write a function called `return_unique` that returns the unique items in the input array.
def return_unique(lst):
    if not lst:
        return []

    countDict = {}

    for i in lst:
        count = 0
        if i in countDict.keys():
            count = countDict[i]
        print(f'i: {i} count: {count}')
        countDict[i] = count + 1

    print(f'countDict: {countDict}')

    unique_list = []

    for index in countDict.keys():
        if countDict[index] == 1:
            unique_list.append(index)

    return unique_list

# Given two lists, merge them to one list and sort the new list in the same order as the first list.
# Examples
# merge_sort([1, 2, 3], [5, 4, 6])
# ➞ [1, 2, 3, 4, 5, 6]
#
# merge_sort([8, 6, 4, 2], [-2, -6, 0, -4])
# ➞ [8, 6, 4, 2, 0, -2, -4, -6]
#
# merge_sort([120, 180, 200], [190, 175, 130])
# ➞ [120, 130, 175, 180, 190, 200]
# Notes
# - You'll always get two lists as arguments.
# - The first list is always sorted, either asc or desc.
# - Use the sorted function to sort a list
def merge_sort(lst1, lst2):
    print(f'lst1: {lst1}')
    print(f'lst2: {lst2}')

    if not lst1:
        if not lst2:
            return []
        return lst2

    if not lst2:
        return lst1

    response_list = lst1 + lst2

    if lst1[1] > lst1[0]:
        print('sort asc')
        response_list.sort()
    else:
        print('sort desc')
        response_list.sort(reverse = True)

    return response_list

# In the provided code is a function which is meant to return how many uppercase letters there are in a list of various words.
# Fix the list comprehension so that the code functions normally!
def count_uppercase(lst):
    if not lst:
        return 0

    total = 0

    for word in lst:
        print(f'word: {word}')

        if not word:
            continue

        for letter in word:
            print(f'letter: {letter}')

            if not letter:
                continue

            if letter.isupper():
                total += 1

    return total

# Create a function called `format_date` that converts a date formatted as `MM/DD/YYYY` to `YYYYDDMM`.
def format_date(date):
    if not date:
        return ""
    print(f'date: {date}')

    date_components = date.rsplit('/')
    print(f'date_components: {date_components}')

    month = date_components[0]
    day = date_components[1]
    year = date_components[2]

    return year + day + month

# Write a function called `split` that groups a string into parentheses clusters. Each cluster will be balanced. Example:
# `split("()()()") ➞ ["()", "()", "()"]`
def split(string):
    if not string:
        return []

    result = []

    bracket_count = 0
    current_string = ''

    for character in string:
        current_string += character

        if character == '(':
            bracket_count += 1
        elif character == ')':
            bracket_count -= 1

        if bracket_count == 0:
            result.append(current_string)
            current_string = ''

    return result

# Write a function called stair which takes an integer steps
# and returns a string representing an upward stair with steps representing the number of the steps in the stair.
#
# Each step will be represented by combinations of underscore(s), newline(s), and vertical line(s).
# So, if you print the result for a stair with three steps, it will look something like this:
#       _
#     _|
#   _|
# _|
# For zero, return ___ (three underscores).
def stair(steps):
    print(f'steps: {steps}')
    if not steps:
        return "___"

    staircase = steps*2*' '+'_\n'

    for step in range(steps, 0, -1):
        print(f'step: {step}')
        space_count = (step-1)*2
        print(f'space_count: {space_count}')
        staircase += space_count*' '+'_|'
        if step > 1:
            staircase += '\n'

    return staircase

# Create a function called can_see_stage that determines whether each seat can "see" the front-stage.
# A number can "see" the front-stage if it is strictly greater than the number before it.
# Everyone can see the front-stage in the example below:
#
# # FRONT STAGE
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 2, 2],
# [5, 5, 5, 5, 4, 4],
# [6, 6, 7, 6, 5, 5]]
#
# # Starting from the left,
# # 6 > 5 > 2 > 1 - so all numbers can see.
# # 6 > 5 > 4 > 2 - so all numbers can see, etc.
#
# Not everyone can see the front-stage in the example below:
#
# # FRONT STAGE
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 2, 2],
# [5, 5, 5, 10, 4, 4],
# [6, 6, 7, 6, 5, 5]]
#
# # The 10 is directly in front of the 6.
#
# The function should return True if every number can see the front-stage, and False if even a single number cannot.
def can_see_stage(seats):
    print(f'seats: {seats}')
    if not seats:
        return True

    rows = len(seats)
    print(f'rows: {rows}')

    if rows <= 1:
        return True

    columns = len(seats[0])
    print(f'columns: {columns}')

    for row in range(1, rows):
        for column in range(columns):
            if seats[row][column] <= seats[row-1][column]:
                return False

    return True

# Create a function called advanced_sort that takes a list of numbers or strings
# and returns a list with the items from the original list stored into sublists.
# Items of the same value should be in the same sublist.
# Examples
# advanced_sort([2, 1, 2, 1])
# ➞ [[2, 2], [1, 1]]
#
# advanced_sort([5, 4, 5, 5, 4, 3])
# ➞ [[5, 5, 5], [4, 4], [3]]
#
# advanced_sort(["b", "a", "b", "a", "c"])
# ➞ [["b", "b"], ["a", "a"], ["c"]]
#
# The sublists should be returned in the order of each element's first appearance in the given list.
def advanced_sort(lst):
    if not lst:
        return []

    sub_lists = []

    for element in lst:
        if len(sub_lists) > 0:
            element_new = True
            for sub_list in sub_lists:
                if sub_list[0] == element:
                    sub_list.append(element)
                    element_new = False
                    continue
            if element_new:
                new_sub_list = [element]
                sub_lists.append(new_sub_list)
                element_new = True
        else:
            new_sub_list = [element]
            sub_lists.append(new_sub_list)

    return sub_lists

# Create a function that takes a number and returns each place value in the number.
# Examples
# num_split(39)
# ➞ [30, 9]
#
# num_split(-434)
# ➞ [-400, -30, -4]
#
# num_split(100)
# ➞ [100, 0, 0]
def num_split(num):
    print(f'num: {num}')
    modifier = 1

    if num < 0:
        num = abs(num)
        modifier = -1

    print(f'num: {num} modifier: {modifier}')

    results = []

    while num != 0:
        print(f'num: {num} modifier: {modifier}')
        digit = num % 10
        print(f'digit: {digit}')
        results.insert(0, digit*modifier)
        print(f'results: {results}')
        num //= 10
        modifier *= 10

    return results

# The function is given a map with 1 representing land, 0 representing water.
# A land cell can have four neighbours along its edges.
# Compute the total perimeter of shore-lines that are defined by land cells touching water or the outer edges of the map.
# Each cell edge has a length equal to 1. An isolated cell without neighbours has a total perimeter length of 4.
def islands_perimeter(grid):
    print(f'grid: {grid}')
    if not grid:
        return 0

    perimeter = 0

    num_rows = len(grid)
    if not num_rows:
        return 0

    for row_index in range(num_rows):
        row = grid[row_index]
        print(f'row {row_index}: {row}')

        num_cells = len(row)
        if not num_cells:
            continue

        for cell_index in range(num_cells):
            if grid[row_index][cell_index] == 0:
                continue

            if row_index == 0:
                perimeter += 1
            elif grid[row_index-1][cell_index] == 0:
                perimeter += 1

            if cell_index == 0:
                perimeter += 1
            elif grid[row_index][cell_index-1] == 0:
                perimeter += 1

            if row_index == num_rows-1:
                perimeter += 1
            elif grid[row_index+1][cell_index] == 0:
                perimeter += 1

            if cell_index == num_cells-1:
                perimeter += 1
            elif grid[row_index][cell_index+1] == 0:
                perimeter += 1

    return perimeter

# Write a function called flatten that takes a list.
# This list can have all kinds of primitives, even other lists.
# The function should return a single, flat, one-dimensional, list with all elements.
def flatten(lst):
    if not lst:
        return []

    flattened_list = []
    contains_list = False

    for element in lst:
        if isinstance(element, list):
            for sub_element in element:
                flattened_list.append(sub_element)
                if isinstance(sub_element, list):
                    contains_list = True
        else:
            flattened_list.append(element)

    if contains_list:
        return flatten(flattened_list)

    return flattened_list

# Write a function called vertical_text that converts a string into a matrix of characters that can be read vertically.
# Add spaces when characters are missing.
# Example
# vertical_text("Holy bananas") ➞
# [
#   ["H", "b"],
#   ["o", "a"],
#   ["l", "n"],
#   ["y", "a"],
#   [" ", "n"],
#   [" ", "a"],
#   [" ", "s"]
# ]
def vertical_text(text):
    print(f'text: {text}')
    if not text:
        return []

    response_matrix = []

    words = text.split(' ')
    print(f'words: {words}')

    max_length = 0

    for word in words:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length

    print(f'max_length: {max_length}')

    for i in range(max_length):
        print(f'i: {i}')
        sub_list = []

        for word in words:
            word_length = len(word)

            if i < word_length:
                sub_list.append(word[i])
            else:
                sub_list.append(' ')

        print(f'sub_list: {sub_list}')
        response_matrix.append(sub_list)

    return response_matrix
