import heapq


def merge_cables(cable_list):
    uneven_check = False
    longest_cable = 0
    if len(cable_list) % 2 == 1:
        uneven_check = True
        longest_cable = max(cable_list)
        cable_list.remove(longest_cable)
    for cable in cable_list:
        if cable <= 0:
            return print("One of the cables is of negative or 0 length")
    heapq.heapify(cable_list)
    total_sum = 0
    while cable_list:
        cable1 = heapq.heappop(cable_list)
        cable2 = heapq.heappop(cable_list)
        total_sum += (cable1 + cable2)
    if uneven_check:
        total_sum += longest_cable
    return total_sum


list1 = [12, 11, 13, 5, 6, 7]
list2 = [12, 11, 13, 5, 123123, 6, 7]

print(merge_cables(list1))
print(merge_cables(list2))
