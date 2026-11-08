import pytest
from ec2026.day10 import Run_2026_10


class Test_2026_10:
    def setup_class(self):
        self.day = Run_2026_10()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 29

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2", counter=10) == 53

    @pytest.mark.skip
    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 0

    def test_regression_1(self):
        assert self.day.run_part("1") == 52

    def test_regression_2(self):
        assert self.day.run_part("2") == 142141

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
