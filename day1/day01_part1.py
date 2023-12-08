

def sum(filename: str) -> int:
    sum = 0
    with open(filename) as file:

        for line in file:
            first_digit = None
            last_digit = None
            for char_idx in range(len(line)):
                char = line[char_idx]
                if char.isdigit():
                    last_digit = char
                    if first_digit is None:
                        first_digit = char
                else:
                    spelled_digit = find_spelled_digit(line[char_idx:])
                    if spelled_digit >= 0:
                        if first_digit is None:
                            first_digit = str(spelled_digit)
                        last_digit = str(spelled_digit)

            add = first_digit + last_digit
            print(add)
            sum += int(add)
            print(sum)

    print(sum)

def find_spelled_digit(string: str) -> int:
    num_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    for num in num_dict:
        if string.find(num) == 0:
            return num_dict[num]

    return -1

sum("input.txt")