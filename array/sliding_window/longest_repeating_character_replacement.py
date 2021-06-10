from collections import defaultdict


def max_count(s, uniq_c, k):
    i, j = (0, 0)
    count = k
    max_repeated_count, repeated_count = (0, 0)
    while j < len(s):
        repeated_count += 1
        if s[j] != uniq_c:
            count -= 1

        if count >= 0:
            max_repeated_count = max(max_repeated_count, repeated_count)
        elif count < 0:
            # increment i and decrement ones_count by one
            # if we encounter 0 at any position then increase count
            while count < 0:
                repeated_count -= 1
                if s[i] != uniq_c:
                    count += 1
                i += 1
        j += 1
    return max_repeated_count


def longest_repeating_character_replacement(s, k):
    uniq_char = set()
    for x in s:
        uniq_char.add(x)
    max_number = 0
    for uniq_c in uniq_char:
        max_number = max(max_number, max_count(s, uniq_c, k))

    return max_number


s = 'ABCDE'
k = 2
# s = "ABBB"
# k = 2
# s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
# k = 4
print(longest_repeating_character_replacement(s, k))
