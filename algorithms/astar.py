# =========================================================
# SafePath AI - A*
# =========================================================

import heapq
import math

from algorithms.graph import GRAPH
from road_profiles import get_road_profile, adjusted_cost


# =========================================================
# COORDINATES
# =========================================================

COORDINATES = {

    "A": (70, 220),
    "B": (180, 160),
    "C": (300, 140),
    "D": (180, 310),

    "E": (360, 250),
    "F": (480, 150),
    "G": (600, 220),

    "H": (430, 70),
    "I": (300, 380),
    "J": (450, 320),

    "K": (560, 300),
    "L": (700, 150),

    "M": (570, 430),
    "N": (680, 380),
    "O": (700, 300),

    "P": (790, 300),
    "Q": (820, 190),

    "R": (700, 480),
    "S": (800, 430),
    "T": (880, 370),

    "U": (880, 500),
    "V": (790, 560)
}


# =========================================================
# HEURISTIC
# =========================================================

def heuristic(node, goal):

    x1, y1 = COORDINATES[node]

    x2, y2 = COORDINATES[goal]

    return math.sqrt(
        (x1 - x2) ** 2
        +
        (y1 - y2) ** 2
    ) / 100


# =========================================================
# A*
# =========================================================

def astar(GRAPH, start, goal, mode="normal"):

    g_score = {
        node: float("inf")
        for node in GRAPH
    }

    f_score = {
        node: float("inf")
        for node in GRAPH
    }

    previous = {
        node: None
        for node in GRAPH
    }


    g_score[start] = 0

    f_score[start] = heuristic(
        start,
        goal
    )


    queue = [
        (
            f_score[start],
            start
        )
    ]


    explored = []

    visited = set()


    # =====================================================
    # SEARCH
    # =====================================================

    while queue:

        current_f, current = heapq.heappop(
            queue
        )


        if current in visited:
            continue


        visited.add(current)

        explored.append(current)


        # -------------------------------------------------
        # GOAL
        # -------------------------------------------------

        if current == goal:
            break


        # -------------------------------------------------
        # NEIGHBOURS
        # -------------------------------------------------

        for neighbour, base_cost in GRAPH[
            current
        ].items():

            profile = get_road_profile(
                current,
                neighbour
            )


            # =============================================
            # WHEELCHAIR HARD BLOCK
            # =============================================

            if (
                mode == "wheelchair"
                and int(
                    profile.get("stairs", 0)
                ) == 1
            ):

                # NEVER put stair road in A* queue
                continue


            road_cost = adjusted_cost(
                base_cost,
                profile,
                mode
            )


            if math.isinf(road_cost):
                continue


            tentative_g = (
                g_score[current]
                +
                road_cost
            )


            if tentative_g < g_score[neighbour]:

                previous[neighbour] = current

                g_score[neighbour] = tentative_g

                f_score[neighbour] = (
                    tentative_g
                    +
                    heuristic(
                        neighbour,
                        goal
                    )
                )


                heapq.heappush(
                    queue,
                    (
                        f_score[neighbour],
                        neighbour
                    )
                )


    # =====================================================
    # NO ROUTE
    # =====================================================

    if g_score[goal] == float("inf"):

        return {
            "path": [],
            "cost": None,
            "explored": explored
        }


    # =====================================================
    # BUILD PATH
    # =====================================================

    path = []

    current = goal


    while current is not None:

        path.append(current)

        current = previous[current]


    path.reverse()


    # =====================================================
    # FINAL WHEELCHAIR VALIDATION
    # =====================================================

    if mode == "wheelchair":

        for i in range(len(path) - 1):

            a = path[i]

            b = path[i + 1]

            profile = get_road_profile(
                a,
                b
            )


            if int(
                profile.get("stairs", 0)
            ) == 1:

                return {
                    "path": [],
                    "cost": None,
                    "explored": explored
                }


    return {
        "path": path,
        "cost": g_score[goal],
        "explored": explored
    }