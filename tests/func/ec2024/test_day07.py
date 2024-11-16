import pytest
from ec2024.day07 import Run_2024_07


class Test_2024_07:
    def setup_class(self):
        self.day = Run_2024_07()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == "BDCA"

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == "DCBA"

    def test_regression_1(self):
        assert self.day.run_part("1") == "BACIEDKJG"

    def test_regression_2(self):
        assert self.day.run_part("2") == "EGAHIKJFC"

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
