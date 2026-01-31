# Dataset Setup (COMPAS)

Save your COMPAS dataset file in this folder as:

data/compas.csv

## Required Columns
The scripts assume the dataset includes:

- age  
- priors_count  
- juv_fel_count  
- juv_misd_count  
- juv_other_count  
- two_year_recid  

If your dataset uses different column names, update them in:
- src/train_model.py  
- src/explain.py  
- src/narrative.py  

## Run Order
After placing `compas.csv` in this folder, run:

python src/train_model.py  
python src/explain.py  
python src/narrative.py  

## Ethics Note
This dataset may reflect historical bias. It is used here strictly for research on transparency, auditability, and due process — not for real sentencing decisions.
