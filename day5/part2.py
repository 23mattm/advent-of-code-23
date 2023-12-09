from part1 import Seed, make_seed


def get_seeds(seed_line: str) -> list:
    '''
    returns a list of seeds from a seed line like
    seeds: x range y range z range...
    :param seed_line:
    :return:
    '''
    numbers = [int(x) for x in seed_line.split(':')[1].strip().split(' ')]

    seeds = list()
    _index = 0
    while _index < len(numbers) - 1:
        seed = make_seed(numbers[_index])
        seed.range = numbers[_index + 1]

        seeds.append(seed)
        _index += 2

    return seeds


def part_two(file_name: str) -> int:

    with open(file_name) as file:
        lines = file.read().split('\n\n')
        seeds = get_seeds(lines[0])



        for section in lines[1:]:

            _seeds = seeds.copy()
            for seed in _seeds:

                for line in section.split('\n')[1:]:

                    line_sep = line.split(' ')
                    destination_start = int(line_sep[0])
                    source_start = int(line_sep[1])
                    _range = int(line_sep[2])

                    translation = destination_start - source_start

                    if seed.source + seed.range <= source_start \
                            or seed.source > source_start + _range:
                        # none of these seeds are in the range
                        continue

                    if seed.source >= source_start and \
                            seed.source + seed.range <= source_start + _range:
                        # every seed in here fits in the range, just translate it
                        seed.source += translation
                        break

                    if seed.source < source_start:
                        # the source of the seed obj is less than the start,
                        # but there are some associated seeds in the range that need to be handled
                        partition = source_start - seed.source
                        seeds.remove(seed)
                        left_partition = make_seed(seed.source)
                        left_partition.range = partition - 1
                        right_partition = make_seed(seed.source + partition)
                        right_partition.range = seed.range - left_partition.range

                        seeds.append(left_partition)

                        right_partition.source += translation

                        seeds.append(right_partition)
                        break

                    if seed.source + seed.range > source_start + _range:
                        # the seeds extend beyond the limit, but there
                        # are some which still exist in the range
                        partition = source_start + _range - seed.source

                        seeds.remove(seed)
                        left_partition = make_seed(seed.source)
                        left_partition.range = partition - 1
                        right_partition = make_seed(seed.source + partition)
                        right_partition.range = seed.range - left_partition.range

                        seeds.append(right_partition)

                        left_partition.source += translation

                        seeds.append(left_partition)
                        break

        lowest = None
        print(seeds)
        for seed in seeds:
            if lowest is None:
                lowest = seed.source

            if seed.source < lowest:
                lowest = seed.source

        return lowest


if __name__ == "__main__":
    print('example', part_two('example.txt'))
    print('input', part_two('input.txt'))