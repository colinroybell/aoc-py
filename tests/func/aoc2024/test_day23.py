import pytest
from aoc2024.day23 import Run_2024_23

class Test_2024_23:
    def setup_class(self):
        self.day = Run_2024_23()
    
    @pytest.mark.skip
    def test_bringup_a(self):
        pass
    
    @pytest.mark.skip
    def test_bringup_b(self):
        pass

    @pytest.mark.skip
    def test_regression_a(self):
        assert(self.day.run_part('a') == 0)

    @pytest.mark.skip
    def test_regression_b(self):
        assert(self.day.run_part('b') == 0)

