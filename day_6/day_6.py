import itertools


def main(groups):
    questions_answered = []
    all_answered = []
    for group in groups:
        group_str = ''.join(group.split('\n'))
        questions_answered.append(len(list(set(group_str))))

        members = group.count('\n') + 1
        num_answered = [len(list(group)) for key, group in itertools.groupby(sorted(group_str))]
        all_answered.append(num_answered.count(members))

    print(f"QUESTIONS ANSWERED: {sum(questions_answered)}")
    print(f"ALL ANSWERED: {sum(all_answered)}")


if __name__ == '__main__':
    f = open('input.txt', 'r')
    data = f.read().split('\n\n')
    main(data)
