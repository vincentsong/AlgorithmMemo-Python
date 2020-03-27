from .dp_53_maximum_subarray import Solution53
from .dp_70_climbing_stairs import Solution70


class TestLeetCodeDPs:

    def test_max_sub_array(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        assert Solution53.max_sub_array(nums) == 6

    def test_climb_stairs(self):
        assert Solution70.climb_stairs(5) == 8
