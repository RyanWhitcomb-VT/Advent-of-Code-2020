def part_1(input):
    for x in input:
        for y in input:
            if x+y == 2020:
                return(x*y)

def part_2(input):
    for x in input:
        for y in input:
            for z in input:
                if x+y+z == 2020:
                    return(x*y*z)

def main(input):
    print(part_1(input))
    print(part_2(input))


if __name__ == '__main__':
    f = open("input.txt", "r")
    input = f.readlines()
    input = [int(x) for x in input]

    main(input)