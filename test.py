from algorithms.graph import GRAPH
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar


print("================================")
print("       SafePath AI Tests")
print("================================")


# Test 1: Graph
print("\nTest 1: Graph")
print("Nodes:", list(GRAPH.keys()))
print("Test 1 OK")


# Test 2: Dijkstra
print("\nTest 2: Dijkstra")

result = dijkstra(
    GRAPH,
    "A",
    "G",
    "normal"
)

print("Path:", " -> ".join(result["path"]))
print("Cost:", result["cost"])

if result["path"]:
    print("Test 2 OK")
else:
    print("Test 2 FAILED")


# Test 3: A*
print("\nTest 3: A*")

result = astar(
    GRAPH,
    "A",
    "G",
    "normal"
)

print("Path:", " -> ".join(result["path"]))
print("Cost:", result["cost"])

if result["path"]:
    print("Test 3 OK")
else:
    print("Test 3 FAILED")


# Test 4: Wheelchair
print("\nTest 4: Wheelchair")

result = dijkstra(
    GRAPH,
    "A",
    "G",
    "wheelchair"
)

print("Path:", " -> ".join(result["path"]))
print("Cost:", result["cost"])

if result["path"]:
    print("Test 4 OK")
else:
    print("Test 4 FAILED")


print("\n================================")
print("       All Tests Completed")
print("================================")