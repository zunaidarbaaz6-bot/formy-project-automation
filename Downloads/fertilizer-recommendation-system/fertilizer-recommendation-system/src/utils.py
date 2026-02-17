"""
Utility functions for fertilizer recommendation system
"""

import pandas as pd
import numpy as np
import joblib


def load_model_and_preprocessor(model_path='models/fertilizer_model.pkl',
                               preprocessor_path='models/preprocessor.pkl'):
    """
    Load trained model and preprocessor
    
    Returns:
        tuple: (model, preprocessor)
    """
    model = joblib.load(model_path)
    preprocessor = joblib.load(preprocessor_path)
    return model, preprocessor


def validate_input(nitrogen, phosphorus, potassium, temperature, 
                  humidity, ph, rainfall):
    """
    Validate input parameters
    
    Args:
        nitrogen: Nitrogen content (0-140 kg/ha)
        phosphorus: Phosphorus content (5-145 kg/ha)
        potassium: Potassium content (5-205 kg/ha)
        temperature: Temperature (10-43°C)
        humidity: Humidity (20-100%)
        ph: pH level (3-10)
        rainfall: Rainfall (50-300 mm)
    
    Returns:
        tuple: (is_valid, error_message)
    """
    errors = []
    
    if not (0 <= nitrogen <= 140):
        errors.append(f"Nitrogen must be between 0-140 kg/ha (got {nitrogen})")
    
    if not (5 <= phosphorus <= 145):
        errors.append(f"Phosphorus must be between 5-145 kg/ha (got {phosphorus})")
    
    if not (5 <= potassium <= 205):
        errors.append(f"Potassium must be between 5-205 kg/ha (got {potassium})")
    
    if not (10 <= temperature <= 43):
        errors.append(f"Temperature must be between 10-43°C (got {temperature})")
    
    if not (20 <= humidity <= 100):
        errors.append(f"Humidity must be between 20-100% (got {humidity})")
    
    if not (3 <= ph <= 10):
        errors.append(f"pH must be between 3-10 (got {ph})")
    
    if not (50 <= rainfall <= 300):
        errors.append(f"Rainfall must be between 50-300 mm (got {rainfall})")
    
    if errors:
        return False, "\n".join(errors)
    
    return True, ""


def get_nutrient_status(nitrogen, phosphorus, potassium):
    """
    Determine nutrient status (deficient, adequate, excess)
    
    Returns:
        dict: Status for each nutrient
    """
    status = {}
    
    # Nitrogen status
    if nitrogen < 40:
        status['Nitrogen'] = 'Deficient'
    elif nitrogen > 100:
        status['Nitrogen'] = 'Excess'
    else:
        status['Nitrogen'] = 'Adequate'
    
    # Phosphorus status
    if phosphorus < 20:
        status['Phosphorus'] = 'Deficient'
    elif phosphorus > 80:
        status['Phosphorus'] = 'Excess'
    else:
        status['Phosphorus'] = 'Adequate'
    
    # Potassium status
    if potassium < 20:
        status['Potassium'] = 'Deficient'
    elif potassium > 100:
        status['Potassium'] = 'Excess'
    else:
        status['Potassium'] = 'Adequate'
    
    return status


def get_ph_category(ph):
    """
    Categorize pH level
    
    Returns:
        str: pH category
    """
    if ph < 5.5:
        return 'Strongly Acidic'
    elif ph < 6.5:
        return 'Slightly Acidic'
    elif ph <= 7.5:
        return 'Neutral'
    elif ph <= 8.5:
        return 'Slightly Alkaline'
    else:
        return 'Strongly Alkaline'


def calculate_npk_ratios(nitrogen, phosphorus, potassium):
    """
    Calculate NPK ratios
    
    Returns:
        dict: Various NPK ratios
    """
    ratios = {
        'N:P': round(nitrogen / (phosphorus + 1), 2),
        'N:K': round(nitrogen / (potassium + 1), 2),
        'P:K': round(phosphorus / (potassium + 1), 2),
        'Total_NPK': round(nitrogen + phosphorus + potassium, 2)
    }
    
    return ratios


def generate_recommendations_text(nitrogen, phosphorus, potassium, 
                                 ph, fertilizer, confidence):
    """
    Generate text-based recommendations
    
    Returns:
        str: Recommendation text
    """
    recommendations = []
    
    # Fertilizer recommendation
    recommendations.append(f"Recommended Fertilizer: {fertilizer} (Confidence: {confidence:.1f}%)")
    recommendations.append("")
    
    # Nutrient-specific recommendations
    nutrient_status = get_nutrient_status(nitrogen, phosphorus, potassium)
    
    if nutrient_status['Nitrogen'] == 'Deficient':
        recommendations.append("• Apply nitrogen-rich fertilizer (e.g., Urea)")
        recommendations.append("  Consider split application for better efficiency")
    elif nutrient_status['Nitrogen'] == 'Excess':
        recommendations.append("• High nitrogen detected - reduce nitrogen application")
        recommendations.append("  Monitor for excessive vegetative growth")
    
    if nutrient_status['Phosphorus'] == 'Deficient':
        recommendations.append("• Phosphorus supplementation needed")
        recommendations.append("  Important for root development and flowering")
    
    if nutrient_status['Potassium'] == 'Deficient':
        recommendations.append("• Potassium deficiency detected")
        recommendations.append("  Critical for disease resistance and water regulation")
    
    # pH recommendations
    ph_category = get_ph_category(ph)
    if ph < 5.5:
        recommendations.append(f"• Soil is {ph_category} (pH: {ph})")
        recommendations.append("  Consider liming to raise pH to 6.0-7.0 range")
    elif ph > 7.5:
        recommendations.append(f"• Soil is {ph_category} (pH: {ph})")
        recommendations.append("  May need sulfur or organic matter to lower pH")
    
    return "\n".join(recommendations)


def format_soil_report(nitrogen, phosphorus, potassium, temperature,
                      humidity, ph, rainfall, crop):
    """
    Format comprehensive soil report
    
    Returns:
        str: Formatted report
    """
    report = []
    report.append("="*60)
    report.append("SOIL ANALYSIS REPORT")
    report.append("="*60)
    report.append("")
    
    report.append("SOIL NUTRIENT ANALYSIS:")
    report.append(f"  Nitrogen (N):      {nitrogen:>6.2f} kg/ha")
    report.append(f"  Phosphorus (P):    {phosphorus:>6.2f} kg/ha")
    report.append(f"  Potassium (K):     {potassium:>6.2f} kg/ha")
    report.append(f"  pH Level:          {ph:>6.2f}")
    report.append("")
    
    report.append("ENVIRONMENTAL CONDITIONS:")
    report.append(f"  Temperature:       {temperature:>6.2f}°C")
    report.append(f"  Humidity:          {humidity:>6.2f}%")
    report.append(f"  Rainfall:          {rainfall:>6.2f} mm")
    report.append("")
    
    report.append(f"CROP TYPE: {crop}")
    report.append("")
    
    # NPK Ratios
    ratios = calculate_npk_ratios(nitrogen, phosphorus, potassium)
    report.append("NPK RATIOS:")
    for key, value in ratios.items():
        report.append(f"  {key:>15}: {value:.2f}")
    report.append("")
    
    # Nutrient Status
    status = get_nutrient_status(nitrogen, phosphorus, potassium)
    report.append("NUTRIENT STATUS:")
    for nutrient, stat in status.items():
        report.append(f"  {nutrient:>15}: {stat}")
    report.append("")
    
    # pH Category
    ph_cat = get_ph_category(ph)
    report.append(f"pH CATEGORY: {ph_cat}")
    report.append("")
    
    report.append("="*60)
    
    return "\n".join(report)


def save_prediction_log(input_data, prediction, confidence, filepath='prediction_log.csv'):
    """
    Log predictions to CSV file
    
    Args:
        input_data: dict of input parameters
        prediction: predicted fertilizer
        confidence: prediction confidence
        filepath: path to log file
    """
    from datetime import datetime
    
    log_entry = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        **input_data,
        'predicted_fertilizer': prediction,
        'confidence': confidence
    }
    
    # Create DataFrame
    log_df = pd.DataFrame([log_entry])
    
    # Append to existing file or create new
    try:
        existing_log = pd.read_csv(filepath)
        log_df = pd.concat([existing_log, log_df], ignore_index=True)
    except FileNotFoundError:
        pass
    
    log_df.to_csv(filepath, index=False)


def print_model_info(model):
    """
    Print model information
    """
    print("\nModel Information:")
    print(f"  Type: {type(model).__name__}")
    
    if hasattr(model, 'n_estimators'):
        print(f"  Number of Estimators: {model.n_estimators}")
    
    if hasattr(model, 'max_depth'):
        print(f"  Max Depth: {model.max_depth}")
    
    if hasattr(model, 'n_features_in_'):
        print(f"  Number of Features: {model.n_features_in_}")
    
    if hasattr(model, 'classes_'):
        print(f"  Number of Classes: {len(model.classes_)}")
        print(f"  Classes: {', '.join(map(str, model.classes_))}")


if __name__ == "__main__":
    # Example usage
    print("Utility Functions Module")
    print("="*60)
    
    # Test validation
    is_valid, message = validate_input(90, 42, 43, 20.8, 82, 6.5, 202.9)
    print(f"\nValidation Test: {'Passed' if is_valid else 'Failed'}")
    if not is_valid:
        print(message)
    
    # Test nutrient status
    status = get_nutrient_status(90, 42, 43)
    print("\nNutrient Status:")
    for nutrient, stat in status.items():
        print(f"  {nutrient}: {stat}")
    
    # Test pH category
    ph_cat = get_ph_category(6.5)
    print(f"\npH Category: {ph_cat}")
    
    # Test NPK ratios
    ratios = calculate_npk_ratios(90, 42, 43)
    print("\nNPK Ratios:")
    for key, value in ratios.items():
        print(f"  {key}: {value}")
