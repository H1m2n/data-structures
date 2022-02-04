import heapq

import heapq

# -----------> 3rd largest number
l = [7, 10, 4, 3, 20, 15, -10]
k = 2
min_heap = []
heapq.heapify(min_heap)
for x in l:
    heapq.heappush(min_heap, x)
    if len(min_heap) > k:
        heapq.heappop(min_heap)

print(f"{k} largest number " + str(min_heap[0]))

# -----------> 3rd smallest number
# tweaks -> python don't provide facility of Max Heap, so we can do workaround by changing the sign of the element
# present in the array and then we can use Min Heap
modified_l = list(map(lambda x: -x, l))
max_heap = []
heapq.heapify(max_heap)
for x in modified_l:
    heapq.heappush(max_heap, x)
    if len(max_heap) > k:
        heapq.heappop(max_heap)
print(f"{k} smallest number " + str(-max_heap[0]))

# -----------> sort K sorted array (element that should present at any index, can be found in K range(left/right side in array))
