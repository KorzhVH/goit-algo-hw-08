import heapq


def merge_cables(cable_list):
    # Note. If number of cables is even, then minimal cost = sum of all len(cables).
    # If uneven, we have to find max(cable_list) and remove it, as merging it will be costlier, then any other cable.
    # Thus, we don't, and it will set it's merge price to 0.
    # The order in even list doesn't matter. It's a sum of all, after all.
    if len(cable_list) % 2 == 1:
        cable_list.remove(max(cable_list))
    for cable in cable_list:
        if cable <= 0:
            return print("One of the cables is of negative or 0 length")
    heapq.heapify(cable_list)
    total_sum = 0
    while cable_list:
        cable1 = heapq.heappop(cable_list)
        cable2 = heapq.heappop(cable_list)
        total_sum += (cable1 + cable2)
    return total_sum


list1 = [12, 11, 13, 5, 6, 7]
list2 = [12, 11, 13, 5, 123123, 6, 7]

print(merge_cables(list1))
print(merge_cables(list2))
