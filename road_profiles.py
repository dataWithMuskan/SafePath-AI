# =========================================================
# SafePath AI - Road Profiles
# =========================================================

ROAD_PROFILES = {}


def add(a, b, lighting=4, crowd=4, cctv=0, stairs=0, ramp=1):
    ROAD_PROFILES[f"{a}-{b}"] = {
        "lighting": lighting,
        "crowd": crowd,
        "cctv": cctv,
        "stairs": stairs,
        "ramp": ramp
    }


# =========================================================
# NORMAL ROADS
# =========================================================

add("A", "B", lighting=5, crowd=5, cctv=1)
add("A", "D", lighting=3, crowd=2, cctv=0)

add("B", "C", lighting=5, crowd=5, cctv=1)
add("B", "E", lighting=4, crowd=4, cctv=1)

# STAIR
add("C", "F", lighting=4, crowd=4, cctv=0, stairs=1, ramp=0)

# CCTV / safe
add("C", "H", lighting=5, crowd=5, cctv=1)

add("D", "E", lighting=4, crowd=4, cctv=0)

# STAIR
add("D", "I", lighting=3, crowd=3, cctv=0, stairs=1, ramp=0)

add("E", "F", lighting=5, crowd=5, cctv=1)
add("E", "G", lighting=5, crowd=5, cctv=1)
add("E", "J", lighting=4, crowd=5, cctv=1)

add("F", "G", lighting=5, crowd=5, cctv=1)

# STAIR
add("F", "K", lighting=3, crowd=3, cctv=0, stairs=1, ramp=0)

add("G", "L", lighting=4, crowd=4, cctv=1)

add("H", "K", lighting=5, crowd=5, cctv=1)
add("H", "M", lighting=3, crowd=3, cctv=0)

add("I", "J", lighting=4, crowd=4, cctv=1)
add("I", "N", lighting=3, crowd=3, cctv=0)

add("J", "K", lighting=5, crowd=5, cctv=1)
add("J", "O", lighting=4, crowd=4, cctv=1)

# STAIR
add("K", "L", lighting=3, crowd=3, cctv=0, stairs=1, ramp=0)

add("K", "P", lighting=5, crowd=5, cctv=1)

add("L", "Q", lighting=4, crowd=4, cctv=1)

add("M", "N", lighting=4, crowd=4, cctv=0)
add("M", "R", lighting=4, crowd=4, cctv=1)

add("N", "O", lighting=4, crowd=4, cctv=1)
add("N", "S", lighting=3, crowd=3, cctv=0)

add("O", "P", lighting=5, crowd=5, cctv=1)
add("O", "T", lighting=5, crowd=5, cctv=1)

add("P", "Q", lighting=5, crowd=5, cctv=1)
add("P", "U", lighting=4, crowd=4, cctv=1)

add("Q", "V", lighting=4, crowd=4, cctv=1)

add("R", "S", lighting=4, crowd=4, cctv=1)

add("S", "T", lighting=5, crowd=5, cctv=1)

add("T", "U", lighting=5, crowd=5, cctv=1)

add("U", "V", lighting=4, crowd=4, cctv=1)


# =========================================================
# HELPERS
# =========================================================

def road_key(a, b):

    if f"{a}-{b}" in ROAD_PROFILES:
        return f"{a}-{b}"

    if f"{b}-{a}" in ROAD_PROFILES:
        return f"{b}-{a}"

    return None


def get_road_profile(a, b):

    key = road_key(a, b)

    if key is None:
        return {
            "lighting": 3,
            "crowd": 3,
            "cctv": 0,
            "stairs": 0,
            "ramp": 1
        }

    return ROAD_PROFILES[key]


# =========================================================
# RISK
# =========================================================

def risk_score(profile):

    score = 0

    if profile["lighting"] <= 2:
        score += 4

    elif profile["lighting"] <= 3:
        score += 2


    if profile["crowd"] <= 2:
        score += 4

    elif profile["crowd"] <= 3:
        score += 2


    if profile["cctv"] == 0:
        score += 2


    if profile["stairs"] == 1:
        score += 2


    return score


def risk_level(profile):

    score = risk_score(profile)

    if score >= 7:
        return "High"

    if score >= 4:
        return "Medium"

    return "Low"


# =========================================================
# COST
# =========================================================

def adjusted_cost(base_cost, profile, mode):

    # NORMAL
    if mode == "normal":
        return base_cost


    # =====================================================
    # WHEELCHAIR
    # STAIR = ABSOLUTELY BLOCKED
    # =====================================================

    if mode == "wheelchair":

        if int(profile.get("stairs", 0)) == 1:
            return float("inf")

        return base_cost


    # =====================================================
    # WOMEN SAFETY
    # CCTV + LIGHTING + CROWD PREFERRED
    # =====================================================

    if mode == "women":

        score = risk_score(profile)

        if profile["cctv"] == 1:
            score -= 2

        return base_cost + max(0, score) * 1.8


    return base_cost