import pytest
from ec2025.day09 import Run_2025_09


class Test_2025_09:
    def setup_class(self):
        self.day = Run_2025_09()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 414

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 1245

    def test_bringup_3_1(self):
        assert self.day.run_part("3", "test3") == 12

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test4") == 36

    def test_regression_1(self):
        assert self.day.run_part("1") == 6512

    def test_regression_2(self):
        assert self.day.run_part("2") == 316895

    @pytest.mark.slow
    def test_regression_3(self):
        assert self.day.run_part("3") == 40528
