from typing import Union
from dataclasses import dataclass

@dataclass
class Seed:
    source: int
    seed_number: int
    range: int
    # soil: Union[int, None]
    # fertilizer: Union[int, None]
    # water: Union[int, None]
    # light: Union[int, None]
    # temp: Union[int, None]
    # humidity: Union[int, None]
    # location: Union[int, None]
    # destination: Union[int, None]


def make_seed(seed_num: int) -> Seed:
    return Seed(
        seed_num,
        seed_num,
        0
    )


def get_seeds(_input: list) -> list:
    '''
    assumes the first element in the input is the seeds
    '''
    return [make_seed(int(x)) for x in _input[0].split(':')[1].strip().split()]


def get_lowest_location(file_name: str) -> int:

    with open(file_name) as file:
        sections = file.read().split('\n\n')
        seeds = get_seeds(sections)

        for section in sections[1:]:
            print(section.split('\n')[0])

            for seed in seeds:

                for line in section.split('\n')[1:]:  # chop off the x-to-x map
                    sep_line = line.split(' ')
                    destination_start = int(sep_line[0])
                    source_start = int(sep_line[1])
                    _range = int(sep_line[2])

                    # for seed in seeds:
                    if source_start <= seed.source < (source_start + _range):
                        translation = destination_start - source_start
                        seed.source += translation
                        break

                if seed.seed_number == 14:
                    print(seed)

        lowest_seed = None
        print(len(seeds))
        for seed in seeds:
            if lowest_seed is None:
                lowest_seed = seed.source

            if seed.source < lowest_seed:
                lowest_seed = seed.source
        return lowest_seed

if __name__ == '__main__':
    print(get_lowest_location('input.txt'))