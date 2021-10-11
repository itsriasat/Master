class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return -1, -1

        def FirstBinarySearch(arr, low, high, target):
            while low <= high:
                mid = low + (high - low) // 2
                if mid == 0 and arr[mid] == target:
                    return mid
                elif arr[mid] == target and arr[mid - 1] != target:
                    return mid
                elif arr[mid] > target:
                    high = mid - 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    low = low - 1
            return -1

        def LastBinarySearch(arr, low, high, target):
            while low <= high:
                mid = low + (high - low) // 2
                if mid == len(arr) - 1 and arr[mid] == target:
                    return mid
                elif arr[mid] == target and arr[mid + 1] != target:
                    return mid
                elif arr[mid] > target:
                    high = mid - 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    low = low + 1
            return -1

        first_position = FirstBinarySearch(nums, 0, len(nums) - 1, target)
        last_position = LastBinarySearch(nums, first_position, len(nums) - 1, target)
        return first_position, last_position
