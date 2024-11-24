import pytest
from ec2024.day15 import Run_2024_15


class Test_2024_15:
    def setup_class(self):
        self.day = Run_2024_15()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 26

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 38

    def test_regression_1(self):
        assert self.day.run_part("1") == 188

    def test_regression_2(self):
        assert self.day.run_part("2") == 504

    @pytest.mark.skip
    def test_regression_3(self):
        # Skip as very long
        assert self.day.run_part("3") == 1540
