import pytest
from ec2024.day10 import Run_2024_10


class Test_2024_10:
    def setup_class(self):
        self.day = Run_2024_10()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == "PTBVRCZHFLJWGMNS"

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 1851

    @pytest.mark.skip
    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 3889

    def test_regression_1(self):
        assert self.day.run_part("1") == "RSMNGWJLCTXHVPKB"

    def test_regression_2(self):
        assert self.day.run_part("2") == 199259

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
