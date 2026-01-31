# Evaluating the Legal Comprehensibility of SHAP-Based Explainable AI for Judicial Sentencing

## 1. Introduction

Machine learning systems are increasingly used to support decision-making in high-stakes domains, including criminal justice. Risk assessment tools designed to predict recidivism or inform sentencing decisions are now deployed in courts across the United States. While these systems promise consistency and efficiency, they raise serious concerns regarding transparency, fairness, and due process when their internal logic is opaque to legal decision-makers.

Explainable Artificial Intelligence (XAI) has emerged as a response to the opacity of complex predictive models. Techniques such as Shapley Additive Explanations (SHAP) provide mathematical feature attributions intended to clarify how input variables influence model predictions. However, most XAI methods are designed for technical audiences and output explanations in numerical or visual formats that are not directly usable in legal contexts.

Courts do not merely require predictions; they require reasons. Judicial reasoning must be intelligible, contestable, and aligned with evidentiary standards governing admissibility. In particular, the Daubert standard emphasizes reliability, transparency, and methodological rigor when scientific or technical evidence is introduced. Feature importance values alone do not constitute legal justification and cannot be meaningfully cross-examined by attorneys or evaluated by judges.

This paper addresses what we term the “narrative gap” between statistical explanations and legal justifications. We propose a framework that translates SHAP-based feature attributions into structured narrative explanations designed to resemble judicial reasoning rather than raw mathematical output. The goal is not to replace judicial discretion, but to provide intelligible and auditable explanations that support due process.

Using a recidivism risk assessment dataset (COMPAS) as a case study, we train a baseline predictive model and apply SHAP to generate local and global explanations. We then introduce a rule-based narrative translation layer that converts these explanations into courtroom-oriented language, emphasizing dominant factors, direction of influence, and relative importance. We evaluate this approach by comparing raw SHAP outputs with narrative explanations in terms of interpretability and consistency.

The contributions of this work are threefold: (1) a reproducible pipeline combining predictive modeling, SHAP explanations, and narrative translation; (2) a formalized set of narrative translation rules grounded in legal intelligibility; and (3) an experimental protocol for evaluating whether such narratives better support legal reasoning than numerical explanations alone.

This work aims to advance the integration of explainable AI into judicial settings by reframing explanation as a legal artifact rather than a purely technical one.
