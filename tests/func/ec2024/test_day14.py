import pytest
from ec2024.day14 import Run_2024_14


class Test_2024_14:
    def setup_class(self):
        self.day = Run_2024_14()

    def test_bringup_1(self):
        pass

    def test_bringup_2(self):
        pass

    def test_bringup_3(self):
        pass

    @pytest.mark.skip
    def test_regression_1(self):
        assert self.day.run_part("1") == 0

    @pytest.mark.skip
    def test_regression_2(self):
        assert self.day.run_part("2") == 0

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
