import pandas as pd
import shap
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load("data/recidivism_model.pkl")

# Load dataset
DATA_PATH = "data/compas.csv"
df = pd.read_csv(DATA_PATH)

# Use same features as training
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

# Global feature importance plot
shap.summary_plot(shap_values, X, show=False)
plt.savefig("docs/global_feature_importance.png", bbox_inches="tight")

print("Saved global feature importance plot to docs/global_feature_importance.png")

# Local explanation for first individual
shap.plots.waterfall(shap_values[0], show=False)
plt.savefig("docs/local_explanation_example.png", bbox_inches="tight")

print("Saved local explanation plot to docs/local_explanation_example.png")
