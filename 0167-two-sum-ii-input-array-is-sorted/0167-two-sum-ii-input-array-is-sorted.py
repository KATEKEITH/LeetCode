class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        s, e = 0, len(numbers) - 1

        while numbers[s] + numbers[e] != target:
            sums = numbers[s] + numbers[e]

            if sums < target:
                s += 1
            elif sums > target:
                s = 0
                e -= 1

        return [s+1, e+1]

