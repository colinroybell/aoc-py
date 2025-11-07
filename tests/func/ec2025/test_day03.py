import pytest
from ec2025.day03 import Run_2025_03


class Test_2025_03:
    def setup_class(self):
        self.day = Run_2025_03()

    @pytest.mark.skip
    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 0

    @pytest.mark.skip
    def test_bringup_2(self):
        assert self.day.run_part("1", "test1") == 0

    @pytest.mark.skip
    def test_bringup_3(self):
        assert self.day.run_part("1", "test1") == 0

    @pytest.mark.skip
    def test_regression_1(self):
        assert self.day.run_part("1") == 0

    @pytest.mark.skip
    def test_regression_2(self):
        assert self.day.run_part("2") == 0

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
