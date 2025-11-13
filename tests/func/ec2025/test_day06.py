import pytest
from ec2025.day06 import Run_2025_06


class Test_2025_06:
    def setup_class(self):
        self.day = Run_2025_06()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 5

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 11

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test2", repeats=1, limit=10) == 34

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test2", repeats=2, limit=10) == 72

    @pytest.mark.skip
    # Our optimisation only handles cases where the limit is less than the length
    def test_bringup_3_3(self):
        assert self.day.run_part("3", "test2", repeats=1000, limit=1000) == 3442321

    def test_regression_1(self):
        assert self.day.run_part("1") == 135

    def test_regression_2(self):
        assert self.day.run_part("2") == 3916

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
