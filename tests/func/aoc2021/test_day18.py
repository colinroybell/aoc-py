import pytest
from aoc2021.day18 import Run_2021_18, Node


class Test_2021_18:
    def setup_class(self):
        self.day = Run_2021_18()

    def test_bringup_a_parse_line(self):
        node = Node.parse_line(
            "[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"
        )
        assert (
            node.string()
            == "[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"
        )

    def test_bringup_a_parse(self):
        node = Node.parse(["[1,2]", "[[3,4],5]"])
        assert node.string() == "[[1,2],[[3,4],5]]"

    def test_bringup_a_explode_1(self):
        node = Node.parse_line("[[[[[9,8],1],2],3],4]")
        assert node.string() == "[[[[[9,8],1],2],3],4]"
        assert node.try_explode(0)
        assert node.string() == "[[[[0,9],2],3],4]"

    def test_bringup_a_explode_2(self):
        node = Node.parse_line("[7,[6,[5,[4,[3,2]]]]]")
        assert node.try_explode(0)
        assert node.string() == "[7,[6,[5,[7,0]]]]"

    def test_bringup_a_explode_3(self):
        node = Node.parse_line("[[6,[5,[4,[3,2]]]],1]")
        assert node.try_explode(0)
        assert node.string() == "[[6,[5,[7,0]]],3]"

    def test_bringup_a_explode_4(self):
        node = Node.parse_line("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
        assert node.try_explode(0)
        assert node.string() == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"

    def test_bringup_a_explode_5(self):
        node = Node.parse_line("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
        assert node.try_explode(0)
        assert node.string() == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"

    def test_bringup_a_split(self):
        node = Node.parse_line("[[[[0,7],4],[15,[0,13]]],[1,1]]")
        assert node.try_split()
        assert node.string() == "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"

    def test_bringup_a_1(self):
        node = Node.parse(self.day.input_filename("a", "test1"))
        assert node.string() == "[[[[1,1],[2,2]],[3,3]],[4,4]]"

    def test_bringup_a_2(self):
        node = Node.parse(self.day.input_filename("a", "test2"))
        print(node.string())
        assert node.string() == "[[[[3,0],[5,3]],[4,4]],[5,5]]"

    def test_bringup_a_3(self):
        node = Node.parse(self.day.input_filename("a,", "test3"))
        assert node.string() == "[[[[5,0],[7,4]],[5,5]],[6,6]]"

    def test_bringup_a_4(self):
        node = Node.parse(self.day.input_filename("a", "test4"))
        assert node.string() == "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"

    def test_bringup_a_5(self):
        assert self.day.run_part("a", ["[[1,2],[[3,4],5]]"]) == 143
        assert self.day.run_part("a", ["[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"]) == 1384
        assert self.day.run_part("a", ["[[[[1,1],[2,2]],[3,3]],[4,4]]"]) == 445
        assert self.day.run_part("a", ["[[[[3,0],[5,3]],[4,4]],[5,5]]"]) == 791
        assert self.day.run_part("a", ["[[[[5,0],[7,4]],[5,5]],[6,6]]"]) == 1137
        assert (
            self.day.run_part(
                "a", ["[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"]
            )
            == 3488
        )
        assert self.day.run_part("a", "test5") == 4140

    def test_bringup_a_6(self):
        node = Node.parse(self.day.input_filename("a,", "test6"))
        node.reduce()
        assert node.string() == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

    def test_bringup_b(self):
        assert self.day.run_part("b", "test5") == 3993

    def test_regression_a(self):
        assert self.day.run_part("a") == 4184

    def test_regression_b(self):
        assert self.day.run_part("b") == 4731
