import math
import itertools
import operator


def binary_partition(min_range, max_range, binary_list):
    if binary_list[0]:
        mid = math.ceil((min_range + max_range)/2)
    else:
        mid = math.floor((min_range + max_range)/2)
    if mid == min_range or mid == max_range:
        return mid

    if binary_list[0]:
        return binary_partition(mid, max_range, binary_list[1:])
    else:
        return binary_partition(min_range, mid, binary_list[1:])


def parse_passes(passes):
    seat_list = []
    for bpass in passes:
        row_binary = [0 if char == 'F' else 1 for char in bpass[:7]]
        col_binary = [0 if char == 'L' else 1 for char in bpass[7:]]

        seat_list.append((binary_partition(0,127,row_binary), binary_partition(0,7,col_binary)))
    return seat_list


def find_seats(seats):
    possible_seats = []
    seat_gb = itertools.groupby(seats, operator.itemgetter(0))
    for key, subiter in seat_gb:
        key_list = list(subiter)
        print(key, key_list)
        if len(key_list) != 8:
            key_seats = [seat[1] for seat in key_list]
            missing_seat = set(range(8)).difference(key_seats)
            possible_seats.append((key, missing_seat))
    return possible_seats


def main(boarding_passes):
    seats = parse_passes(boarding_passes)
    seat_ids = [row * 8 + col for row,col in seats]
    print(f"MAX ID: {max(seat_ids)}")

    sorted_seats = sorted(seats, key=lambda tup: tup[0])
    print(find_seats(sorted_seats))


if __name__ == '__main__':
    f = open('input.txt', 'r')
    data = f.readlines()
    main(data)