# =========================================================
# SafePath AI - Dijkstra
# =========================================================

import heapq

from algorithms.graph import GRAPH
from road_profiles import get_road_profile, adjusted_cost


def dijkstra(GRAPH, start, goal, mode="normal"):

    # ---------------------------------------------
    # DISTANCE
    # ---------------------------------------------

    distances = {
        node: float("inf")
        for node in GRAPH
    }

    previous = {
        node: None
        for node in GRAPH
    }

    distances[start] = 0

    priority_queue = [
        (0, start)
    ]

    explored = []

    visited = set()


    # ---------------------------------------------
    # SEARCH
    # ---------------------------------------------

    while priority_queue:

        current_cost, current = heapq.heappop(
            priority_queue
        )


        if current in visited:
            continue


        visited.add(current)

        explored.append(current)


        # -----------------------------------------
        # GOAL
        # -----------------------------------------

        if current == goal:
            break


        # -----------------------------------------
        # NEIGHBOURS
        # -----------------------------------------

        for neighbour, base_cost in GRAPH[
            current
        ].items():

            profile = get_road_profile(
                current,
                neighbour
            )


            # =====================================
            # WHEELCHAIR HARD BLOCK
            # =====================================

            if (
                mode == "wheelchair"
                and int(
                    profile.get("stairs", 0)
                ) == 1
            ):

                # NEVER enter this road
                continue


            new_cost = (
                current_cost
                +
                adjusted_cost(
                    base_cost,
                    profile,
                    mode
                )
            )


            # -------------------------------------
            # NORMAL RELAXATION
            # -------------------------------------

            if new_cost < distances[neighbour]:

                distances[neighbour] = new_cost

                previous[neighbour] = current

                heapq.heappush(
                    priority_queue,
                    (
                        new_cost,
                        neighbour
                    )
                )


    # ---------------------------------------------
    # NO ROUTE
    # ---------------------------------------------

    if distances[goal] == float("inf"):

        return {
            "path": [],
            "cost": None,
            "explored": explored
        }


    # ---------------------------------------------
    # BUILD PATH
    # ---------------------------------------------

    path = []

    current = goal


    while current is not None:

        path.append(current)

        current = previous[current]


    path.reverse()


    # ---------------------------------------------
    # FINAL SAFETY CHECK
    # ---------------------------------------------

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

                # This should NEVER happen
                return {
                    "path": [],
                    "cost": None,
                    "explored": explored
                }


    return {
        "path": path,
        "cost": distances[goal],
        "explored": explored
    }