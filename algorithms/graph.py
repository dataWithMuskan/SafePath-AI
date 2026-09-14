# SafePath AI - 22 Node Road Network (A to V)

GRAPH = {
    "A": {"B": 4, "D": 7},
    "B": {"A": 4, "C": 3, "E": 2},
    "C": {"B": 3, "F": 4, "H": 5},
    "D": {"A": 7, "E": 3, "I": 4},

    "E": {"B": 2, "D": 3, "F": 3, "G": 5, "J": 4},
    "F": {"C": 4, "E": 3, "G": 3, "K": 4},
    "G": {"E": 5, "F": 3, "L": 4},

    "H": {"C": 5, "K": 3, "M": 4},
    "I": {"D": 4, "J": 3, "N": 5},
    "J": {"E": 4, "I": 3, "K": 3, "O": 4},

    "K": {"F": 4, "H": 3, "J": 3, "L": 2, "P": 4},
    "L": {"G": 4, "K": 2, "Q": 3},

    "M": {"H": 4, "N": 3, "R": 5},
    "N": {"I": 5, "M": 3, "O": 3, "S": 4},
    "O": {"J": 4, "N": 3, "P": 3, "T": 5},

    "P": {"K": 4, "O": 3, "Q": 2, "U": 4},
    "Q": {"L": 3, "P": 2, "V": 4},

    "R": {"M": 5, "S": 3},
    "S": {"N": 4, "R": 3, "T": 3},
    "T": {"O": 5, "S": 3, "U": 2},

    "U": {"P": 4, "T": 2, "V": 3},
    "V": {"Q": 4, "U": 3},
}


LOCATION_NAMES = {
    "A": "Main Gate",
    "B": "Library",
    "C": "School",
    "D": "Parking",
    "E": "Campus",
    "F": "Hospital",
    "G": "Mall",
    "H": "Metro Station",
    "I": "Bus Stop",
    "J": "Cafeteria",
    "K": "Admin Block",
    "L": "Auditorium",
    "M": "Playground",
    "N": "Hostel",
    "O": "Sports Complex",
    "P": "Main Road",
    "Q": "Market",
    "R": "Pharmacy",
    "S": "ATM",
    "T": "Police Help Desk",
    "U": "Garden",
    "V": "Parking 2",
}