from typing import List
import pytest


class TestBinarySearch:

    @pytest.fixture
    def data(self):
        return [1, 3, 6, 9, 10]

    def binary_search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        mid = len(nums) // 2
        if mid == target:
            return mid
        if target < nums[mid]:
            return self.binary_search(nums[:mid], target)
        else:
            return self.binary_search(nums[mid+1:], target)

    def test_binary_search(self, data):
        print(self.binary_search(data, 3))
