import pytest
from ec2025.day14 import Run_2025_14


class Test_2025_14:
    def setup_class(self):
        self.day = Run_2025_14()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 200

    @pytest.mark.skip
    def test_bringup_3(self):
        assert self.day.run_part("3", "test3") == 0

    @pytest.mark.skip
    # Broke after fixing other tests: need to look at
    def test_regression_1(self):
        assert self.day.run_part("1") == 493

    @pytest.mark.skip
    def test_regression_2(self):
        assert self.day.run_part("2") == 1169445

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
