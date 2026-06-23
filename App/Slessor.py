def sudoku_quadrant_checker(sudoku_board):
    print(f'sudoku_board: {sudoku_board}')
    response = ""

    for row in sudoku_board:
        print(f'row: {row}')
        row_list = row.split('(')[1].split(')')[0].split(',')
        print(f'row_list: {row_list}')
        error_locations = []

        for i in range(1,10):
            i_count = row_list.count(str(i))
            print(f'i: {i} i_count: {i_count}')

            if i_count > 1:
                row_index = sudoku_board.index(row)
                print(f'row_index: {row_index}')

                prev_column_index = 0
                for j in range (i_count):
                    column_index = row_list.index(str(i), prev_column_index)
                    print(f'column_index: {column_index}')
                    prev_column_index = column_index + 1
                    error_locations.append([row_index + 1, column_index + 1])

                print(f'error_locations: {error_locations}')

    return response