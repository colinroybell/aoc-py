year = 2015

init_filename = "src/aoc{}/__init__.py".format(year)
with open(init_filename, "w") as f:
    pass

init_tests_filename = "tests/func/aoc{}/__init__.py".format(year)
with open(init_tests_filename, "w") as f:
    pass

for num in range(1, 26):
    if num < 4 or num == 13:
        continue
    n = "{:02d}".format(num)

    main_file = """from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_{}_{}(DayBase):
    YEAR='{}'
    DAY='{}'


def part_a(input):
    assert 0, "not implemented"

def part_b(input):
    assert 0,"not implemented"

if __name__ == "__main__":
    Run_{}_{}().run_cmdline()
""".format(
        year, n, year, n, year, n
    )

    main_filename = "src/aoc{}/day{}.py".format(year, n)
    with open(main_filename, "w") as f:
        f.writelines(main_file)

    test_file = """import pytest
from aoc{}.day{} import Run_{}_{}

class Test_{}_{}:
    def setup_class(self):
        self.day = Run_{}_{}()

    def test_bringup_a(self):
        pass

    def test_bringup_b(self):   
        pass

    @pytest.mark.xfail
    def test_regression_a(self):
        assert(self.day.run_part('a') == 0)

    @pytest.mark.xfail
    def test_regression_b(self):    
        assert(self.day.run_part('b') == 0)

""".format(
        year, n, year, n, year, n, year, n
    )

    test_filename = "tests/func/aoc{}/test_day{}.py".format(year, n)
    with open(test_filename, "w") as f:
        f.writelines(test_file)
