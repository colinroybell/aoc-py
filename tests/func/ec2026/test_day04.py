import pytest
from ec2026.day04 import Run_2026_04


class Test_2026_04:
    def setup_class(self):
        self.day = Run_2026_04()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 27598

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 6470

    @pytest.mark.skip
    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 0

    def test_regression_1(self):
        assert self.day.run_part("1") == 198726

    def test_regression_2(self):
        assert self.day.run_part("2") == 572513734

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
