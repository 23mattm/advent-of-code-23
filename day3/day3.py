
class PartNumber:
    # line and column of the start of the number
    line: int
    col: int
    number: int


def get_whole_number(line: str, digit_index: int) -> (int, str):
    next = 1
    whole_number = line[digit_index]

    start_idx = digit_index
    end_idx = digit_index + 1

    while digit_index - next >= 0 and \
            line[digit_index - next].isdigit():
        next += 1
        start_idx -= 1

    next = 1
    while digit_index + next < len(line) and \
            line[digit_index + next].isdigit():
        next += 1
        end_idx += 1

    return start_idx, line[start_idx:end_idx]


def part_one(file_name: str) -> int:
    file = open(file_name)
    file_lines = file.read().split('\n')
    file.close()

    part_num_dict = dict()

    # a list of symbol locations stored as tuples of (line, col)
    symbol_locations = list()

    # adds (line, col) pairs to symbol_locations
    for line_index in range(len(file_lines)):
        line = file_lines[line_index]
        for char_idx in range(len(line)):
            char = line[char_idx]
            if not (char.isalnum() or char == '.'):
                # char is a symbol
                symbol_locations.append((line_index, char_idx))

    for line_col in symbol_locations:

        for line_adj in range(-1, 2):
            for col_adj in range(-1, 2):
                if line_adj == 0 and col_adj == 0: continue

                checking_line_idx = line_col[0] + line_adj
                checking_char_idx = line_col[1] + col_adj

                checking_char = (
                    file_lines)[checking_line_idx][checking_char_idx]

                if checking_char.isdigit():
                    start_idx, whole_num = get_whole_number(
                        file_lines[checking_line_idx],  # the line
                        checking_char_idx
                    )
                    key = f'l{checking_line_idx}c{start_idx}'
                    part_num_dict[key] = int(whole_num)

    part_num_sum = 0
    for part_num in part_num_dict:
        part_num_sum += part_num_dict[part_num]

    print(part_num_dict)
    return part_num_sum


def part_two(filename: str) -> int:
    file = open(filename)
    file_lines = file.read().split('\n')
    file.close()

    ratio_sum = 0
    for line_idx in range(len(file_lines)):
        line = file_lines[line_idx]

        for char_idx in range(len(line)):
            char = line[char_idx]

            if char == '*':
                # a set of unique starting positions for adjacent numbers
                # stored as tuples (line, col, num)
                adjacent_numbers = set()

                for line_adj in range(-1, 2):
                    for col_adj in range(-1, 2):
                        if line_adj == 0 and col_adj == 0: continue
                        checking_line = line_idx + line_adj
                        checking_col = char_idx + col_adj

                        checking_char = file_lines[checking_line][checking_col]
                        if checking_char.isdigit():
                            start_idx, whole_num = get_whole_number(
                                file_lines[checking_line],
                                checking_col
                            )
                            adjacent_numbers.add(
                                (checking_line,
                                 start_idx,
                                 int(whole_num))
                            )

                if len(adjacent_numbers) == 2:
                    ratio_sum += adjacent_numbers.pop()[2] * \
                        adjacent_numbers.pop()[2]

    return ratio_sum


print(part_one('input.txt'))
print(part_two('input.txt'))
