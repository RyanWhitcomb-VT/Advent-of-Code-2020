BIRTH = 'byr'
ISSUE = 'iyr'
EXPIRATION = 'eyr'
HEIGHT = 'hgt'
HAIR = 'hcl'
EYE = 'ecl'
PASS_ID = 'pid'
COUNTRY_ID = 'cid'

YEAR_LEN = 4


def parse_passport(passport):
    passport_key_value = passport.split(' ')
    passport_key_value = [kv.split(':') for kv in passport_key_value]
    return dict(passport_key_value)


def parse_data(passports):
    passport_list = passports.split('\n\n')
    passport_list = [passport.replace('\n', ' ') for passport in passport_list]
    return passport_list


def validate_field_rules(pass_dict):
    byr = pass_dict[BIRTH]
    iyr = pass_dict[ISSUE]
    eyr = pass_dict[EXPIRATION]
    hgt = pass_dict[HEIGHT]
    hcl = pass_dict[HAIR]
    ecl = pass_dict[EYE]
    pid = pass_dict[PASS_ID]

    if byr < '1920' or byr > '2002':
        return False

    if iyr < '2010' or iyr > '2020':
        return False

    if eyr < '2020' or eyr > '2030':
        return False

    if not hgt.endswith(('in', 'cm')):
        return False
    else:
        if hgt.endswith('cm') and (hgt[:-2] < '150' or hgt[:-2] > '193'):
            return False
        if hgt.endswith('in') and (hgt[:-2] < '59' or hgt[:-2] > '76'):
            return False

    if len(hcl) != 7 or hcl[0] != '#' or not hcl[1:].isalnum():
        return False

    if ecl not in ['amb','blu','brn','gry','grn','hzl','oth']:
        return False

    if len(pid) != 9 or not pid.isnumeric():
        return False

    return True


def main(passports):
    field_list = [BIRTH, ISSUE, EXPIRATION, HEIGHT, HAIR, EYE, PASS_ID]
    part_1 = 0
    part_2 = 0
    for passport in passports:
        passport_dict = parse_passport(passport)

        # Part 1
        passport_fields = list(passport_dict.keys())
        if len(set(field_list).intersection(passport_fields)) == len(field_list):
            part_1 += 1

            # Part 2
            if validate_field_rules(passport_dict):
                part_2 += 1

    print(f'PART 1: {part_1}')
    print(f'PART 2: {part_2}')


if __name__ == '__main__':
    f = open('input.txt', 'r')
    data = parse_data(f.read())
    main(data)
