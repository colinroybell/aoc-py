import pytest
from codyssi2025.day15 import Run_2025_15


class Test_2025_15:
    def setup_class(self):
        self.day = Run_2025_15()

    def test_bringup_1(self):
        assert self.day.run_part("1", "test1") == 12645822

    def test_bringup_2(self):
        assert (
            self.day.run_part("2", "test1")
            == "ozNxANO-pYNonIG-MUantNm-lOSlxki-SDJtdpa-JSXfNAJ"
        )

    def test_bringup_3(self):
        assert self.day.run_part("3", "test1") == "pYNonIG"

    def test_regression_1(self):
        assert self.day.run_part("1") == 1032203140

    def test_regression_2(self):
        assert (
            self.day.run_part("2")
            == "ngdFUNx-SzDtKLI-ExIDZdB-xbhPRVY-fqOyhHs-ZPmuSlA-fGYNHFt-LIgFUqn-bZPrexp-FXUrnFE-AVKXlZs-syCbUig"
        )

    def test_regression_3(self):
        assert self.day.run_part("3") == "SzDtKLI"
