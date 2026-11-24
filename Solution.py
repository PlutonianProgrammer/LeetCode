class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        def recursiveHelper(acc, index):

            # iterate through each number including start number
            for i in range(index, len(candidates)):

                # if combination resulting in target found, add to result
                if candidates[i] + sum(acc) == target:
                    result.append(acc + [candidates[i]])

                    # ascending list, so the next i results in a sum larger than target
                    return

                # if adding candidates[i] is < target, call recursively on the same index
                elif candidates[i] + sum(acc) < target:
                    recursiveHelper(acc + [candidates[i]], i)

                # if the sum is too large, exit, since the array is sorted
                else:
                    return

        # call for start with no accumulation and index 0
        recursiveHelper([], 0)

        return result