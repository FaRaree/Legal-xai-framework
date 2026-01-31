# Experiment Protocol: Legal Comprehensibility of SHAP Explanations

## Study Title
Evaluating the Legal Comprehensibility of SHAP-based Explainable AI for Judicial Sentencing

## Objective
To measure whether SHAP feature attributions can be translated into narrative explanations that are more intelligible to legal audiences than raw numerical outputs.

This protocol focuses on the “Narrative Gap”:
- SHAP output: feature contributions (math)
- Court requirement: intelligible justification (legal reasoning)

---

## Dataset
**Primary dataset:** COMPAS (recidivism risk)  
**Storage:** `data/compas.csv`  
**Notes:** COMPAS is controversial and may embed bias; this study uses it strictly to evaluate transparency and explanation quality.

---

## Model (Baseline)
**Model type:** XGBoost classifier  
**Target label:** `two_year_recid`  
**Features (baseline):**
- age
- priors_count
- juv_fel_count
- juv_misd_count
- juv_other_count

**Training script:** `src/train_model.py`  
**Saved model:** `data/recidivism_model.pkl`

---

## Explainability Method
**Method:** SHAP (Shapley Additive Explanations)  
**Outputs:**
1) Global feature importance plot  
2) Local individual explanation plot  
**Script:** `src/explain.py`  
**Artifacts saved to:** `docs/`

---

## Narrative Layer (Key Contribution)
**Method:** Rule-based narrative translation (SHAP → legal justification)  
**Rules:** `docs/narrative_rules.md`  
**Script:** `src/narrative.py`

**Output format:** Short, structured explanation describing:
- Main factors
- Direction of influence (increase/decrease)
- Relative importance (primary/moderate/minor)
- Plain language suitable for adversarial questioning

---

## Evaluation Plan
This study compares two explanation styles:

### A) Raw SHAP output (baseline)
- Numerical contributions / plots only

### B) Narrative Justification (proposed)
- Rule-based written explanation derived from SHAP

---

## Metrics (Phase 1: Practical + Reproducible)
**Primary metric:** Human comprehension survey (legal audience proxy)
- Participants: law students, paralegals, or non-technical adults (pilot)
- Task: “Explain why the model predicted high/low risk”
- Score: clarity rating (1–5), confidence (1–5), and perceived fairness (1–5)

**Secondary metric:** Consistency audit
- Does the narrative accurately reflect the top SHAP features?
- Are the top 3 factors preserved? (Yes/No)

---

## Ethics & Risk Controls
- Do not deploy this system in real legal decisions.
- Document bias concerns explicitly.
- Avoid sensitive attributes unless required for bias auditing, and document any such use.

---

## Deliverables
1) Public GitHub repository with reproducible code
2) `docs/daubert_checklist.md` (legal admissibility mapping)
3) `docs/narrative_rules.md` (translation rules)
4) `docs/experiment_protocol.md` (this document)
5) Draft paper outline (8–12 pages target)

---

## Timeline (Suggested)
- **Feb:** Dataset integration + baseline model + SHAP
- **Mar:** Narrative rules + narrative generator
- **Apr:** Evaluation (human survey + consistency audit)
- **May:** White paper + polished repo + preprint upload
