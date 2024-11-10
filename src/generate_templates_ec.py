year = 2024

init_filename = "src/ec{}/__init__.py".format(year)
with open(init_filename, "w") as f:
    pass

init_tests_filename = "tests/func/ec{}/__init__.py".format(year)
with open(init_tests_filename, "w") as f:
    pass

for num in range(1, 21):
    n = "{:02d}".format(num)

    main_file = """from utils.day_base import DayBase
from utils.data_input import input_generator


class Run_{}_{}(DayBase):
    YEAR='{}'
    DAY='{}'
    PREFIX='ec'


def part_1(input):
    assert 0, "not implemented"

def part_2(input):
    assert 0,"not implemented"

def part_3(input):
    assert 0,"not implemented"    

if __name__ == "__main__":
    Run_{}_{}().run_cmdline()
""".format(
        year, n, year, n, year, n
    )

    main_filename = "src/ec{}/day{}.py".format(year, n)
    with open(main_filename, "w") as f:
        f.writelines(main_file)

    test_file = """import pytest
from ec{}.day{} import Run_{}_{}

class Test_{}_{}:
    def setup_class(self):
        self.day = Run_{}_{}()

    def test_bringup_1(self):
        pass

    def test_bringup_2(self):
        pass

    def test_bringup_3(self):
        pass
       

    @pytest.mark.skip
    def test_regression_a(self):
        assert(self.day.run_part('1') == 0)

    @pytest.mark.skip
    def test_regression_b(self):
        assert(self.day.run_part('2') == 0)
   
    @pytest.mark.skip
    def test_regression_b(self):
        assert(self.day.run_part('3') == 0)
     

""".format(
        year, n, year, n, year, n, year, n
    )

    test_filename = "tests/func/ec{}/test_day{}.py".format(year, n)
    with open(test_filename, "w") as f:
        f.writelines(test_file)
