from utils.day_base import DayBase
from utils.data_input import input_generator
import hashlib


class Run_2016_05(DayBase):
    YEAR = "2016"
    DAY = "05"


def part_a(input):
    doorid = next(input_generator(input))
    count = 0
    found = 0
    output = ""
    while found < 8:
        string = doorid + str(count)
        string = string.encode("utf-8")
        hash = hashlib.md5(string).hexdigest()
        if hash[0:5] == "00000":
            found += 1
            output += hash[5]
            print(string, count, hash, output)
        count += 1
    return output


def part_b(input):
    doorid = next(input_generator(input))
    count = 0
    found = 0
    output = "________"
    while "_" in output:
        string = doorid + str(count)
        string = string.encode("utf-8")
        hash = hashlib.md5(string).hexdigest()
        if hash[0:5] == "00000":
            pos = int(hash[5], 16)
            if pos < 8 and output[pos] == "_":
                output = output[:pos] + hash[6] + output[pos + 1 :]
                print(count, hash, output)
        count += 1
    return output


if __name__ == "__main__":
    Run_2016_05().run_cmdline()
