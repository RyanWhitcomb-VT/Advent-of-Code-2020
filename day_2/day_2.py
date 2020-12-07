from collections import Counter


def parse_passwords(lines):
    count_list = []
    var_list = []
    input_list = []
    for line in lines:
        count_list.append(line.split(' ')[0])
        var_list.append(line.split(' ')[1][0])
        input_list.append(line.split(' ')[2])

    count_list = [(int(count.split('-')[0]), int(count.split('-')[1])) for count in count_list]

    return count_list, var_list, input_list


def part_1(count_list, var_list, input_list):
    valid_passwords = 0
    for idx, password in enumerate(input_list):
        low_bound = count_list[idx][0]
        high_bound = count_list[idx][1]
        var = var_list[idx]

        pass_count = Counter(password)
        if low_bound <= pass_count[var] <= high_bound:
            valid_passwords += 1

    return valid_passwords


def part_2(count_list, var_list, input_list):
    valid_passwords = 0
    for idx, password in enumerate(input_list):
        low_idx = count_list[idx][0] - 1
        high_idx = count_list[idx][1] - 1
        var = var_list[idx]

        pass_select = password[low_idx] + password[high_idx]
        pass_count = Counter(pass_select)

        if pass_count[var] == 1:
            valid_passwords += 1

    return valid_passwords


def main(lines):
    count_list, var_list, input_list = parse_passwords(lines)
    print(part_1(count_list, var_list, input_list))
    print(part_2(count_list, var_list, input_list))


if __name__ == '__main__':
    f = open('input.txt', 'r')
    data = f.readlines()
    main(data)