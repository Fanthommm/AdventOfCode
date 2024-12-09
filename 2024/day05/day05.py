import time
from functools import cmp_to_key


def upgrade_is_valid(update, befores, afters):
    is_valid = True
    # print(update)
    for number_index in range(len(update)):
        for i in range(0, number_index):
            if update[number_index] in befores.keys():
                if update[i] not in befores[update[number_index]]:
                    is_valid = False
            else:
                is_valid = False
        for j in range(number_index + 1, len(update)):
            if update[number_index] in afters.keys():
                if update[j] not in afters[update[number_index]]:
                    is_valid = False
            else:
                is_valid = False
    if is_valid:
        # print(update[len(update) // 2])
        return update[len(update) // 2]
    else:
        return is_valid


def part_one(rules, updates, befores, afters):
    result_total = 0
    for update in updates:
        update = update.split(",")
        valid = upgrade_is_valid(update, befores, afters)
        if valid != False:
            result_total += int(valid)
    print(f"Part one : {result_total}")


def compare(a, b, afters):
    if b in afters.keys():
        # if a in afters[b] or b in befores[a]:
        if a in afters[b]:
            return 1
    if a in afters.keys():
        # if b in afters[a] or a in befores[b]:
        if b in afters[a]:
            return -1
    return 0


def part_two(rules, updates, befores, afters):
    result_total = 0
    for update in updates:
        update = update.split(",")
        valid = upgrade_is_valid(update, befores, afters)
        if valid == False:
            print(update)
            sorted_updates = sorted(
                update,
                key=cmp_to_key(lambda item1, item2: compare(item1, item2, afters)),
            )
            result_total += int(sorted_updates[len(sorted_updates) // 2])
    print(f"Part two : {result_total}")


# mylist = ['a', 'b', 'c', 'd', 'e']
# myorder = [3, 2, 0, 1, 4]
# mylist = [mylist[i] for i in myorder]
# print(mylist) # prints: ['d', 'c', 'a', 'b', 'e']

if __name__ == "__main__":
    with open("input.txt") as f:
        # with open("test_input.txt") as f:
        # with open('input_reda.txt') as f:
        lines = f.readlines()

    data = [line.rstrip() for line in lines]
    rules = data[: data.index("")]
    updates = data[data.index("") + 1 :]

    befores = {}
    afters = {}
    for r in rules:
        r = r.split("|")
        if r[1] not in befores.keys():
            befores[r[1]] = [r[0]]
        else:
            befores[r[1]].append(r[0])
        if r[0] not in afters.keys():
            afters[r[0]] = [r[1]]
        else:
            afters[r[0]].append(r[1])

    # print("Befores")
    # print(befores)
    # print("Afters")
    # print(afters)

    starttime = time.time()
    part_one(rules, updates, befores, afters)
    part_two(rules, updates, befores, afters)
    endtime = time.time()
    print(f"Execution time: {endtime-starttime}")
