import pytest
from ec2024.day20 import Run_2024_20


class Test_2024_20:
    def setup_class(self):
        self.day = Run_2024_20()

    # We wrote a bespoke test for this one
    # def test_bringup_1(self):
    #    pass

    @pytest.mark.skip
    def test_bringup_2_2(self):
        assert self.day.run_part("2", "test2") == 24

    @pytest.mark.skip
    def test_bringup_2_3(self):
        assert self.day.run_part("2", "test2") == 78

    @pytest.mark.skip
    def test_bringup_2_4(self):
        assert self.day.run_part("2", "test2") == 206

    def test_regression_1(self):
        assert self.day.run_part("1") == 1032

    @pytest.mark.skip
    def test_regression_2(self):
        assert self.day.run_part("2") == 0

    @pytest.mark.skip
    def test_regression_3(self):
        assert self.day.run_part("3") == 0
