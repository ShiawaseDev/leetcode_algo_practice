def twoSum(nums, target):
        hsh_map = {}
        for val_index,value in enumerate(nums):
            difference = target - value
            if difference in hsh_map:
                return [hsh_map[difference], val_index]
            else:
                hsh_map[value] = val_index

assert twoSum(nums=[1,2,3,4,5,6,7,8], target=9) == [3,4]
assert twoSum(nums=[5,6,6,8], target=12) == [1,2]
assert twoSum(nums=[5,6,6,8], target=12) == [1,2]
assert twoSum(nums=[1,2,3,4,5,6,7,8], target=11) == [4,5]