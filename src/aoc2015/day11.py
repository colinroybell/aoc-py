from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2015_11(DayBase):
    YEAR = "2015"
    DAY = "11"


def next_letter(c):
    return chr(97 + (ord(c) - 97 + 1) % 26)


def update_rule_1(pw):
    for n, c in enumerate(pw):
        if c == "i" or c == "o" or c == "l":
            new_pw = pw[0:n] + next_letter(c) + "a" * (7 - n)
            print("Rule 1: {}".format(new_pw))
            return True, new_pw
    return False, pw


def update_rule_2(pw):
    last = None
    doubles = []
    last_double_pos = None
    for n in range(0, 7):
        if pw[n] == pw[n + 1] and pw[n] not in doubles:
            doubles.append(pw[n])
            last_double_pos = n
    if len(doubles) >= 2:
        return False, pw
    new_pw = list(pw)
    new_pw[7] = next_letter(new_pw[7])
    pos = 7
    while new_pw[pos] == "a" and pos > 0:
        pos -= 1
        new_pw[pos] = next_letter(new_pw[pos])
    pw = "".join(new_pw)
    print("Rule 2: {}".format(pw))
    return True, pw


def update_rule_3(pw):
    old_pw = pw
    for n in range(0, 6):
        if ord(pw[n + 1]) - ord(pw[n]) == 1 and ord(pw[n + 2]) - ord(pw[n + 1]) == 1:
            return False, pw

    # Brute force version. What I'd done below is misread the question (yza, zab don't count). I think I got the right answer at some point but didn't type it in right.
    new_pw = list(pw)
    new_pw[7] = next_letter(new_pw[7])
    pos = 7
    while new_pw[pos] == "a" and pos > 0:
        pos -= 1
        new_pw[pos] = next_letter(new_pw[pos])
    pw = "".join(new_pw)
    print("Rule 2: {}".format(pw))
    return True, pw

    new_pw = list(pw)
    new_pw[6] = next_letter(new_pw[5])
    new_pw[7] = next_letter(new_pw[6])
    pw = "".join(new_pw)
    if pw > old_pw:
        print("Rule 3: {}".format(pw))
        return True, pw

    new_pw[5] = next_letter(new_pw[5])
    pos = 5
    while new_pw[pos] == "a" and pos > 0:
        pos -= 1
        new_pw[pos] = next_letter(new_pw[pos])
    new_pw[6] = next_letter(new_pw[5])
    new_pw[7] = next_letter(new_pw[6])
    pw = "".join(new_pw)
    print("Rule 3: {}".format(pw))
    assert pw > old_pw
    return True, pw


import re


def next_password(pw):
    new_pw = list(pw)
    new_pw[7] = next_letter(new_pw[7])
    pos = 7
    while new_pw[pos] == "a" and pos > 0:
        pos -= 1
        new_pw[pos] = next_letter(new_pw[pos])
    pw = "".join(new_pw)

    ok = False
    while not ok:
        update1, pw = update_rule_1(pw)
        update2, pw = update_rule_2(pw)
        update3, pw = update_rule_3(pw)
        print(update1, update2, update3)
        ok = (not update1) and (not update2) and (not update3)
    return pw


def part_a(input):
    pw = next(input_generator(input))
    return next_password(pw)


def part_b(input):
    pw = next(input_generator(input))
    return next_password(next_password(pw))


if __name__ == "__main__":
    Run_2015_11().run_cmdline()
