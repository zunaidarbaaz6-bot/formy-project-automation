@echo off
REM Fertilizer Recommendation System - Quick Start Script for Windows
REM This script runs the complete pipeline

echo ==========================================
echo FERTILIZER RECOMMENDATION SYSTEM
echo Complete Pipeline Execution
echo ==========================================
echo.

REM Step 1: Generate Dataset
echo [1/5] Generating synthetic dataset...
python src\generate_dataset.py
if %errorlevel% neq 0 (
    echo X Dataset generation failed
    exit /b 1
)
echo √ Dataset generated successfully
echo.

REM Step 2: Preprocess Data
echo [2/5] Preprocessing data and engineering features...
python src\data_preprocessing.py
if %errorlevel% neq 0 (
    echo X Data preprocessing failed
    exit /b 1
)
echo √ Data preprocessing completed
echo.

REM Step 3: Train Model
echo [3/5] Training Random Forest model...
python src\train_model.py
if %errorlevel% neq 0 (
    echo X Model training failed
    exit /b 1
)
echo √ Model training completed
echo.

REM Step 4: Generate Visualizations
echo [4/5] Creating data visualizations...
python src\visualize_data.py
if %errorlevel% neq 0 (
    echo X Visualization generation failed
    exit /b 1
)
echo √ Visualizations generated
echo.

REM Step 5: Run Example Predictions
echo [5/5] Running example predictions...
python src\predict.py
if %errorlevel% neq 0 (
    echo X Prediction failed
    exit /b 1
)
echo √ Predictions completed
echo.

echo ==========================================
echo PIPELINE COMPLETED SUCCESSFULLY!
echo ==========================================
echo.
echo Results:
echo   • Trained model: models\fertilizer_model.pkl
echo   • Visualizations: reports\figures\
echo   • Performance report: reports\model_performance.txt
echo.
echo To make custom predictions:
echo   python src\predict.py --nitrogen 90 --phosphorus 42 ^
echo                         --potassium 43 --temperature 20.8 ^
echo                         --humidity 82 --ph 6.5 ^
echo                         --rainfall 202.9 --crop Rice
echo.

pause
