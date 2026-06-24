def sudoku_quadrant_checker(sudoku_board):
    tag = 'sudoku_quadrant_checker | '
    print(tag + f'sudoku_board: {sudoku_board}')
    response = "legal"
    error_coordinates = []
    error_quadrants = []
    sudoku_board_matrix = sudoku_convert_board_to_matrix(sudoku_board)

    error_coordinates += sudoku_row_checker(sudoku_board_matrix)
    print(tag + f'error_coordinates: {error_coordinates}')
    error_coordinates += sudoku_column_checker(sudoku_board_matrix)
    print(tag + f'error_coordinates: {error_coordinates}')

    for coordinate in error_coordinates:
        print(tag + f'coordinate: {coordinate}')
        error_quadrants.append(sudoku_quadrant_from_coordinate(coordinate))
    print(tag + f'error_quadrants: {error_quadrants}')

    error_quadrants_string = ''
    for error_quadrant in sorted(error_quadrants):
        if not str(error_quadrant) in error_quadrants_string:
            if len(error_quadrants_string) > 0:
                error_quadrants_string += ','
            error_quadrants_string += str(error_quadrant)

    if len(error_quadrants_string) > 0:
        response = error_quadrants_string

    print(tag + f'response: {response}')

    return response

def sudoku_row_checker(sudoku_board_matrix):
    tag = 'sudoku_row_checker | '
    error_coordinates = []

    for row in sudoku_board_matrix:
        # print(tag + f'row: {row}')

        for i in range(1,10):
            i_count = row.count(str(i))
            # print(tag + f'i: {i} i_count: {i_count}')

            if i_count > 1:
                row_index = sudoku_board_matrix.index(row)
                # print(tag + f'row_index: {row_index}')

                prev_column_index = 0
                for j in range (i_count):
                    column_index = row.index(str(i), prev_column_index)
                    # print(tag + f'column_index: {column_index}')
                    prev_column_index = column_index + 1
                    error_coordinates.append([row_index + 1, column_index + 1])

    # print(tag + f'error_coordinates: {error_coordinates}')
    return error_coordinates

def sudoku_convert_board_to_matrix(sudoku_board):
    tag = 'sudoku_convert_board_to_matrix | '
    # print(tag + f'sudoku_board: {sudoku_board}')
    sudoku_board_matrix = []

    for row in sudoku_board:
        # print(tag + f'row: {row}')
        row_list = row.strip('()').split(',')
        # print(tag + f'row_list: {row_list}')
        sudoku_board_matrix.append(row_list)

    # print(tag + f'sudoku_board_matrix: {sudoku_board_matrix}')
    return sudoku_board_matrix

def sudoku_quadrant_from_coordinate(coordinate):
    tag = 'sudoku_quadrant_from_coordinate | '
    row = coordinate[0]
    column = coordinate[1]
    # print(tag + f'coordinate: {coordinate} row: {row} column: {column}')

    if row/3 <= 1:
        # print(tag + f'row/3 ({row/3}) <= 1')
        if column/3 <= 1:
            # print(tag + f'column/3 ({column/3}) <= 1')
            return 1
        elif column/3 <= 2:
            # print(tag + f'1 < column/3 ({column/3}) <= 2')
            return 2
        else:
            # print(tag + f'2 < column/3 ({column/3})')
            return 3
    elif row/3 <= 2:
        # print(tag + f'1 < row/3 ({row/3}) <= 2')
        if column/3 <= 1:
            # print(tag + f'column/3 ({column/3}) <= 1')
            return 4
        elif column/3 <= 2:
            # print(tag + f'1 < column/3 ({column/3}) <= 2')
            return 5
        else:
            # print(tag + f'2 < column/3 ({column/3})')
            return 6
    else:
        # print(tag + f'2 < row/3 ({row/3})')
        if column/3 <= 1:
            # print(tag + f'column/3 ({column/3}) <= 1')
            return 7
        elif column/3 <= 2:
            # print(tag + f'1 < column/3 ({column/3}) <= 2')
            return 8
        else:
            # print(tag + f'2 < column/3 ({column/3})')
            return 9

def sudoku_column_checker(sudoku_board_matrix):
    tag = 'sudoku_column_checker | '
    # print(tag + f'sudoku_board_matrix: {sudoku_board_matrix}')
    flipped_sudoku_board = []

    for column_index in range(len(sudoku_board_matrix[0])):
        flipped_row = []
        for row in sudoku_board_matrix:
            flipped_row.append(row[column_index])
        flipped_sudoku_board.append(flipped_row)

    flipped_error_coordinates = sudoku_row_checker(flipped_sudoku_board)
    # print(tag + f'flipped_error_coordinates: {flipped_error_coordinates}')

    error_coordinates = []
    for flipped_error_coordinate in flipped_error_coordinates:
        error_coordinates.append([flipped_error_coordinate[1], flipped_error_coordinate[0]])
    return error_coordinates

def step_walk_in_out(number_of_steps):
    return number_of_steps

def wildcard_characters(input_string):
    response = False
    return response

def tetris_move(input_array):
    return 1

def switch_sort(input_array):
    return 1