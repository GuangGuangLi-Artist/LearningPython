#coding=utf-8

#图
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# print(graph)
graph["a"] = {}
graph["a"]["fin"] = 1

# print(graph)

graph["b"] = {}
graph["b"]["fin"] = 5
graph["b"]["a"] = 3

graph["fin"] = {}
# print(graph)

# 创建开销的代码
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
# print(costs)

#创建父节点
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = "None"
# print(parents)

# 记录处理过的节点

processed = []

# 最低开销节点函数

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not  in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# print(find_lowest_cost_node(costs))
node = find_lowest_cost_node(costs)
while node is not  None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(processed)