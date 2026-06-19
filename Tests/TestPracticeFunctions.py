# tests for practice functions from python-practice.com

import unittest
#import pytest
from App import PracticeFunctions

class MyTestCase(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(PracticeFunctions.count_vowels('example'), 3)
        self.assertEqual(PracticeFunctions.count_vowels('sky'), 0)
        self.assertEqual(PracticeFunctions.count_vowels('aeiou'), 5)
        self.assertEqual(PracticeFunctions.count_vowels('Ear Worm'), 3)

    def test_calc_discount(self):
        self.assertEqual(PracticeFunctions.calc_discount(50, 20), 40)
        self.assertEqual(PracticeFunctions.calc_discount(100, 0), 100)
        self.assertEqual(PracticeFunctions.calc_discount(100, 1), 99)
        self.assertEqual(PracticeFunctions.calc_discount(50, 100), 0)

    def test_double_characters(self):
        self.assertEqual(PracticeFunctions.double_characters('hello'), 'hheelllloo')
        self.assertEqual(PracticeFunctions.double_characters('world'), 'wwoorrlldd')
        self.assertEqual(PracticeFunctions.double_characters('123'), '112233')
        self.assertEqual(PracticeFunctions.double_characters(''), '')

    def test_mood_today(self):
        self.assertEqual(PracticeFunctions.mood_today("happy"), "Today, I am feeling happy")
        self.assertEqual(PracticeFunctions.mood_today("sad"), "Today, I am feeling sad")
        self.assertEqual(PracticeFunctions.mood_today("very happy"), "Today, I am feeling very happy")
        self.assertEqual(PracticeFunctions.mood_today(), "Today, I am feeling neutral")

    def test_reverse(self):
        self.assertEqual(PracticeFunctions.reverse("Hello World"), "DLROw OLLEh")
        self.assertEqual(PracticeFunctions.reverse("ReVeRsE"), "eSrEvEr")
        self.assertEqual(PracticeFunctions.reverse(""), "")
        self.assertEqual(PracticeFunctions.reverse("Radar"), "RADAr")

    def test_reverse_bool(self):
        self.assertEqual(PracticeFunctions.reverse_bool(False), True)
        self.assertEqual(PracticeFunctions.reverse_bool(True), False)
        self.assertEqual(PracticeFunctions.reverse_bool(0), "boolean expected")
        self.assertEqual(PracticeFunctions.reverse_bool(None), "boolean expected")

    def test_num_layers(self):
        self.assertEqual(PracticeFunctions.num_layers(0), "0.0005m")
        self.assertEqual(PracticeFunctions.num_layers(1), "0.001m")
        self.assertEqual(PracticeFunctions.num_layers(3), "0.004m")
        self.assertEqual(PracticeFunctions.num_layers(16), "32.768m")

    def test_unique_sort(self):
        self.assertEqual(PracticeFunctions.unique_sort([1, 5, 8, 2, 3, 4, 4, 4, 10]), [1, 2, 3, 4, 5, 8, 10])
        self.assertEqual(PracticeFunctions.unique_sort([1, 2, 5, 4, 7, 7, 7]), [1, 2, 4, 5, 7])
        self.assertEqual(PracticeFunctions.unique_sort([7, 6, 5, 4, 3, 2, 1, 0, 1]), [0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(PracticeFunctions.unique_sort([3, 6, 5, 4, 3, 27, 1, 100, 1]), [1, 3, 4, 5, 6, 27, 100])

    def test_index_of_caps(self):
        self.assertEqual(PracticeFunctions.index_of_caps("pYtHoN"), [1, 3, 5])
        self.assertEqual(PracticeFunctions.index_of_caps("eQuINoX"), [1, 3, 4, 6])
        self.assertEqual(PracticeFunctions.index_of_caps("determine"), [])
        self.assertEqual(PracticeFunctions.index_of_caps("STRIKE"), [0, 1, 2, 3, 4, 5])

    def test_relation_to_luke(self):
        self.assertEqual(PracticeFunctions.relation_to_luke("Darth Vader"), "Luke, I am your father.")
        self.assertEqual(PracticeFunctions.relation_to_luke("Leia"), "Luke, I am your sister.")
        self.assertEqual(PracticeFunctions.relation_to_luke("Han"), "Luke, I am your brother in law.")
        self.assertEqual(PracticeFunctions.relation_to_luke("R2D2"), "Luke, I am your droid.")

    def test_is_palindrome(self):
        self.assertEqual(PracticeFunctions.is_palindrome("racecar"), True)
        self.assertEqual(PracticeFunctions.is_palindrome("A man, a plan, a canal, Panama!"), True)
        self.assertEqual(PracticeFunctions.is_palindrome("hello"), False)
        self.assertEqual(PracticeFunctions.is_palindrome("1221"), True)

    def test_highest_frequency(self):
        result = PracticeFunctions.highest_frequency([1,6,4,3,1])
        self.assertEqual(result, [1])
        result = PracticeFunctions.highest_frequency([2,4,6,2,6])
        result.sort()
        self.assertEqual(result, [2,6])
        result = PracticeFunctions.highest_frequency([5,5,4,4,3,3,2,2,1,1])
        result.sort()
        self.assertEqual(result, [1,2,3,4,5])
        result = PracticeFunctions.highest_frequency([])
        self.assertEqual(result, [])

    def test_multiplication_table(self):
        table = PracticeFunctions.multiplication_table(5)
        self.assertEqual(table[4][3], 12)
        table = PracticeFunctions.multiplication_table(10)
        self.assertEqual(table[10][10], 100)
        table = PracticeFunctions.multiplication_table(1)
        self.assertEqual(table[1][1], 1)
        table = PracticeFunctions.multiplication_table(4)
        # verify the headers for the table exist
        self.assertEqual(table[0][1], 1)
        self.assertEqual(table[0][2], 2)
        self.assertEqual(table[0][3], 3)
        self.assertEqual(table[0][4], 4)

    def test_uncensor(self):
        self.assertEqual(PracticeFunctions.uncensor("l*k* th*s", "iei"), "like this")
        self.assertEqual(PracticeFunctions.uncensor("*****", "aeiou"), "aeiou")
        self.assertEqual(PracticeFunctions.uncensor("*PP*RC*S*", "UEAE"), "UPPERCASE")
        self.assertEqual(PracticeFunctions.uncensor("*'m C*ns*r*d", "Ieoe"), "I'm Censored")

    def test_fizz_buzz(self):
        self.assertEqual(PracticeFunctions.fizz_buzz(3), "Fizz")
        self.assertEqual(PracticeFunctions.fizz_buzz(4), "4")
        self.assertEqual(PracticeFunctions.fizz_buzz(5), "Buzz")
        self.assertEqual(PracticeFunctions.fizz_buzz(15), "FizzBuzz")

    def test_return_unique(self):
        self.assertEqual(PracticeFunctions.return_unique([1, 9, 8, 8, 7, 6, 1, 6]), [9, 7])
        self.assertEqual(PracticeFunctions.return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]), [2, 1])
        self.assertEqual(PracticeFunctions.return_unique([9, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]), [])
        self.assertEqual(PracticeFunctions.return_unique([4, 3, 9, 9, 1, 1, 6, 1, 6, 2, 4]), [3, 2])

    def test_merge_sort(self):
        self.assertEqual(PracticeFunctions.merge_sort([1, 2, 3], [5, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(PracticeFunctions.merge_sort([8, 6, 4, 2], [-2, -6,  0, -4 ]), [8, 6, 4, 2, 0, -2, -4, -6])
        self.assertEqual(PracticeFunctions.merge_sort([120, 180, 200], [190, 175, 130]), [120, 130, 175, 180, 190, 200])
        self.assertEqual(PracticeFunctions.merge_sort([25, 21, 17, 13], []), [25, 21, 17, 13])

    def test_count_uppercase(self):
        self.assertEqual(PracticeFunctions.count_uppercase(["SOLO", "hello", "Tea", "wHat"]), 6)
        self.assertEqual(PracticeFunctions.count_uppercase(["little", "lower", "down"]), 0)
        self.assertEqual(PracticeFunctions.count_uppercase(["PYTHON", "Educate", "Coding"]), 8)
        self.assertEqual(PracticeFunctions.count_uppercase(["Fix", "mY", "Code"]), 3)

    def test_format_date(self):
        self.assertEqual(PracticeFunctions.format_date("11/12/2019"), "20191211")
        self.assertEqual(PracticeFunctions.format_date("12/31/2019"), "20193112")
        self.assertEqual(PracticeFunctions.format_date("01/15/2019"), "20191501")
        self.assertEqual(PracticeFunctions.format_date("07/12/2023"), "20231207")

    def test_split(self):
        self.assertEqual(PracticeFunctions.split("()()()"), ["()", "()", "()"])
        self.assertEqual(PracticeFunctions.split(""), [])
        self.assertEqual(PracticeFunctions.split("()()(())"), ["()", "()", "(())"])
        self.assertEqual(PracticeFunctions.split("(())(()())"), ["(())", "(()())"])

    def test_stair(self):
        self.assertEqual(PracticeFunctions.stair(0), "___")
        self.assertEqual(PracticeFunctions.stair(1), "  _\n_|")
        self.assertEqual(PracticeFunctions.stair(2), "    _\n  _|\n_|")
        self.assertEqual(PracticeFunctions.stair(5), "          _\n        _|\n      _|\n    _|\n  _|\n_|")

    def test_can_see_stage(self):
        self.assertEqual(PracticeFunctions.can_see_stage(
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]), True)
        self.assertEqual(PracticeFunctions.can_see_stage(
            [[1, 2, 2],
             [1, 2, 3],
             [4, 4, 4]]), False)
        self.assertEqual(PracticeFunctions.can_see_stage(
            [[1, 2, 3, 2, 1, 1],
             [2, 4, 4, 3, 2, 2],
             [5, 5, 5, 10, 4, 4],
             [6, 6, 7, 6, 5, 5]]), False)
        self.assertEqual(PracticeFunctions.can_see_stage(
            [[1, 2, 3, 2, 1, 1],
             [2, 4, 4, 3, 2, 2],
             [5, 5, 5, 5, 4, 4],
             [6, 6, 7, 6, 5, 5]]), True)

    def test_advanced_sort(self):
        self.assertEqual(PracticeFunctions.advanced_sort([1,2,1,2]), [[1,1],[2,2]])
        self.assertEqual(PracticeFunctions.advanced_sort([2, 1, 2, 1]), [[2, 2], [1, 1]])
        self.assertEqual(PracticeFunctions.advanced_sort([80, 80, 4, 60, 60, 3]), [[80, 80], [4], [60, 60], [3]])
        self.assertEqual(PracticeFunctions.advanced_sort(['c','c','b','c','b',1,1]), [['c','c','c'],['b','b'],[1,1]])

    def test_num_split(self):
        self.assertEqual(PracticeFunctions.num_split(39), [30, 9])
        self.assertEqual(PracticeFunctions.num_split(-434), [-400, -30, -4])
        self.assertEqual(PracticeFunctions.num_split(100), [100, 0, 0])
        self.assertEqual(PracticeFunctions.num_split(3929), [3000, 900, 20, 9])

    def test_islands_perimeter(self):
        area = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        self.assertEqual(PracticeFunctions.islands_perimeter(area), 16)
        area = [[1, 0]]
        self.assertEqual(PracticeFunctions.islands_perimeter(area), 4)
        area = [
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
            [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        ]
        self.assertEqual(PracticeFunctions.islands_perimeter(area), 140)
        area = [
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
        ]
        self.assertEqual(PracticeFunctions.islands_perimeter(area), 42)

    def test_flatten(self):
        self.assertEqual(PracticeFunctions.flatten([1, 5, [3, 5, [5, 2], 5]]), [1, 5, 3, 5, 5, 2, 5])
        self.assertEqual(PracticeFunctions.flatten([1, 5, 7, 3, 2]), [1, 5, 7, 3, 2])
        self.assertEqual(PracticeFunctions.flatten([[[[5, 7, 8]]]]), [5, 7, 8])
        self.assertEqual(PracticeFunctions.flatten([]), [])

    def test_vertical_text(self):
        self.assertEqual(PracticeFunctions.vertical_text("Holy bananas"), [
            ['H', 'b'],
            ['o', 'a'],
            ['l', 'n'],
            ['y', 'a'],
            [' ', 'n'],
            [' ', 'a'],
            [' ', 's']])
        self.assertEqual(PracticeFunctions.vertical_text("Hello fellas"), [
            ['H', 'f'],
            ['e', 'e'],
            ['l', 'l'],
            ['l', 'l'],
            ['o', 'a'],
            [' ', 's']])
        self.assertEqual(PracticeFunctions.vertical_text("I hope you have a great day"), [
            ['I', 'h', 'y', 'h', 'a', 'g', 'd'],
            [' ', 'o', 'o', 'a', ' ', 'r', 'a'],
            [' ', 'p', 'u', 'v', ' ', 'e', 'y'],
            [' ', 'e', ' ', 'e', ' ', 'a', ' '],
            [' ', ' ', ' ', ' ', ' ', 't', ' ']])
        self.assertEqual(PracticeFunctions.vertical_text("Piri piri over there"), [
            ['P', 'p', 'o', 't'],
            ['i', 'i', 'v', 'h'],
            ['r', 'r', 'e', 'e'],
            ['i', 'i', 'r', 'r'],
            [' ', ' ', ' ', 'e']])

if __name__ == '__main__':
    unittest.main()
