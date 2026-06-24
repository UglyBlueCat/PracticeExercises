import unittest

from App import Slessor

class MyTestCase(unittest.TestCase):
    #     Sudoku Quadrant Checker
    #
    # the strArr parameter being passed which will represent a 9x9 Sudoku board of integers ranging from 1 to 9.
    #
    # The rules of Sudoku are to place each of the 9 integers integer in every row and column
    # and not have any integers repeat in the respective row, column, or 3x3 sub-grid.
    #
    # The input strArr will represent a Sudoku board
    # and it will be structured in the following format: ["(N,N,N,N,N,x,x,x,x)","(...)","(...)",...)]
    #
    # where N stands for an integer between 1 and 9 and x will stand for an empty cell.
    #
    # Your program will determine if the board is legal; the board also does not necessarily have to be finished.
    #
    # If the board is legal, your program should return the string legal
    # but if it isn't legal, it should return the 3x3 quadrants (separated by commas) where the errors exist.
    #
    # The 3x3 quadrants are numbered from 1 to 9 starting from top-left going to bottom-right.
    def test_sudoku_quadrant_checker(self):
        self.assertEqual(Slessor.sudoku_quadrant_checker(
            [
                "(1,2,3,4,5,6,7,8,1)",
                "(x,x,x,x,x,x,x,x,x)",
                "(x,x,x,x,x,x,x,x,x)",
                "(1,x,x,x,x,x,x,x,x)",
                "(x,x,x,x,x,x,x,x,x)",
                "(x,x,x,x,x,x,x,x,x)",
                "(x,x,x,x,x,x,x,x,x)",
                "(x,x,x,x,x,x,x,x,x)",
                "(x,x,x,x,x,x,x,x,x)"
            ]
        ),
            "1,3,4")

        self.assertEqual(Slessor.sudoku_quadrant_checker(
            [
                "(1,2,3,4,5,6,7,8,9)",
                "(x,x,x,x,x,x,x,x,x)",
                "(6,x,5,x,3,x,x,4,x)",
                "(2,x,1,1,x,x,x,x,x)",
                "(x,x,x,x,x,x,x,x,x)",
                "(x,x,x,x,x,x,x,x,x)",
                "(x,x,x,x,x,x,x,x,x)",
                "(x,x,x,x,x,x,x,x,x)",
                "(x,x,x,x,x,x,x,x,9)"
            ]
        ), "3,4,5,9")

# Step Walking In: 3 Out: 3
#
# Have the function StepWalking(num) take the num parameter being passed which will be an integer between 1 and 15 that represents the number of stairs you will have to climb.
#
# You can climb the set of stairs by taking either 1 step or 2 steps, and you can combine these in any order.
#
# So for example, to climb 3 steps you can either do: (1 step, 1 step, 1 step) or (2, 1) or (1, 2).
#
# So for 3 steps we have 3 different ways to climb them, so your program should return 3.
#
# Your program should return the number of combinations of climbing num steps.
#
# Examples
#
# Input: 1
# Output: 1
#
# Input: 3
# Output: 3

    def test_step_walk_in_out(self):
        self.assertEqual(True, False)

# Wildcard Characters
#
# Have the function WildcardCharacters(str) read str which will contain two strings separated by a space.
#
# The first string will consist of the following sets of characters: +, *, and {N} which is optional.
#
# The plus (+) character represents a single alphabetic character, the asterisk (*) represents a sequence of the same character of length 3 unless it is followed by {N} which represents how many characters should appear in the sequence where N will be at least 1.
#
# Your goal is to determine if the second string exactly matches the pattern of the first string in the input.
#
# For example: if str is "++*{5} gheeeee" then the second string in this case does match the pattern, so your program should return the string true.
#
# If the second string does not match the pattern your program should return the string false.
#
# Hard challenges are worth 15 points and you are not timed for them.
#
# Examples
#
# Input: "+++++* abcdemmmmmm"
# Output: false
# Input: "**+*{2} mmmrrrkbb"
# Output: true

    def test_wildcard_characters(self):
        self.assertEqual(True, False)

# Wildcards
#
# Have the function Wildcards(str) read str which will contain two strings separated by a space.
#
# The first string will consist of the following sets of characters: +, *, $, and {N} which is optional.
#
# The plus (+) character represents a single alphabetic character, the ($) character represents a number between 1-9, and the asterisk (*) represents a sequence of the same character of length 3 unless it is followed by {N} which represents how many characters should appear in the sequence where N will be at least 1.
#
# Your goal is to determine if the second string exactly matches the pattern of the first string in the input.
#
# For example: if str is "++*{5} jtggggg" then the second string in this case does match the pattern, so your program should return the string true.
#
# If the second string does not match the pattern your program should return the string false.
#
# Examples:
#
# Input: "+++++* abcdehhhhhh"
# Output: false
# Input: "$**+*{2} 9mmmrrrkbb"
# Output: true

    def test_wildcards(self):
        self.assertEqual(True, False)

# Tetris Move
#
# Have the function TetrisMove(strArr) take strArr parameter being passed which will be an array containing one letter followed by 12 numbers representing a Tetris piece followed by the fill levels for the 12 columns of the board.
#
# Calculate the greatest number of horizontal lines that can be completed when the piece arrives at the bottom assuming it is dropped immediately after being rotated and moved horizontally from the top.
#
# Tricky combinations of vertical and horizontal movements are excluded.
#
# The piece types are represented by capital letters.
#
# For example,
#
# with an input of ["L","3","4","4","5","6","2","0","6","5","3","6","6"], the board will look something like this:
#
# Your result should be 3 because the L piece can be rotated and dropped in column 6-7 which will complete 3 full rows of blocks.
#
# Hard challenges are worth 15 points and you are not timed for them.
# Examples
# Input: ["I", "2", "4", "3", "4", "5", "2", "0", "2", "2", "3", "3", "3"]
# Output: 2
# Input: ["O", "4", "3", "2", "3", "5", "1", "0", "1", "2", "4", "3", "4"]
# Output: 0

    def test_tetris_move(self):
        self.assertEqual(True, False)

# Switch Sort
#
# Have the function SwitchSort(arr) take arr which will be an an array consisting of integers 1...size(arr) and determine what the fewest number of steps is in order to sort the array from least to greatest using the following technique: Each element E in the array can swap places with another element that is arr[E] spaces to the left or right of the chosen element.
#
# You can loop from one end of the array to the other.
#
# For example: if arr is the array [1, 3, 4, 2] then you can choose the second element which is the number 3, and if you count 3 places to the left you'll loop around the array and end up at the number 4.
#
# Then you swap these elements and arr is then [1, 4, 3, 2]. From here only one more step is required, you choose the last element which is the number 2, count 2 places to the left and you'll reach the number 4, then you swap these elements and you end up with a sorted array [1, 2, 3, 4].
#
# Your program should return an integer that specifies the least amount of steps needed in order to sort the array using the following switch sort technique.
#
# The array arr will at most contain five elements and will contain at least two elements.
# Examples
#
# Input: [3,1,2]
# Output: 2
# Input: [1,3,4,2]
# Output: 2

    def test_switch_sort(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
