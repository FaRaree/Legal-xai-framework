import pandas as pd
import shap
import joblib

# Load trained model
model = joblib.load("data/recidivism_model.pkl")

# Load dataset
DATA_PATH = "data/compas.csv"
df = pd.read_csv(DATA_PATH)

# Same features used in training
features = [
    "age",
    "priors_count",
    "juv_fel_count",
    "juv_misd_count",
    "juv_other_count"
]

X = df[features].dropna()

# Create SHAP explainer
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

def shap_to_narrative(shap_row, feature_names):
    """
    Convert SHAP values into a courtroom-style narrative explanation.
    """
    explanations = []
    for value, feature in sorted(zip(shap_row.values, feature_names), key=lambda x: abs(x[0]), reverse=True):
        if value > 0:
            explanations.append(
                f"The risk score increased primarily due to the individual's {feature.replace('_', ' ')}, "
                f"which the model weighs as a significant contributing factor."
            )
        elif value < 0:
            explanations.append(
                f"The risk score decreased in part because of the individual's {feature.replace('_', ' ')}, "
                f"which the model treats as a mitigating factor."
            )
    return explanations

# Generate narrative for the first individual in the dataset
narrative_explanation = shap_to_narrative(shap_values[0], features)

print("Narrative Explanation:\n")
for sentence in narrative_explanation:
    print("-", sentence)
