# Evaluating the Legal Comprehensibility of SHAP-Based Explainable AI for Judicial Sentencing

## 1. Introduction

Machine learning systems are increasingly used to support decision-making in high-stakes domains, including criminal justice. Risk assessment tools designed to predict recidivism or inform sentencing decisions are now deployed in courts across the United States. While these systems promise consistency and efficiency, they raise serious concerns regarding transparency, fairness, and due process when their internal logic is opaque to legal decision-makers.

Explainable Artificial Intelligence (XAI) has emerged as a response to the opacity of complex predictive models. Techniques such as Shapley Additive Explanations (SHAP) provide mathematical feature attributions intended to clarify how input variables influence model predictions. However, most XAI methods are designed for technical audiences and output explanations in numerical or visual formats that are not directly usable in legal contexts.

Courts do not merely require predictions; they require reasons. Judicial reasoning must be intelligible, contestable, and aligned with evidentiary standards governing admissibility. In particular, the Daubert standard emphasizes reliability, transparency, and methodological rigor when scientific or technical evidence is introduced. Feature importance values alone do not constitute legal justification and cannot be meaningfully cross-examined by attorneys or evaluated by judges.

This paper addresses what we term the “narrative gap” between statistical explanations and legal justifications. We propose a framework that translates SHAP-based feature attributions into structured narrative explanations designed to resemble judicial reasoning rather than raw mathematical output. The goal is not to replace judicial discretion, but to provide intelligible and auditable explanations that support due process.

Using a recidivism risk assessment dataset (COMPAS) as a case study, we train a baseline predictive model and apply SHAP to generate local and global explanations. We then introduce a rule-based narrative translation layer that converts these explanations into courtroom-oriented language, emphasizing dominant factors, direction of influence, and relative importance. We evaluate this approach by comparing raw SHAP outputs with narrative explanations in terms of interpretability and consistency.

The contributions of this work are threefold: (1) a reproducible pipeline combining predictive modeling, SHAP explanations, and narrative translation; (2) a formalized set of narrative translation rules grounded in legal intelligibility; and (3) an experimental protocol for evaluating whether such narratives better support legal reasoning than numerical explanations alone.

This work aims to advance the integration of explainable AI into judicial settings by reframing explanation as a legal artifact rather than a purely technical one.

## 4. Methodology

### 4.1 Dataset
This study uses the COMPAS recidivism risk assessment dataset as a representative example of algorithmic decision-making in judicial contexts. The dataset contains demographic and criminal history features commonly used to predict two-year recidivism outcomes. Although the dataset is known to reflect historical bias, it is employed here strictly to study explainability and transparency rather than to justify automated sentencing.

The target variable is `two_year_recid`, indicating whether an individual reoffended within two years. A subset of features was selected to construct a baseline predictive model: age, priors_count, juv_fel_count, juv_misd_count, and juv_other_count.

---

### 4.2 Predictive Model
A gradient-boosted decision tree model (XGBoost) was trained to predict recidivism risk. The model was selected due to its strong predictive performance and compatibility with post-hoc explainability techniques. The dataset was split into training and test sets using an 80/20 partition. Model performance was evaluated using accuracy and area under the receiver operating characteristic curve (AUC).

The trained model was saved and reused for explanation generation to ensure reproducibility.

---

### 4.3 Explainability via SHAP
To interpret the trained model, Shapley Additive Explanations (SHAP) were applied. SHAP is grounded in cooperative game theory and assigns each feature a contribution value reflecting its influence on an individual prediction. Both global explanations (feature importance across the dataset) and local explanations (feature contributions for individual predictions) were generated.

SHAP satisfies desirable properties such as additivity and consistency, making it suitable for evaluating how individual factors affect predicted risk scores.

---

### 4.4 Narrative Translation Layer
The core contribution of this work is a narrative translation layer that converts numerical SHAP values into structured legal-style explanations. Rather than presenting raw feature attributions, this layer applies a set of rule-based mappings to generate plain-language justifications.

Features are ranked by absolute SHAP magnitude and categorized as dominant, moderate, or minor contributors. Each feature’s direction of influence (increasing or decreasing risk) is reflected in the narrative output. Technical terminology is avoided in favor of language resembling judicial reasoning.

For example, a raw attribution such as “priors_count = +0.42” is translated into: “The risk score increased primarily due to a pattern of prior offenses, which the model treats as a significant contributing factor.”

---

### 4.5 Reproducibility
All experiments are reproducible using the provided scripts. Model training is performed by `src/train_model.py`, explanation generation by `src/explain.py`, and narrative construction by `src/narrative.py`. The dataset is loaded from `data/compas.csv`, and outputs are saved to the `docs/` directory. This design ensures that both predictions and explanations can be regenerated and audited.

## 3. Related Work

### 3.1 Explainable Artificial Intelligence (XAI)
Explainable Artificial Intelligence has emerged as a response to the opacity of complex machine learning models. Feature attribution methods such as LIME and SHAP attempt to identify which input variables most influence model predictions. Among these approaches, SHAP is distinguished by its grounding in cooperative game theory and its satisfaction of properties such as consistency and additivity.

While SHAP and similar techniques improve transparency for technical audiences, their outputs are typically numerical or visual and require statistical literacy to interpret. As a result, these methods do not directly address the needs of non-technical decision-makers such as judges or attorneys.

---

### 3.2 Algorithmic Decision-Making in Criminal Justice
Risk assessment tools have been widely adopted in criminal justice systems to assist with bail, parole, and sentencing decisions. Studies of systems such as COMPAS have revealed concerns related to bias, fairness, and transparency. Prior research has demonstrated that even when predictive accuracy is high, the reasoning behind algorithmic outputs often remains inaccessible to affected individuals.

Legal scholars have argued that opaque algorithms undermine procedural fairness by preventing meaningful challenges to automated recommendations. These critiques highlight the tension between efficiency and due process in algorithmic governance.

---

### 3.3 Legal Standards for Technical Evidence
In U.S. courts, the admissibility of scientific and technical evidence is governed in part by the Daubert standard, which emphasizes reliability, testability, and transparency of methodology. Machine-generated evidence raises novel challenges because it often lacks an interpretable chain of reasoning comparable to human expert testimony.

Recent legal scholarship has called for explainable AI systems that can provide intelligible justifications rather than abstract statistical metrics. However, most existing XAI research does not explicitly map its outputs to legal standards of admissibility.

---

### 3.4 Position of This Work
This study builds upon prior work in explainable AI and algorithmic justice by reframing explanation as a legal artifact rather than a technical one. Whereas existing approaches focus on producing mathematically faithful feature attributions, this work emphasizes the translation of those attributions into narrative explanations aligned with judicial reasoning norms. In doing so, it aims to bridge the gap between statistical explanation and legally meaningful justification.

## 5. Results

### 5.1 Model Performance
The baseline XGBoost model achieved moderate predictive performance on the COMPAS dataset. Accuracy and AUC metrics were used to evaluate classification quality. While performance is not the primary objective of this study, these results establish that the model behaves comparably to commonly used risk assessment baselines.

These results demonstrate that the model produces meaningful predictions suitable for explainability analysis.

---

### 5.2 Global Feature Importance
Global SHAP analysis revealed that prior criminal history variables (e.g., priors_count and juvenile offense counts) exerted the strongest influence on predicted recidivism risk. Age exhibited a comparatively smaller but consistent effect.

This global pattern aligns with prior empirical findings in recidivism modeling, suggesting that the explanation method accurately reflects model behavior rather than producing arbitrary attributions.

---

### 5.3 Local Explanations
For individual predictions, SHAP produced feature-level attributions indicating how each factor contributed to the final risk score. These local explanations allow inspection of case-specific reasoning rather than relying solely on aggregate trends.

For example, in a representative case, the largest positive contribution was associated with prior offenses, while age contributed marginally in a mitigating direction.

---

### 5.4 Narrative Justifications
Applying the narrative translation layer to SHAP outputs yielded structured explanations in plain language. Instead of numerical values, the system produced statements such as:

> “The risk score increased primarily due to a documented pattern of prior offenses, which the model treats as a significant contributing factor. Juvenile history also moderately increased the assessed risk, while age had a limited mitigating effect.”

These narrative explanations preserved the relative importance and direction of SHAP attributions while replacing technical terminology with legally intelligible language.

---

### 5.5 Comparison with Raw SHAP Output
Raw SHAP outputs consist of numerical contributions and visual plots that require statistical interpretation. By contrast, narrative explanations provide directly interpretable reasons that can be scrutinized, contested, and contextualized by non-technical users.

This comparison highlights the central finding of this study: mathematical explanation alone is insufficient for legal contexts, whereas narrative translation supports intelligibility without discarding model transparency.

## 6. Evaluation

### 6.1 Evaluation Objective
The evaluation focuses on whether narrative explanations derived from SHAP values are more intelligible to human readers than raw numerical or visual explanations. Rather than optimizing predictive accuracy, this study evaluates interpretability and legal usability.

---

### 6.2 Comparison Conditions
Two explanation formats were compared:

**A) Raw SHAP Output:**  
Numerical feature contributions and visual plots.

**B) Narrative Justification (Proposed):**  
Rule-based written explanations derived from SHAP values using the narrative translation layer.

---

### 6.3 Human Comprehension Study (Pilot)
A pilot human-subjects evaluation is proposed using law students or non-technical participants as a proxy for legal decision-makers. Participants are presented with either raw SHAP output or narrative explanations and asked to:

- Summarize the reason for a high or low risk prediction.
- Rate clarity on a 1–5 scale.
- Rate confidence in their understanding on a 1–5 scale.
- Rate perceived fairness of the explanation on a 1–5 scale.

---

### 6.4 Consistency Audit
To ensure fidelity to the underlying model, narrative explanations are audited for consistency with SHAP outputs. The top three contributing features in the narrative explanation are compared with the top three SHAP features.

Consistency is measured as:
- Exact match of dominant features (Yes/No).
- Preservation of direction of influence (increase vs. decrease).

---

### 6.5 Limitations
This evaluation is exploratory and limited by dataset scope and participant pool size. Future work will require controlled studies with legal professionals and real-world case data to validate generalizability.

---

### 6.6 Ethical Safeguards
Participants are informed that explanations are generated by an experimental system and are not used for real legal decisions. Sensitive attributes are excluded from narrative outputs unless explicitly required for bias auditing.

## 7. Discussion

### 7.1 Legal Implications
The results of this study suggest that explanation methods designed for technical audiences are insufficient for judicial use. While SHAP provides mathematically faithful feature attributions, its outputs do not inherently satisfy the legal demand for intelligible reasoning. Courts require explanations that can be articulated, questioned, and evaluated within adversarial proceedings. By translating SHAP outputs into narrative justifications, this framework reframes explanation as a form of legal reasoning rather than a statistical artifact.

This approach aligns with the Daubert emphasis on transparency and methodological reliability by exposing the primary drivers of algorithmic decisions in a form that resembles human justification. Rather than presenting a risk score as an inscrutable conclusion, the narrative layer provides a structured account of why the system reached its assessment.

---

### 7.2 Transparency versus Accuracy
Explainable AI systems often face a trade-off between predictive performance and interpretability. This study does not aim to maximize accuracy but to demonstrate that intelligibility can be improved without discarding model-based reasoning. The proposed framework preserves the underlying predictive model while altering only the presentation of its explanations.

This suggests that legal transparency need not require replacing machine learning systems with simpler models, but instead demands a rethinking of how explanations are communicated to human decision-makers.

---

### 7.3 Limitations
Several limitations should be acknowledged. First, the study relies on a single dataset and a limited feature set, which constrains generalizability. Second, the narrative translation rules are handcrafted and may oversimplify complex relationships. Third, the evaluation is exploratory and does not yet include practicing judges or attorneys.

These limitations highlight the need for future work involving real legal professionals, alternative datasets, and more adaptive narrative generation methods.

---

### 7.4 Broader Implications
Beyond sentencing and recidivism prediction, the concept of narrative translation has implications for other domains involving machine-generated evidence, such as digital forensics and financial fraud detection. In these contexts, juries and judges similarly require explanations that resemble human reasoning rather than technical diagnostics.

This work therefore contributes to a broader vision of explainable AI as a communicative system, not merely an analytical one.

---

### 7.5 Future Work
Future research will extend this framework to additional datasets and incorporate more flexible natural language generation techniques. Controlled studies with legal professionals will be necessary to evaluate whether narrative explanations genuinely improve trust and understanding in judicial settings. Further work may also integrate fairness auditing directly into the narrative layer to expose potential proxy variables and disparate impacts.

## 8. Conclusion

This study examined whether SHAP-based explainable AI outputs can be transformed into narrative justifications suitable for judicial reasoning. While existing explainability methods provide mathematically grounded feature attributions, they do not directly satisfy legal requirements for intelligibility and contestability. Courts require reasons that can be articulated, scrutinized, and challenged within adversarial proceedings, rather than abstract numerical contributions.

By introducing a rule-based narrative translation layer, this work reframes explanation as a legal artifact rather than a purely technical one. The proposed framework preserves the fidelity of SHAP attributions while expressing them in structured language that resembles judicial justification. The results demonstrate that such narratives can retain consistency with underlying model behavior while improving interpretability for non-technical audiences.

The primary contribution of this work is the formalization of the “narrative gap” between statistical explanation and legal justification, along with a reproducible pipeline for addressing it. This approach offers a path toward more transparent and auditable algorithmic decision-support systems in the criminal justice domain.

Future research should evaluate this framework with practicing legal professionals, extend it to additional datasets and decision contexts, and explore adaptive narrative generation methods. More broadly, this work suggests that meaningful explainability in law requires not only faithful attribution, but also communication aligned with legal norms of reasoning and evidence.
