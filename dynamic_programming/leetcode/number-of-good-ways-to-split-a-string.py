class Solution:
    def numSplits(self, s: str) -> int:
        """
        Approach ->
        1. first create a right map, to already have records for comparison at right partition
        2. we need to create left partition now by looping again, but this time loop should not include last element of array,
           because if we include it, we can't have right partition at very end as on element can't reside in both the
           partition
        3. whenever we including a element in left partition, we need to exclude it from the right partition.
        4. compare the length of keys, if it is equal then it is good way to split string
        """
        count = 0
        right_map = {}
        for x in s:
            if x in right_map:
                right_map[x] = right_map[x] + 1
            else:
                right_map[x] = 1
        left_map = {}
        for x in s[0:len(s) - 1]:
            # This step required for partition purpose, because an element can't be in both partition
            if x in right_map:
                right_map[x] = right_map[x] - 1
                if right_map[x] == 0:
                    del (right_map[x])

            if x in left_map:
                left_map[x] = left_map[x] + 1
            else:
                left_map[x] = 1

            if len(left_map.keys()) == len(right_map.keys()):
                count += 1
        return count


obj = Solution()
s = "aacaba"
s = 'abcd'
s = 'aaaaa'
s = 'acbadbaada'
print(obj.numSplits(s))
