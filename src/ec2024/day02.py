from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_02(DayBase):
    YEAR = "2024"
    DAY = "02"
    PREFIX = "ec"


def part_1(input, phrase=None):
    generator = input_generator(input)
    word_line = next(generator)
    blank = next(generator)
    if phrase == None:
        phrase = next(generator)
    word_line = word_line[6:]
    words = word_line.split(",")
    print(words)
    count = 0
    for word in words:
        wlen = len(word)
        for i in range(len(phrase) - wlen + 1):
            if phrase[i : i + wlen] == word:
                count += 1
                print(i, word)
    return count


def part_2(input):
    generator = input_generator(input)
    word_line = next(generator)
    word_line = word_line[6:]
    words = word_line.split(",")
    blank = next(generator)
    count = 0

    for phrase in generator:
        found = [0 for _ in range(len(phrase))]
        print(phrase)
        for word in words:
            wlen = len(word)
            for i in range(len(phrase) - wlen + 1):
                forward = phrase[i : i + wlen]
                backward = forward[::-1]
                # print(forward, backward)
                if forward == word or backward == word:
                    for i in range(i, i + wlen):
                        found[i] = 1

        count += sum(found)
        print(phrase, count)
    return count


def part_3(input):
    generator = input_generator(input)
    word_line = next(generator)
    word_line = word_line[6:]
    words = word_line.split(",")
    blank = next(generator)
    count = 0

    grid = []
    for phrase in generator:
        grid.append(phrase)
    width = len(grid[0])
    height = len(grid)

    found = [[0 for _ in range(width)] for _ in range(height)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for x in range(width):
        for y in range(height):
            for (xd, yd) in dirs:
                for word in words:
                    wlen = len(word)
                    ok = True
                    for i in range(wlen):
                        xx = (x + i * xd) % width
                        yy = y + i * yd
                        if yy < 0 or yy >= height or grid[yy][xx] != word[i]:
                            ok = False
                            break
                    if ok:
                        print("Found {} at {} {} + {} {}".format(word, x, y, xd, yd))
                        for i in range(wlen):
                            xx = (x + i * xd) % width
                            yy = y + i * yd
                            found[yy][xx] = 1
    print(found)
    for i in range(height):
        count += sum(found[i])
    return count


if __name__ == "__main__":
    Run_2024_02().run_cmdline()
