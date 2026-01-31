import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score
from xgboost import XGBClassifier
import joblib

# Load dataset
DATA_PATH = "data/compas.csv"  # you will add this later

df = pd.read_csv(DATA_PATH)

# Select features (simple baseline)
features = [
    "age",
    "priors_count",
    "juv_fel_count",
    "juv_misd_count",
    "juv_other_count"
]

target = "two_year_recid"

df = df[features + [target]].dropna()

X = df[features]
y = df[target]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = XGBClassifier(
    n_estimators=100,
    max_depth=3,
    learning_rate=0.1,
    eval_metric="logloss"
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

auc = roc_auc_score(y_test, y_prob)
acc = accuracy_score(y_test, y_pred)

print(f"AUC: {auc:.3f}")
print(f"Accuracy: {acc:.3f}")

# Save model
joblib.dump(model, "data/recidivism_model.pkl")

print("Model saved to data/recidivism_model.pkl")
