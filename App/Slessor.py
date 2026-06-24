def sudoku_quadrant_checker(sudoku_board):
    tag = 'sudoku_quadrant_checker | '
    print(tag + f'sudoku_board: {sudoku_board}')
    response = "legal"
    error_coordinates = []
    error_quadrants = []

    error_coordinates += sudoku_row_checker(sudoku_board)
    print(tag + f'error_coordinates: {error_coordinates}')


    return response

def sudoku_row_checker(sudoku_board):
    tag = 'sudoku_row_checker | '
    error_coordinates = []

    for row in sudoku_board:
        print(tag + f'row: {row}')
        row_list = row.strip('()').split(',')
        print(tag + f'row_list: {row_list}')

        for i in range(1,10):
            i_count = row_list.count(str(i))
            print(tag + f'i: {i} i_count: {i_count}')

            if i_count > 1:
                row_index = sudoku_board.index(row)
                print(tag + f'row_index: {row_index}')

                prev_column_index = 0
                for j in range (i_count):
                    column_index = row_list.index(str(i), prev_column_index)
                    print(tag + f'column_index: {column_index}')
                    prev_column_index = column_index + 1
                    error_coordinates.append([row_index + 1, column_index + 1])

    print(tag + f'error_coordinates: {error_coordinates}')
    return error_coordinates


