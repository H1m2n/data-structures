# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

# Since we can only take cards from either front or end, this implies after chossing k cards,
# we will be left with n-k cards where n is number of cards. And since we need to find the max possible points we can achieve.
# The sum of cards left with us should be minimum. Hence we just need to find the contiguous array of size n-k such that
# its sum is minimum and subtract this value from the total sum of the array.

def max_points_from_card(cardPoints, k):
    # need to find out min n-k length of contiguous array
    cond = len(cardPoints) - k
    if cond == 0:
        return sum(cardPoints)
    min_points, points = (0, 0)
    i, j = (0, 0)
    while j < len(cardPoints):
        window_size = j - i + 1
        points = points + cardPoints[j]
        if window_size < cond:
            j += 1
        elif window_size == cond:
            if min_points == 0:
                # initialize min point var with current point
                min_points = points
            else:
                min_points = min(min_points, points)
            points = points - cardPoints[i]
            i += 1
            j += 1
    return sum(cardPoints) - min_points


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3

cardPoints = [9, 7, 7, 9, 7, 7, 9]
k = 7

cardPoints = [100, 40, 17, 9, 73, 75]
k = 3
print(max_points_from_card(cardPoints, k))
