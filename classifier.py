# ==========================================
# SafePath AI - Risk Classifier
# ==========================================

import pandas as pd

from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_score
)

from sklearn.tree import DecisionTreeClassifier


# ==========================================
# FEATURES
# ==========================================

FEATURES = [
    "lighting",
    "isolation",
    "public_activity",
    "stairs",
    "ramp",
    "sidewalk"
]


# ==========================================
# TRAIN CLASSIFIER
# ==========================================

def train_classifier():

    data = pd.read_csv("data/road_data.csv")

    X = data[FEATURES]
    y = data["risk"]

    cv = StratifiedKFold(
        n_splits=4,
        shuffle=True,
        random_state=42
    )

    model = DecisionTreeClassifier(
        max_depth=4,
        random_state=42
    )

    scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="accuracy"
    )

    accuracy = scores.mean()

    # Train final model
    model.fit(X, y)

    return model, accuracy


# ==========================================
# PREDICT RISK
# ==========================================

def predict_risk(
    model,
    lighting,
    isolation,
    public_activity,
    stairs,
    ramp,
    sidewalk
):

    sample = pd.DataFrame(
        [[
            lighting,
            isolation,
            public_activity,
            stairs,
            ramp,
            sidewalk
        ]],
        columns=FEATURES
    )

    prediction = model.predict(sample)

    return prediction[0]


# ==========================================
# CREATE MODEL
# ==========================================

MODEL, MODEL_ACCURACY = train_classifier()