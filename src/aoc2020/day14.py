from utils.day_base import DayBase
from utils.data_input import input_generator
import re


class Run_2020_14(DayBase):
    YEAR = "2020"
    DAY = "14"


def part_a(input):
    mask_re = re.compile(r"mask = (.{36})")
    mem_re = re.compile(r"mem\[(\d+)\] = (\d+)")
    mem = {}
    mask = []
    for line in input_generator(input):
        m = mask_re.match(line)
        if m:
            mask = m.group(1)[::-1]
        m = mem_re.match(line)
        if m:
            address = int(m.group(1))
            input_val = int(m.group(2))
            output_val = 0
            for i in range(0, 36):
                mask_bit = mask[i]
                if mask_bit == "X":
                    bit = input_val % 2
                else:
                    bit = int(mask_bit)
                input_val = input_val // 2
                output_val += bit * (2 ** i)
            mem[address] = output_val
    sum_ = 0
    for _, v in mem.items():
        sum_ += v
    return sum_


def part_b(input):
    mask_re = re.compile(r"mask = (.{36})")
    mem_re = re.compile(r"mem\[(\d+)\] = (\d+)")
    mem = {}
    write_offsets = []
    for line in input_generator(input):
        m = mask_re.match(line)
        if m:
            mask = m.group(1)[::-1]
            write_offsets = [0]
            for i in range(0, 36):
                if mask[i] == "X":
                    inc = 2 ** i
                    current_len = len(write_offsets)
                    for offset in range(0, current_len):
                        write_offsets.append(write_offsets[offset] + inc)
        m = mem_re.match(line)
        if m:
            address = int(m.group(1))
            input_val = int(m.group(2))
            base_address = 0
            for i in range(0, 36):
                mask_bit = mask[i]
                if mask_bit == "X":
                    bit = 0
                elif mask_bit == "0":
                    bit = address % 2
                else:
                    bit = 1
                address = address // 2
                base_address += bit * (2 ** i)
            for offset in write_offsets:
                mem[base_address + offset] = input_val
    sum_ = 0
    for _, v in mem.items():
        sum_ += v
    return sum_


if __name__ == "__main__":
    Run_2020_14().run_cmdline()
