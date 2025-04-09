import joblib


model = joblib.load("model.pkl")

# Print the type of model (e.g., RandomForestClassifier, LogisticRegression, etc.)
print(" Model Type:", type(model))

# Model parameters
try:
    print("\nModel Parameters:")
    print(model.get_params())
except AttributeError:
    print("\n This model type does not support get_params().\n\n")

print(model)
