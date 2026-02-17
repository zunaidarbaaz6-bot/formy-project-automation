"""
Prediction script for fertilizer recommendation
"""

import pandas as pd
import numpy as np
import joblib
import argparse
from data_preprocessing import DataPreprocessor


class FertilizerPredictor:
    """
    Make fertilizer predictions for new soil samples
    """
    
    def __init__(self, model_path='models/fertilizer_model.pkl',
                 preprocessor_path='models/preprocessor.pkl'):
        self.model = joblib.load(model_path)
        self.preprocessor = DataPreprocessor()
        self.preprocessor.load_preprocessor(preprocessor_path)
        print("Model and preprocessor loaded successfully!")
    
    def predict_single(self, nitrogen, phosphorus, potassium, temperature,
                      humidity, ph, rainfall, crop):
        """
        Predict fertilizer for a single sample
        """
        # Create input DataFrame
        input_data = pd.DataFrame({
            'Nitrogen': [nitrogen],
            'Phosphorus': [phosphorus],
            'Potassium': [potassium],
            'Temperature': [temperature],
            'Humidity': [humidity],
            'pH': [ph],
            'Rainfall': [rainfall],
            'Crop': [crop]
        })
        
        # Apply feature engineering
        input_enhanced = self.preprocessor.engineer_features(input_data)
        
        # Encode categorical variables
        input_encoded = self.preprocessor.encode_categorical(input_enhanced, fit=False)
        
        # Scale features
        input_scaled = self.preprocessor.scale_features(input_encoded, fit=False)
        
        # Make prediction
        prediction = self.model.predict(input_scaled)[0]
        prediction_proba = self.model.predict_proba(input_scaled)[0]
        
        # Decode prediction
        fertilizer = self.preprocessor.label_encoders['Fertilizer'].inverse_transform([prediction])[0]
        confidence = prediction_proba[prediction] * 100
        
        # Get all probabilities
        all_fertilizers = self.preprocessor.label_encoders['Fertilizer'].classes_
        recommendations = sorted(
            zip(all_fertilizers, prediction_proba * 100),
            key=lambda x: x[1],
            reverse=True
        )[:3]
        
        return fertilizer, confidence, recommendations
    
    def predict_batch(self, input_file, output_file='predictions.csv'):
        """
        Predict fertilizer for multiple samples from CSV
        """
        # Load input data
        df = pd.read_csv(input_file)
        
        # Apply preprocessing
        df_enhanced = self.preprocessor.engineer_features(df)
        df_encoded = self.preprocessor.encode_categorical(df_enhanced, fit=False)
        
        # Make predictions
        predictions = self.model.predict(df_encoded)
        prediction_proba = self.model.predict_proba(df_encoded)
        
        # Decode predictions
        fertilizers = self.preprocessor.label_encoders['Fertilizer'].inverse_transform(predictions)
        confidences = np.max(prediction_proba, axis=1) * 100
        
        # Add to DataFrame
        df['Recommended_Fertilizer'] = fertilizers
        df['Confidence'] = confidences
        
        # Save results
        df.to_csv(output_file, index=False)
        print(f"\nPredictions saved to {output_file}")
        
        return df
    
    def display_recommendation(self, nitrogen, phosphorus, potassium, temperature,
                             humidity, ph, rainfall, crop):
        """
        Display formatted recommendation
        """
        fertilizer, confidence, recommendations = self.predict_single(
            nitrogen, phosphorus, potassium, temperature,
            humidity, ph, rainfall, crop
        )
        
        print("\n" + "="*60)
        print("FERTILIZER RECOMMENDATION")
        print("="*60)
        print("\nSoil Parameters:")
        print(f"  Nitrogen (N):   {nitrogen} kg/ha")
        print(f"  Phosphorus (P): {phosphorus} kg/ha")
        print(f"  Potassium (K):  {potassium} kg/ha")
        print(f"  pH Level:       {ph}")
        print("\nEnvironmental Conditions:")
        print(f"  Temperature:    {temperature}°C")
        print(f"  Humidity:       {humidity}%")
        print(f"  Rainfall:       {rainfall} mm")
        print(f"\nCrop Type: {crop}")
        print("\n" + "-"*60)
        print(f"RECOMMENDED FERTILIZER: {fertilizer}")
        print(f"Confidence: {confidence:.2f}%")
        print("-"*60)
        
        print("\nTop 3 Recommendations:")
        for i, (fert, prob) in enumerate(recommendations, 1):
            print(f"  {i}. {fert}: {prob:.2f}%")
        
        print("\n" + "="*60)
        
        # Provide additional guidance
        self._provide_guidance(nitrogen, phosphorus, potassium, ph)
    
    def _provide_guidance(self, nitrogen, phosphorus, potassium, ph):
        """
        Provide additional agricultural guidance
        """
        print("\nAdditional Guidance:")
        
        if nitrogen < 40:
            print("  • Nitrogen deficiency detected. Consider split application.")
        elif nitrogen > 100:
            print("  • High nitrogen levels. Monitor for excess vegetative growth.")
        
        if phosphorus < 20:
            print("  • Low phosphorus. Important for root development.")
        
        if potassium < 20:
            print("  • Potassium deficiency may affect disease resistance.")
        
        if ph < 5.5:
            print("  • Soil is acidic. Consider liming to adjust pH.")
        elif ph > 7.5:
            print("  • Soil is alkaline. May affect nutrient availability.")
        
        print("\nNote: Always consult with local agricultural experts for")
        print("      site-specific recommendations.")
        print("="*60 + "\n")


def main():
    """
    Command-line interface for predictions
    """
    parser = argparse.ArgumentParser(description='Fertilizer Recommendation Predictor')
    
    parser.add_argument('--nitrogen', type=float, help='Nitrogen content (kg/ha)')
    parser.add_argument('--phosphorus', type=float, help='Phosphorus content (kg/ha)')
    parser.add_argument('--potassium', type=float, help='Potassium content (kg/ha)')
    parser.add_argument('--temperature', type=float, help='Temperature (°C)')
    parser.add_argument('--humidity', type=float, help='Humidity (%)')
    parser.add_argument('--ph', type=float, help='pH level')
    parser.add_argument('--rainfall', type=float, help='Rainfall (mm)')
    parser.add_argument('--crop', type=str, help='Crop type')
    parser.add_argument('--batch', type=str, help='Input CSV file for batch prediction')
    parser.add_argument('--output', type=str, default='predictions.csv',
                       help='Output file for batch predictions')
    
    args = parser.parse_args()
    
    # Initialize predictor
    predictor = FertilizerPredictor()
    
    if args.batch:
        # Batch prediction
        print(f"Processing batch predictions from {args.batch}...")
        predictor.predict_batch(args.batch, args.output)
    elif all([args.nitrogen, args.phosphorus, args.potassium, args.temperature,
              args.humidity, args.ph, args.rainfall, args.crop]):
        # Single prediction
        predictor.display_recommendation(
            args.nitrogen, args.phosphorus, args.potassium,
            args.temperature, args.humidity, args.ph,
            args.rainfall, args.crop
        )
    else:
        # Interactive mode - Example predictions
        print("="*60)
        print("FERTILIZER RECOMMENDATION SYSTEM - DEMO MODE")
        print("="*60)
        print("\nExample Prediction 1: Rice Farm")
        predictor.display_recommendation(
            nitrogen=90, phosphorus=42, potassium=43,
            temperature=20.8, humidity=82, ph=6.5,
            rainfall=202.9, crop='Rice'
        )
        
        print("\nExample Prediction 2: Wheat Farm")
        predictor.display_recommendation(
            nitrogen=75, phosphorus=38, potassium=36,
            temperature=18.5, humidity=65, ph=6.8,
            rainfall=150.0, crop='Wheat'
        )
        
        print("\nTo make custom predictions, use command-line arguments:")
        print("python predict.py --nitrogen 90 --phosphorus 42 --potassium 43 \\")
        print("                  --temperature 20.8 --humidity 82 --ph 6.5 \\")
        print("                  --rainfall 202.9 --crop Rice")


if __name__ == "__main__":
    main()
