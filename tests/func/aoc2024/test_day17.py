import pytest
from aoc2024.day17 import Run_2024_17, init, set_register, get_register, run_program


class Test_2024_17:
    def setup_class(self):
        self.day = Run_2024_17()

    def test_bringup_a_1(self):
        init()
        set_register("C", 9)
        run_program([2, 6])
        assert get_register("B") == 1

    def test_bringup_a_2(self):
        init()
        set_register("A", 10)
        output = run_program([5, 0, 5, 1, 5, 4])
        assert output == "0,1,2"

    def test_bringup_a_3(self):
        init()
        set_register("A", 2024)
        output = run_program([0, 1, 5, 4, 3, 0])
        assert output == "4,2,5,6,7,7,7,7,3,1,0"
        assert get_register("A") == 0

    def test_bringup_a_6(self):
        assert self.day.run_part("a", "test1") == "4,6,3,5,6,3,5,2,1,0"

    @pytest.mark.skip
    def test_bringup_b(self):
        pass

    def test_regression_a(self):
        assert self.day.run_part("a") == "1,5,0,1,7,4,1,0,3"

    def test_regression_b(self):
        assert self.day.run_part("b") == 47910079998866
