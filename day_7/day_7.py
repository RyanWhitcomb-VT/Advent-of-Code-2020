def create_dependencies(rules):
    rule_dict = {}
    for rule in rules:
        rule_key, contains = rule.split('contain')
        contains_dict = {}
        for bag in contains.strip().split(' , '):
            bag_count = bag.split(' ')[0].strip()
            if bag_count == 'no':
                bag_count = '0'
                bag_name = 'no other'
            else:
                bag_name = ' '.join(bag.split(' ')[1:])
            contains_dict[bag_name.strip()] = int(bag_count.strip())
        rule_dict[rule_key.strip()] = contains_dict
    return rule_dict


def traverse_dict(bags_dict, init_bag_types):
    while True:
        change_count = len(init_bag_types)
        for bag in bags_dict:
            if set(init_bag_types).intersection(bags_dict[bag].keys()):
                init_bag_types.add(bag)
        if len(init_bag_types) == change_count:
            return init_bag_types


def bag_contains(bag_dict, bag_info):
    bag_count = 0
    if sum(bag_info.values()) == 0:
        return 0
    else:
        for bag in bag_info.keys():
            add = bag_info[bag]
            mult = bag_info[bag]*bag_contains(bag_dict, bag_dict[bag])
            bag_count += (add + mult)
    return bag_count


def main(rules):
    bags_dict = create_dependencies(rules)

    shiny_gold_count = traverse_dict(bags_dict, {'shiny gold'})
    shiny_gold_contains = bag_contains(bags_dict, bags_dict['shiny gold'])
    print(f"CONTAINS SHINY GOLD: {len(shiny_gold_count) - 1}")
    print(f"SHINY GOLD CONTAINS: {shiny_gold_contains}")


if __name__ == '__main__':
    f = open('input.txt', 'r')
    data = f.readlines()
    data = [line.replace('bags', '').replace('.', '').replace('\n', '').replace('bag', '') for line in data]
    main(data)
