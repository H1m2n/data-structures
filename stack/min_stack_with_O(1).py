# Approach:
# we will have a variable where we store min
# and sometimes in stack we will store a flag(by using formula) if the current element is the next min element
# so basically the min element contains the actual element and flag is just anomaly

# formula for flag(anomaly) = 2 * x(push_e) - min
# formula for previously stored min = 2 * min - y(pop_e)
