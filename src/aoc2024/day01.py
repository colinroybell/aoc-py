from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_2024_01(DayBase):
    YEAR='2024'
    DAY='01'


def part_a(input):
    return next(input_generator(input))

def part_b(input):
    assert 0,"not implemented"

if __name__ == "__main__":
    Run_2024_01().run_cmdline()
