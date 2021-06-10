# We have n number of records in a list, a row contains id, name, location and vote
# we need to find out max number of vote for baner location
# record = [1, 'himanshu', 'baner', 10, 2, 'akshay', 'kothrud', 20, 3, 'ashutosh', 'baner', 30, 4, 'sai', 'warje', 50]

# length of a records in 4
def cal_max_vote(arr, record_length):
    i, j = (0, record_length - 1)
    loc_i = 2
    max_vote = 0
    while j < len(arr):
        if arr[loc_i] == 'baner':
            max_vote = max(max_vote, arr[j])
        i = j + 1
        j = i + (record_length - 1)
        loc_i = i + 2
    return max_vote


arr = [1, 'himanshu', 'baner', 10, 2, 'akshay', 'kothrud', 20, 3, 'ashutosh', 'baner', 30, 4, 'sai', 'warje', 50]
print(cal_max_vote(arr, 4))

# 0  (3 - 0 + 1)
# 3
