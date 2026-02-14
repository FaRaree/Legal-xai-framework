import os
import joblib
import pandas as pd
import shap
import streamlit as st

def confidence_and_limits(probability: float, threshold: float, input_row=None):
    """
    Returns (confidence_label, distance_from_threshold, completeness_ratio, review_recommendation)
    - probability: model predicted probability (0..1)
    - threshold: decision threshold (0..1)
    - input_row: optional pandas Series/dict of inputs for completeness check
    """
    # Confidence based on how far probability is from the threshold
    dist = abs(probability - threshold)

    if dist >= 0.25:
        confidence = "High"
        review = "Optional (routine human review recommended)"
    elif dist >= 0.10:
        confidence = "Moderate"
        review = "Recommended (human review advised)"
    else:
        confidence = "Low"
        review = "Required (prediction is near threshold)"

    # Data completeness (if we have the inputs)
    completeness_ratio = None
    if input_row is not None:
        try:
            # works for pandas Series
            total = len(input_row)
            missing = int(input_row.isna().sum())
            completeness_ratio = (total - missing) / max(total, 1)
        except Exception:
            # works for dict-like
            try:
                vals = list(input_row.values())
                total = len(vals)
                missing = sum(v is None for v in vals)
                completeness_ratio = (total - missing) / max(total, 1)
            except Exception:
                completeness_ratio = None

    return confidence, dist, completeness_ratio, review

st.set_page_config(page_title="Legal XAI Demo", layout="wide")

st.title("Legal-XAI-Framework Demo")
st.caption("SHAP explanations → Daubert-aligned narrative justification (research prototype)")

# Paths
MODEL_PATH = "data/recidivism_model.pkl"
DATA_PATH = "data/compas.csv"

FEATURES = ["age", "priors_count", "juv_fel_count", "juv_misd_count", "juv_other_count"]
TARGET = "two_year_recid"

st.sidebar.header("Input Factors (Example Case)")
age = st.sidebar.slider("Age", min_value=16, max_value=80, value=30)
priors_count = st.sidebar.slider("Prior convictions (count)", min_value=0, max_value=50, value=2)
juv_fel_count = st.sidebar.slider("Juvenile felony count", min_value=0, max_value=20, value=0)
juv_misd_count = st.sidebar.slider("Juvenile misdemeanor count", min_value=0, max_value=20, value=0)
juv_other_count = st.sidebar.slider("Other juvenile count", min_value=0, max_value=20, value=0)

input_row = pd.DataFrame([{
    "age": age,
    "priors_count": priors_count,
    "juv_fel_count": juv_fel_count,
    "juv_misd_count": juv_misd_count,
    "juv_other_count": juv_other_count
}])[FEATURES]

# Guardrails
if not os.path.exists(MODEL_PATH):
    st.error(
        "Model file not found: data/recidivism_model.pkl\n\n"
        "Run locally first:\n"
        "  python src/train_model.py\n"
    )
    st.stop()

model = joblib.load(MODEL_PATH)

# Load background data for SHAP if available
background_X = None
if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    # Ensure required columns exist
    missing = [c for c in FEATURES if c not in df.columns]
    if missing:
        st.warning(f"Dataset found, but missing columns: {missing}. SHAP may fail unless you align columns.")
    else:
        background_X = df[FEATURES].dropna()
else:
    st.warning(
        "Dataset not found: data/compas.csv\n\n"
        "SHAP needs background data. Add the dataset locally as described in data/README.md."
    )

# Prediction
proba = float(model.predict_proba(input_row)[:, 1][0])
pred = int(proba >= 0.5)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Prediction")
    st.metric("Predicted probability of recidivism (2 years)", f"{proba:.3f}")
    st.write("Predicted class (threshold 0.50):", "**Recidivism**" if pred == 1 else "**No recidivism**")
    st.subheader("Case Inputs")
    st.dataframe(input_row, use_container_width=True)

def narrative_from_shap(values, feature_names):
    # Rank by absolute magnitude
    pairs = sorted(zip(values, feature_names), key=lambda x: abs(x[0]), reverse=True)

    def bucket(v):
        av = abs(v)
        if av >= 0.40:
            return "primary"
        if av >= 0.15:
            return "moderate"
        return "minor"

    lines = []
    for v, f in pairs:
        direction = "increased" if v > 0 else "decreased"
        b = bucket(v)
        label = f.replace("_", " ")

        if b == "primary":
            lines.append(f"**Primary factor:** {label} {direction} the risk assessment.")
        elif b == "moderate":
            lines.append(f"**Moderate factor:** {label} {direction} the risk assessment.")
        else:
            lines.append(f"**Minor factor:** {label} had a limited effect and {direction} the risk assessment.")
    return lines

with col2:
    st.subheader("Narrative Justification (Prototype)")
    st.caption("This converts SHAP contributions into courtroom-friendly language (no raw weights shown).")

    if background_X is None or len(background_X) < 10:
        st.info("Add data/compas.csv locally to enable SHAP + narrative from real attributions.")
        st.stop()

    # SHAP
    explainer = shap.Explainer(model, background_X)
    shap_values = explainer(input_row)

    # For binary classification, shap_values.values may be shape (1, n_features) or (1, n_features, 2)
    vals = shap_values.values
    if vals.ndim == 3:
        # pick the positive class attributions
        vals = vals[:, :, 1]
    vals = vals[0]

    narrative_lines = narrative_from_shap(vals, FEATURES)
    for line in narrative_lines:
        st.write("-", line)

    st.subheader("Raw SHAP Output (Audit View)")
    st.caption("Shown for transparency/auditability (engineers / experts).")
    audit_df = pd.DataFrame({
        "feature": FEATURES,
        "shap_value": vals
    }).sort_values(by="shap_value", key=lambda s: s.abs(), ascending=False)
    st.dataframe(audit_df, use_container_width=True)
