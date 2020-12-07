import math


def parse_line(line):
    tree_locs = []
    line_list = list(line)
    for idx, val in enumerate(line_list):
        if val == '#':
            tree_locs.append(idx)

    return tree_locs


def slope_intersect(tree_map, rise, run, width):
    offset = 0
    tree_count = 0
    for row in range(0, len(tree_map), rise):
        adj_offset = offset % width
        if adj_offset in tree_map[row]:
            tree_count += 1
        offset += run
    return tree_count


def main(tree_map):
    map_width = len(tree_map[0])
    tree_dict = {}
    for idx, line in enumerate(tree_map):
        tree_dict[idx] = parse_line(line)

    print(f"Part 1: {slope_intersect(tree_dict, 1, 3, map_width)}")

    part_2_trees = []
    part_two_input = [[1,1], [1,3], [1,5], [1, 7], [2, 1]]
    for dims in part_two_input:
        part_2_trees.append(slope_intersect(tree_dict, dims[0], dims[1], map_width))

    print(f"Part 2: {math.prod(part_2_trees)}")


if __name__ == '__main__':
    f = open('input.txt', 'r')
    data = f.read().splitlines()

    main(data)