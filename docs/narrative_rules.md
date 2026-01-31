# Narrative Translation Rules (SHAP → Legal Justification)

This document defines how numerical SHAP feature contributions are converted into narrative explanations suitable for judicial reasoning.

The goal is to transform statistical attributions into statements that satisfy legal intelligibility and procedural transparency.

---

## Rule 1: Dominant Feature Identification

If a feature contributes more than 40% of the total SHAP magnitude:

**Narrative Output:**  
> "This decision is primarily influenced by the defendant’s prior criminal history."

---

## Rule 2: Moderate Feature Influence

If a feature contributes between 15% and 40%:

**Narrative Output:**  
> "This factor moderately increased the assessed risk due to its historical correlation with recidivism."

---

## Rule 3: Minor Feature Influence

If a feature contributes less than 15%:

**Narrative Output:**  
> "This factor had a limited effect on the overall assessment."

---

## Rule 4: Direction of Influence

If SHAP value is positive:

**Narrative Output:**  
> "This factor increased the risk score."

If SHAP value is negative:

**Narrative Output:**  
> "This factor reduced the risk score."

---

## Rule 5: Aggregated Explanation

Narrative explanations should be structured as:

> Base Risk + (Major Factors) + (Minor Factors) = Final Risk Assessment

Example:

> "The risk score is elevated primarily due to multiple prior offenses, with additional influence from juvenile history. Age contributed minimally to the final assessment."

---

## Rule 6: Procedural Transparency

Each narrative explanation must:
- Identify the most influential features,
- Describe their direction (increase/decrease),
- Avoid technical jargon (e.g., “SHAP value = 0.42”),
- Permit adversarial questioning.

---

## Legal Objective

These rules ensure that AI explanations:
- Are intelligible to judges and attorneys,
- Can be challenged in court,
- Disclose reasoning rather than hide it,
- Support due process protections.

---

## Research Contribution

This rule-based narrative layer represents a novel interface between:
- Cooperative game theory (SHAP),
- And legal standards of justification.

It formalizes explanation as a legal artifact, not merely a statistical output.
