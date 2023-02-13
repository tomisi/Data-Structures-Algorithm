class Solution(object):
    # In the containsDuplicate method of the Solution class, the nums list is passed as an argument to the method
    def containsDupicate(self, nums):
    # The method creates an empty hashset using the set() constructor:
        hashset = set()
    # Then, the method iterates over the elements of the nums list using a for loop
        for n in nums:
    # For each element n in the nums list, the method checks whether the element is already in the hashset using the in    operator:
            if n in hashset:
    #If the element n is in the hashset, then the method returns True, indicating that there is a duplicate element in the nums list.
# If the element n is not in the hashset, then the method adds the element to the hashset using the add() method:
                return True  # if we find a duplicate element, return True
            hashset.add(n)  # add the current element to the hashset
        return False  # if we reach this point, there are no duplicates in the lis