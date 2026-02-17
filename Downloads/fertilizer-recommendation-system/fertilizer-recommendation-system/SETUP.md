# Setup and Execution Guide

This guide will help you set up and run the Fertilizer Recommendation System.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fertilizer-recommendation-system.git
cd fertilizer-recommendation-system
```

### 2. Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

### Step 1: Generate Dataset

```bash
python src/generate_dataset.py
```

This creates a synthetic agricultural dataset in `data/raw/fertilizer_data.csv`

### Step 2: Preprocess Data

```bash
python src/data_preprocessing.py
```

This performs:
- Data cleaning
- Feature engineering (NPK ratios, pH categories, etc.)
- Data encoding and scaling
- Saves processed data to `data/processed/`

### Step 3: Train Model

```bash
python src/train_model.py
```

This:
- Trains Random Forest classifier
- Evaluates model performance
- Generates confusion matrix and feature importance plots
- Saves trained model to `models/`

Expected output:
- Accuracy: ~98-99%
- Model file: `models/fertilizer_model.pkl`
- Visualizations in `reports/figures/`

### Step 4: Generate Visualizations

```bash
python src/visualize_data.py
```

Creates comprehensive visualizations:
- Nutrient distributions
- Correlation heatmaps
- Fertilizer distributions
- Crop analysis
- Environmental factors
- NPK relationships

### Step 5: Make Predictions

**Interactive Demo Mode:**
```bash
python src/predict.py
```

**Single Prediction:**
```bash
python src/predict.py --nitrogen 90 --phosphorus 42 --potassium 43 \
                      --temperature 20.8 --humidity 82 --ph 6.5 \
                      --rainfall 202.9 --crop Rice
```

**Batch Predictions:**
```bash
python src/predict.py --batch input_data.csv --output predictions.csv
```

## Project Structure After Setup

```
fertilizer-recommendation-system/
│
├── data/
│   ├── raw/
│   │   └── fertilizer_data.csv          # Generated dataset
│   └── processed/
│       └── processed_data.csv           # Processed dataset
│
├── models/
│   ├── fertilizer_model.pkl             # Trained ML model
│   └── preprocessor.pkl                 # Preprocessor objects
│
├── reports/
│   ├── figures/                         # Visualizations
│   │   ├── confusion_matrix.png
│   │   ├── feature_importance.png
│   │   ├── nutrient_distribution.png
│   │   └── ... (more plots)
│   └── model_performance.txt            # Performance metrics
│
└── ... (source code and configs)
```

## Jupyter Notebook

To run the exploratory analysis notebook:

```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

## Troubleshooting

### Issue: Module not found error

**Solution:** Make sure you're in the project root directory and virtual environment is activated.

```bash
# Check current directory
pwd

# Activate virtual environment if not already active
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### Issue: Permission denied when running scripts

**Solution:** On macOS/Linux, make scripts executable:

```bash
chmod +x src/*.py
```

### Issue: Matplotlib display issues

**Solution:** If plots don't display:

```python
# Add this at the beginning of scripts
import matplotlib
matplotlib.use('Agg')  # For non-GUI backend
```

## Running Tests

To verify installation:

```bash
python src/utils.py
```

This runs utility function tests.

## Next Steps

1. **Customize the Dataset**: Modify `src/generate_dataset.py` to change parameters
2. **Tune Hyperparameters**: Edit `src/train_model.py` to experiment with model settings
3. **Add New Features**: Extend `src/data_preprocessing.py` with domain knowledge
4. **Deploy**: Consider Flask/FastAPI for creating a web API

## Common Workflows

### Complete Pipeline (All Steps)

```bash
# Generate, process, train, visualize, and predict
python src/generate_dataset.py && \
python src/data_preprocessing.py && \
python src/train_model.py && \
python src/visualize_data.py && \
python src/predict.py
```

### Re-train Model Only

```bash
# If you've made changes to training code
python src/train_model.py
```

### Generate New Predictions

```bash
# After model is trained
python src/predict.py --nitrogen 85 --phosphorus 45 --potassium 40 \
                      --temperature 22 --humidity 75 --ph 6.8 \
                      --rainfall 180 --crop Maize
```

## Performance Optimization

For large datasets:

1. **Use Parallel Processing:**
   - Model training uses `n_jobs=-1` by default
   
2. **Reduce Dataset Size:**
   - Modify `n_samples` in `generate_dataset.py`

3. **Feature Selection:**
   - Use feature importance plots to identify top features
   - Reduce dimensionality if needed

## Support

For issues or questions:
1. Check the documentation in README.md
2. Review example outputs in `reports/`
3. Open an issue on GitHub

## Additional Resources

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas User Guide](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/)
