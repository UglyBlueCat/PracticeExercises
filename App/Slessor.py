def sudoku_quadrant_checker(sudoku_board):
    tag = 'sudoku_quadrant_checker | '
    print(tag + f'sudoku_board: {sudoku_board}')
    response = "legal"
    error_coordinates = []
    error_quadrants = []

    error_coordinates += sudoku_row_checker(sudoku_board)
    print(tag + f'error_coordinates: {error_coordinates}')

    for coordinate in error_coordinates:
        print(tag + f'coordinate: {coordinate}')
        error_quadrants.append(sudoku_quadrant_from_coordinate(coordinate))
    print(tag + f'error_quadrants: {error_quadrants}')

    if len(error_quadrants) > 0:
        response = str(error_quadrants)
    print(tag + f'response: {response}')

    return response

def sudoku_row_checker(sudoku_board):
    tag = 'sudoku_row_checker | '
    error_coordinates = []

    for row in sudoku_board:
        # print(tag + f'row: {row}')
        row_list = row.strip('()').split(',')
        # print(tag + f'row_list: {row_list}')

        for i in range(1,10):
            i_count = row_list.count(str(i))
            # print(tag + f'i: {i} i_count: {i_count}')

            if i_count > 1:
                row_index = sudoku_board.index(row)
                # print(tag + f'row_index: {row_index}')

                prev_column_index = 0
                for j in range (i_count):
                    column_index = row_list.index(str(i), prev_column_index)
                    # print(tag + f'column_index: {column_index}')
                    prev_column_index = column_index + 1
                    error_coordinates.append([row_index + 1, column_index + 1])

    # print(tag + f'error_coordinates: {error_coordinates}')
    return error_coordinates

def sudoku_quadrant_from_coordinate(coordinate):
    tag = 'sudoku_quadrant_from_coordinate | '
    row = coordinate[0]
    column = coordinate[1]
    print(tag + f'coordinate: {coordinate} row: {row} column: {column}')

    if row/3 <= 1:
        print(tag + f'row/3 ({row/3}) <= 1')
        if column/3 <= 1:
            print(tag + f'column/3 ({column/3}) <= 1')
            return 1
        elif column/3 <= 2:
            print(tag + f'1 < column/3 ({column/3}) <= 2')
            return 2
        else:
            print(tag + f'2 < column/3 ({column/3})')
            return 3
    elif row/3 <= 2:
        print(tag + f'1 < row/3 ({row/3}) <= 2')
        if column/3 <= 1:
            print(tag + f'column/3 ({column/3}) <= 1')
            return 4
        elif column/3 <= 2:
            print(tag + f'1 < column/3 ({column/3}) <= 2')
            return 5
        else:
            print(tag + f'2 < column/3 ({column/3})')
            return 6
    else:
        print(tag + f'2 < row/3 ({row/3})')
        if column/3 <= 1:
            print(tag + f'column/3 ({column/3}) <= 1')
            return 7
        elif column/3 <= 2:
            print(tag + f'1 < column/3 ({column/3}) <= 2')
            return 8
        else:
            print(tag + f'2 < column/3 ({column/3})')
            return 9

def step_walk_in_out(number_of_steps):
    return number_of_steps