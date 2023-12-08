from part1 import get_cards, get_matches


def insert_into_dic(key: str, dic: dict):
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1


def total_cards(filename: str) -> int:
    card_dict = dict()
    cards = get_cards(filename)

    for card_num in range(1, len(cards) + 1):
        card = cards[card_num - 1]
        insert_into_dic(str(card_num), card_dict)

        matches = get_matches(card)
        if matches > 0:
            for count in range(1, matches + 1):
                for _ in range(card_dict[str(card_num)]):
                    insert_into_dic(str(card_num + count), card_dict)

    print(card_dict)
    card_count = 0
    for card in card_dict:
        card_count += card_dict[card]

    return card_count

print(total_cards('input.txt'))

