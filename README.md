# DataCleanse AI - Python Data Pipeline

DataCleanse AI is a lightweight Python automation script that streamlines dataset cleaning routines by automatically handling missing entries, removing duplicate records, and standardizing text formatting.

## Features
- **Duplicate Removal:** Identifies and drops identical rows seamlessly.
- **Smart Imputation:** Fills numeric missing fields with column medians and categorical fields with modal values.
- **String Normalization:** Strips irregular leading and trailing whitespace from text inputs.
- **Pipeline Logging:** Prints clear operational metrics and shape transformations directly to the console.

## Requirements
- Python 3.8+
- `pandas`
- `numpy`

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/agenticflow-tech/DataCleanse-AI.git
   pip install pandas numpy
   python datacleanse.py
   ```
