class Solution:
    count = 0

    def calculate(self, n, pos, visited):
        """
        Tries for 123 permutation
        All permutations lies on the branch in DFS fashion
                    0
                 /  \  \
                1   2   3
              /  \  / \  / \
             2    3 1  3 1  2
             |    | |  | |  |
             3    2 3  1 2  1
        """
        if pos > n:
            # if we successfully traverse the array means we are meeting the permutation rule, so
            # increase the count by 1, and check for next element by starting it at first position
            self.count += 1
            pos = 1
        for i in range(1, n + 1):
            # if we getting a number check if it is visited or not, if it is not then check for permutation rule
            # if both condition is true, then only go deeper to include other non visited element.
            # The flow is ->
            # we are trying to placing a number at each position. If it already visited, then at that position,
            # we are placing other number(as we looping again, so already visited will be discarded), so like wise
            # this looping process create all permutation
            if not visited[i] and (pos % i == 0 or i % pos == 0):
                visited[i] = True
                self.calculate(n, pos + 1, visited)
                visited[i] = False

    def countArrangement(self, n: int) -> int:
        visited = [False] * (n + 1)
        self.calculate(n, 1, visited)
        return self.count


obj = Solution()
print(obj.countArrangement(12))
