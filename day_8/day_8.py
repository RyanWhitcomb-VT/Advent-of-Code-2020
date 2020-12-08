def traverse(instructions):
    accumulator = 0
    idx_list = []
    idx = 0
    while True:
        if idx in idx_list:
            return accumulator
        else:
            idx_list.append(idx)

        inst, val = instructions[idx].split(' ')
        if inst == 'acc':
            accumulator += int(val)
            idx += 1
        elif inst == 'jmp':
            idx += int(val)
        else:
            idx += 1


def find_end(instructions):
    bad_inst = []
    for idx, line in enumerate(instructions):
        inst = line.split(' ')[0]
        if inst == 'jmp' or inst == 'nop':
            bad_inst.append(idx)

    for bad_idx in bad_inst:
        accumulator = 0
        idx_list = []
        idx = 0
        while idx not in idx_list:
            idx_list.append(idx)

            inst, val = instructions[idx].split(' ')
            if inst == 'acc':
                accumulator += int(val)
                idx += 1
            elif inst == 'jmp':
                if idx == bad_idx:
                    idx += 1
                idx += int(val)
            elif inst == 'nop':
                if idx == bad_idx:
                    idx += int(val)
                idx += 1
            else:
                return accumulator


def main(instructions):
    print(traverse(instructions))
    print(find_end(instructions))


if __name__ == '__main__':
    f = open('input.txt', 'r')
    data = f.readlines()
    main(data)