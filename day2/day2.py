"""Cubes"""

def part_one(file_path: str):
    BLUE_MAX = 14
    GREEN_MAX = 13
    RED_MAX = 12

    with open(file_path) as file:
        id_sum = 0
        for line in file:
            first_partition = line.split(':')
            # below gets the game ID in the format "Game XXX"
            game_id = int(first_partition[0].split(' ')[1])
            game_subsets = first_partition[1].split(';')
            game_valid = True
            for game in game_subsets:
                colors = game.split(',')
                print('game:', game, 'colors:', colors)
                for color in colors:
                    color = color.strip()
                    color = color.split(' ')
                    if color[1] == 'green' and int(color[0]) > GREEN_MAX:
                        game_valid = False
                    if color[1] == 'blue' and int(color[0]) > BLUE_MAX:
                        game_valid = False
                    if color[1] == 'red' and int(color[0]) > RED_MAX:
                        game_valid = False
            if game_valid:
                id_sum += game_id

        return id_sum


def part_two(file_name: str) -> int:

    with open(file_name) as file:
        power_sum = 0
        for line in file:
            game = line.split(':')[1].strip()

            redmin = 0
            bluemin = 0
            greenmin = 0

            game_subsets = game.split(';')
            for subset in game_subsets:

                for color in subset.split(','):
                    color = color.strip()
                    num_color = color.split(' ')
                    if num_color[1] == 'green' and int(num_color[0]) > greenmin:
                        greenmin = int(num_color[0])
                    if num_color[1] == 'blue' and int(num_color[0]) > bluemin:
                        bluemin = int(num_color[0])
                    if num_color[1] == 'red' and int(num_color[0]) > redmin:
                        redmin = int(num_color[0])

            power = redmin * bluemin * greenmin
            power_sum += power
        return power_sum


print('part two:', part_two('input.txt'))