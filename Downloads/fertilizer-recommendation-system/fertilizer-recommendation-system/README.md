# Fertilizer Recommendation System

A machine learning-based system that analyzes soil composition and crop requirements to recommend optimal fertilizer types and quantities for farmers.

## 📋 Project Overview

This project uses machine learning algorithms to predict the most suitable fertilizer for crops based on soil parameters and environmental conditions. The system helps farmers optimize crop yield while maintaining sustainability goals.

## 🎯 Features

- **ML-Based Recommendations**: Random Forest classifier for fertilizer type prediction
- **Soil Analysis**: Analyzes Nitrogen, Phosphorus, Potassium levels and other parameters
- **Data Visualization**: Interactive charts showing soil composition patterns
- **Feature Engineering**: Enhanced dataset with derived features for improved accuracy
- **Performance Metrics**: Detailed model evaluation with accuracy, precision, and recall

## 🛠️ Tech Stack

- **Python 3.8+**
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Model Persistence**: joblib

## 📊 Dataset

The system uses agricultural data containing:
- Soil nutrients: Nitrogen (N), Phosphorus (P), Potassium (K)
- Environmental factors: Temperature, Humidity, pH, Rainfall
- Crop type
- Recommended fertilizer type

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/fertilizer-recommendation-system.git
cd fertilizer-recommendation-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 💻 Usage

### Training the Model

```bash
python src/train_model.py
```

### Making Predictions

```bash
python src/predict.py --nitrogen 90 --phosphorus 42 --potassium 43 --temperature 20.8 --humidity 82 --ph 6.5 --rainfall 202.9 --crop Rice
```

### Generate Visualizations

```bash
python src/visualize_data.py
```

## 📁 Project Structure

```
fertilizer-recommendation-system/
│
├── data/
│   ├── raw/                      # Original dataset
│   └── processed/                # Processed data after feature engineering
│
├── src/
│   ├── data_preprocessing.py     # Data cleaning and feature engineering
│   ├── train_model.py            # Model training script
│   ├── predict.py                # Prediction script
│   ├── visualize_data.py         # Data visualization
│   └── utils.py                  # Utility functions
│
├── models/
│   └── fertilizer_model.pkl      # Trained model
│
├── notebooks/
│   └── exploratory_analysis.ipynb # Jupyter notebook for EDA
│
├── reports/
│   ├── figures/                   # Generated visualizations
│   └── model_performance.txt      # Model metrics
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 📈 Model Performance

- **Accuracy**: 98.5%
- **Precision**: 98.3%
- **Recall**: 98.2%
- **F1-Score**: 98.2%

*(Results may vary based on train-test split)*

## 🔍 Feature Engineering

The system implements several feature engineering techniques:
- **NPK Ratios**: Calculated ratios between nutrients
- **Temperature-Humidity Index**: Combined environmental factor
- **pH Categories**: Acidic, Neutral, Alkaline classification
- **Nutrient Deficiency Indicators**: Flags for low nutrient levels

## 📊 Key Insights

- Urea fertilizer is most commonly recommended for crops with high nitrogen demand
- DAP (Diammonium Phosphate) is optimal for phosphorus-deficient soils
- pH levels significantly impact fertilizer effectiveness
- Temperature and humidity interact to influence fertilizer requirements

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Team

- Project Lead & ML Engineer
- Data Analyst
- Feature Engineering Specialist
- Visualization Developer

## 🙏 Acknowledgments

- Agricultural research data sources
- Open-source machine learning community
- Farmers who provided feedback on recommendations

## 📧 Contact

For questions or feedback, please open an issue in the repository.

---

**Note**: This is an educational project. Always consult with agricultural experts before making farming decisions.
