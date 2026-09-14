from classifier import train_classifier, predict_risk


# Train classifier
model, accuracy = train_classifier()


print("================================")
print("       SafePath AI Classifier")
print("================================")

print("Test Accuracy:", round(accuracy * 100, 2), "%")


print("\nRoad 1:")

risk = predict_risk(
    model,
    lighting=90,
    isolation=15,
    public_activity=85,
    stairs=0,
    ramp=1,
    sidewalk=1
)

print("Predicted Risk:", risk)


print("\nRoad 2:")

risk = predict_risk(
    model,
    lighting=30,
    isolation=80,
    public_activity=25,
    stairs=1,
    ramp=0,
    sidewalk=0
)

print("Predicted Risk:", risk)