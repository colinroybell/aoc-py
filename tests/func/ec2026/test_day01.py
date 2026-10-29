import pytest
from ec2026.day01 import Run_2026_01

class Test_2026_01:
    def setup_class(self):
        self.day = Run_2026_01()
   
    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 11

    def test_bringup_2(self):
        assert self.day.run_part("2", "test1") == 9

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == 61
       
    def test_regression_1(self):
        assert(self.day.run_part('1') == 1461)

    def test_regression_2(self):
        assert(self.day.run_part('2') == 303)
   
    def test_regression_3(self):
        assert(self.day.run_part('3') == 654807)
     

