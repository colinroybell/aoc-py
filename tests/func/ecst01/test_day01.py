import pytest
from ecst01.day01 import Run_st01_01, eni, part_1_value


class Test_st01_01:
    def setup_class(self):
        self.day = Run_st01_01()

    def test_bringup_eni(self):
        Run_st01_01.PART = 1
        assert eni(2, 4, 5) == 1342
        assert eni(3, 5, 16) == 311193

    def test_bringup_part_1_value(self):
        Run_st01_01.PART = 1
        assert part_1_value("A=4 B=4 C=6 X=3 Y=4 Z=5 M=11") == 114644
        assert part_1_value("A=8 B=4 C=7 X=8 Y=4 Z=6 M=12") == 48661009
        assert part_1_value("A=2 B=8 C=6 X=2 Y=4 Z=5 M=13") == 313276
        assert part_1_value("A=5 B=9 C=6 X=8 Y=6 Z=8 M=14") == 11611972920
        assert part_1_value("A=5 B=9 C=7 X=6 Y=6 Z=8 M=15") == 1240513421
        assert part_1_value("A=8 B=8 C=8 X=6 Y=9 Z=6 M=16") == 24

    def test_bringup_1(self):
        Run_st01_01.PART = 1
        assert self.day.run_part("1", "test1") == 11611972920

    def test_bringup_eni_part_2(self):
        Run_st01_01.PART = 2
        assert eni(2, 7, 5) == 34213
        assert eni(3, 8, 16) == 111931

    def test_bringup_part_1_value_part_2(self):
        Run_st01_01.PART = 2
        assert part_1_value("A=4 B=4 C=6 X=3 Y=14 Z=15 M=11") == 150231
        assert part_1_value("A=8 B=4 C=7 X=8 Y=14 Z=16 M=12") == 110099
        assert part_1_value("A=2 B=8 C=6 X=2 Y=14 Z=15 M=13") == 9387665
        assert part_1_value("A=5 B=9 C=6 X=8 Y=16 Z=18 M=14") == 1113198
        assert part_1_value("A=5 B=9 C=7 X=6 Y=16 Z=18 M=15") == 11051340
        assert part_1_value("A=8 B=8 C=8 X=6 Y=19 Z=16 M=16") == 0

    def test_bringup_2(self):
        assert self.day.run_part("2", "test2") == 11051340

    def test_bringup_2_2(self):
        assert self.day.run_part("2", "test3") == 1507702060886

    def test_bringup_eni_part_3(self):
        Run_st01_01.PART = 3
        assert eni(2, 7, 5) == 19
        assert eni(3, 8, 16) == 48

    def test_bringup_part_1_value_part_3(self):
        Run_st01_01.PART = 3

        assert part_1_value("A=4 B=4 C=6 X=3000 Y=14000 Z=15000 M=110") == 1573000
        assert part_1_value("A=8 B=4 C=7 X=8000 Y=14000 Z=16000 M=120") == 1439940
        assert part_1_value("A=2 B=8 C=6 X=2000 Y=14000 Z=15000 M=130") == 2079860
        assert part_1_value("A=5 B=9 C=6 X=8000 Y=16000 Z=18000 M=140") == 2407850
        assert part_1_value("A=5 B=9 C=7 X=6000 Y=16000 Z=18000 M=150") == 2099880
        assert part_1_value("A=8 B=8 C=8 X=6000 Y=19000 Z=16000 M=160") == 3279640

    def test_bringup_3(self):
        assert self.day.run_part("3", "test4") == 3279640

    def test_bringup_3_2(self):
        assert self.day.run_part("3", "test5") == 7276515438396

    def test_regression_1(self):
        assert self.day.run_part("1") == 8168337335

    def test_regression_2(self):
        assert self.day.run_part("2") == 301260262247223

    def test_regression_3(self):
        assert self.day.run_part("3") == 496392042644159
