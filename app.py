from flask import Flask, jsonify, send_from_directory

from algorithms.graph import GRAPH, LOCATION_NAMES
from algorithms.dijkstra import dijkstra
from algorithms.astar import astar
from road_profiles import get_road_profile, risk_score, risk_level


app = Flask(
    __name__,
    static_folder="frontend",
    static_url_path=""
)


# ------------------------------------------------
# ROUTE INFORMATION
# ------------------------------------------------

def route_risks(path):

    result = []

    if not path or len(path) < 2:
        return result

    for a, b in zip(path, path[1:]):

        profile = get_road_profile(a, b)

        result.append({
            "road": f"{a}-{b}",
            "risk": risk_level(profile),
            "score": risk_score(profile),
            "stairs": profile["stairs"],
            "ramp": profile["ramp"],
            "cctv": profile["cctv"],
            "lighting": profile["lighting"],
            "crowd": profile["crowd"]
        })

    return result


# ------------------------------------------------
# SHORTEST PATH
# ------------------------------------------------

def shortest_path(start, goal, mode):

    return dijkstra(
        GRAPH,
        start,
        goal,
        mode
    )


# ------------------------------------------------
# SAFEST PATH
# ------------------------------------------------

def safest_path(start, goal, mode):

    import heapq

    pq = [(0, 0, start)]

    best = {
        node: (float("inf"), float("inf"))
        for node in GRAPH
    }

    previous = {}

    best[start] = (0, 0)

    while pq:

        risk_cost, distance, current = heapq.heappop(pq)

        if (risk_cost, distance) != best[current]:
            continue

        if current == goal:
            break

        for neighbor, base_cost in GRAPH[current].items():

            profile = get_road_profile(
                current,
                neighbor
            )

            if mode == "wheelchair" and profile["stairs"] == 1:
                continue

            road_risk = risk_score(profile)

            # CCTV advantage
            if mode == "women" and profile["cctv"] == 1:
                road_risk = max(0, road_risk - 2)

            new_risk = risk_cost + road_risk
            new_distance = distance + base_cost

            candidate = (
                new_risk,
                new_distance
            )

            if candidate < best[neighbor]:

                best[neighbor] = candidate

                previous[neighbor] = current

                heapq.heappush(
                    pq,
                    (
                        new_risk,
                        new_distance,
                        neighbor
                    )
                )

    if best[goal][0] == float("inf"):
        return {
            "path": [],
            "cost": None
        }

    path = []

    current = goal

    while current != start:

        path.append(current)

        if current not in previous:
            return {
                "path": [],
                "cost": None
            }

        current = previous[current]

    path.append(start)

    path.reverse()

    return {
        "path": path,
        "cost": round(best[goal][1], 2),
        "risk": best[goal][0]
    }


# ------------------------------------------------
# LONGEST SIMPLE PATH
# ------------------------------------------------

def longest_path(start, goal, mode):

    best_path = []
    best_cost = -1

    visited = set()

    def dfs(current, path, cost):

        nonlocal best_path, best_cost

        if current == goal:

            if cost > best_cost:

                best_cost = cost
                best_path = path.copy()

            return

        # Safety guard
        if len(path) >= len(GRAPH):
            return

        for neighbor, base_cost in GRAPH[current].items():

            if neighbor in visited:
                continue

            profile = get_road_profile(
                current,
                neighbor
            )

            if mode == "wheelchair" and profile["stairs"] == 1:
                continue

            visited.add(neighbor)

            dfs(
                neighbor,
                path + [neighbor],
                cost + base_cost
            )

            visited.remove(neighbor)

    visited.add(start)

    dfs(
        start,
        [start],
        0
    )

    return {
        "path": best_path,
        "cost": (
            round(best_cost, 2)
            if best_cost >= 0
            else None
        )
    }


# ------------------------------------------------
# RESULTS API
# ------------------------------------------------

@app.route("/results")
def results():

    start = request_arg("start", "A")
    goal = request_arg("goal", "V")
    mode = request_arg("mode", "normal")

    if start not in GRAPH:
        start = "A"

    if goal not in GRAPH:
        goal = "V"

    if start == goal:

        same = {
            "path": [start],
            "cost": 0,
            "explored": [start]
        }

        return jsonify({
            "start": start,
            "goal": goal,
            "mode": mode,

            "dijkstra": same,
            "astar": same,

            "shortest": {
                "path": [start],
                "cost": 0
            },

            "safest": {
                "path": [start],
                "cost": 0,
                "risk": 0
            },

            "longest": {
                "path": [start],
                "cost": 0
            },

            "route_risks": [],
            "shortest_risks": [],
            "astar_risks": [],

            "start_name": LOCATION_NAMES[start],
            "goal_name": LOCATION_NAMES[goal]
        })

    d = dijkstra(
        GRAPH,
        start,
        goal,
        mode
    )

    a = astar(
        GRAPH,
        start,
        goal,
        mode
    )

    shortest = shortest_path(
        start,
        goal,
        mode
    )

    safe = safest_path(
        start,
        goal,
        mode
    )

    longest = longest_path(
        start,
        goal,
        mode
    )

    return jsonify({

        "start": start,
        "goal": goal,
        "mode": mode,

        "start_name": LOCATION_NAMES[start],
        "goal_name": LOCATION_NAMES[goal],

        "dijkstra": d,
        "astar": a,

        "shortest": shortest,

        "safest": safe,

        "longest": longest,

        "route_risks": route_risks(
            d["path"]
        ),

        "shortest_risks": route_risks(
            shortest["path"]
        ),

        "astar_risks": route_risks(
            a["path"]
        )
    })


def request_arg(name, default):

    from flask import request

    value = request.args.get(
        name,
        default
    )

    return value.strip()


# ------------------------------------------------
# FRONTEND
# ------------------------------------------------

@app.route("/")
def home():

    return send_from_directory(
        "frontend",
        "index.html"
    )


@app.route("/<path:path>")
def static_files(path):

    return send_from_directory(
        "frontend",
        path
    )


if __name__ == "__main__":

    print("")
    print("=" * 55)
    print(" SafePath AI is running")
    print(" http://127.0.0.1:5000")
    print("=" * 55)
    print("")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )