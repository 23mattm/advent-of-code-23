import math


def get_cards(file_name: str) -> list:
    with open(file_name) as file:
        lines = file.readlines()
    return [line.split(':')[1].strip() for line in lines]


def get_numbers(numbers: str) -> list:
    """
    return a list of numbers from a string of numbers separated by
    any amount of spcae characters
    """
    return [int(num.strip()) for num in numbers.split()]


def get_matches(card: str) -> int:
    """
    returns the amount of matches in a given card
    """
    temp = card.split('|')
    winning_nums = get_numbers(temp[0])
    my_nums = get_numbers(temp[1])
    matches = 0
    for number in my_nums:
        if number in winning_nums:
            matches += 1
    return matches


def get_total_points(file_name: str) -> int:
    cards = get_cards(file_name)

    point_sum = 0
    for card in cards:
        matches = get_matches(card)
        if matches > 0:
            point_sum += math.pow(2, matches-1)

    return point_sum


print(get_total_points('input.txt'))
