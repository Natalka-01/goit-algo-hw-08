import heapq

def min_total_cost(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        a = heapq.heappop(cables)
        b = heapq.heappop(cables)
        cost = a + b
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost

# Приклад:
cables = [5, 2, 4, 3]
print(min_total_cost(cables)) 