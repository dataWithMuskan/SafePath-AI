def accessibility_penalty(road):

    penalty = 0

    if road["stairs"]:
        penalty += 100

    if not road["ramp"]:
        penalty += 20

    if not road["sidewalk"]:
        penalty += 20

    return penalty


def safety_penalty(road):

    penalty = 0

    penalty += (
        100 - road["lighting"]
    ) * 0.4

    penalty += (
        road["isolation"]
    ) * 0.4

    penalty += (
        100 - road["public_activity"]
    ) * 0.2

    return penalty


def safety_score(road):

    penalty = safety_penalty(road)

    score = 100 - penalty

    return max(
        0,
        min(100, score)
    )


if __name__ == "__main__":

    test_road = {
        "stairs": False,
        "ramp": True,
        "sidewalk": True
    }

    print(
        "Accessibility penalty:",
        accessibility_penalty(test_road)
    )


    safety_road = {
        "lighting": 80,
        "isolation": 20,
        "public_activity": 80
    }

    print(
        "Safety penalty:",
        safety_penalty(safety_road)
    )

    print(
        "Safety score:",
        safety_score(safety_road)
    )