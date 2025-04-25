import pytest
from codyssi2025.day16 import Run_2025_16


class Test_2025_16:
    def setup_class(self):
        self.day = Run_2025_16()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 6902016000

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
