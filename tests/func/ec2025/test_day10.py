import pytest
from ec2025.day10 import Run_2025_10


class Test_2025_10:
    def setup_class(self):
        self.day = Run_2025_10()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1", steps=3) == 27

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2", steps=3) == 27

    @pytest.mark.skip
    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 0

    def test_regression_1(self):
        assert self.day.run_part("1") == 164

    def test_regression_2(self):
        assert self.day.run_part("2") == 1734

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
