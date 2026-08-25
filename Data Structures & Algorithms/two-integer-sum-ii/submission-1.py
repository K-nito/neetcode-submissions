class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr = 0
        rightPtr = len(numbers) - 1

        while leftPtr < rightPtr:
            #Since it's sorted, moving the left ptr will only increase sum. So move right ptr
            if numbers[leftPtr] + numbers[rightPtr] > target:
                rightPtr -= 1
            #Return if match is found
            elif numbers[leftPtr] + numbers[rightPtr] == target:
                return [leftPtr + 1, rightPtr + 1]
            #If sum < target, decreasing right ptr won't increase sum. So move left ptr
            else:
                leftPtr += 1

        return -1
