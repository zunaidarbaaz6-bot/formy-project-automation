#!/bin/bash

# Fertilizer Recommendation System - Quick Start Script
# This script runs the complete pipeline

echo "=========================================="
echo "FERTILIZER RECOMMENDATION SYSTEM"
echo "Complete Pipeline Execution"
echo "=========================================="
echo ""

# Step 1: Generate Dataset
echo "[1/5] Generating synthetic dataset..."
python src/generate_dataset.py
if [ $? -eq 0 ]; then
    echo "✓ Dataset generated successfully"
else
    echo "✗ Dataset generation failed"
    exit 1
fi
echo ""

# Step 2: Preprocess Data
echo "[2/5] Preprocessing data and engineering features..."
python src/data_preprocessing.py
if [ $? -eq 0 ]; then
    echo "✓ Data preprocessing completed"
else
    echo "✗ Data preprocessing failed"
    exit 1
fi
echo ""

# Step 3: Train Model
echo "[3/5] Training Random Forest model..."
python src/train_model.py
if [ $? -eq 0 ]; then
    echo "✓ Model training completed"
else
    echo "✗ Model training failed"
    exit 1
fi
echo ""

# Step 4: Generate Visualizations
echo "[4/5] Creating data visualizations..."
python src/visualize_data.py
if [ $? -eq 0 ]; then
    echo "✓ Visualizations generated"
else
    echo "✗ Visualization generation failed"
    exit 1
fi
echo ""

# Step 5: Run Example Predictions
echo "[5/5] Running example predictions..."
python src/predict.py
if [ $? -eq 0 ]; then
    echo "✓ Predictions completed"
else
    echo "✗ Prediction failed"
    exit 1
fi
echo ""

echo "=========================================="
echo "PIPELINE COMPLETED SUCCESSFULLY!"
echo "=========================================="
echo ""
echo "Results:"
echo "  • Trained model: models/fertilizer_model.pkl"
echo "  • Visualizations: reports/figures/"
echo "  • Performance report: reports/model_performance.txt"
echo ""
echo "To make custom predictions:"
echo "  python src/predict.py --nitrogen 90 --phosphorus 42 \\"
echo "                        --potassium 43 --temperature 20.8 \\"
echo "                        --humidity 82 --ph 6.5 \\"
echo "                        --rainfall 202.9 --crop Rice"
echo ""
