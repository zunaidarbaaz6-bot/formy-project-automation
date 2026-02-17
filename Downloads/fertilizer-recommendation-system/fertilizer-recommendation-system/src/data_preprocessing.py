"""
Data preprocessing and feature engineering for fertilizer recommendation
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

class DataPreprocessor:
    """
    Handles data cleaning, feature engineering, and preprocessing
    """
    
    def __init__(self):
        self.label_encoders = {}
        self.scaler = StandardScaler()
        
    def load_data(self, filepath):
        """Load dataset from CSV file"""
        df = pd.read_csv(filepath)
        print(f"Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    
    def check_missing_values(self, df):
        """Check for missing values"""
        missing = df.isnull().sum()
        if missing.sum() > 0:
            print("\nMissing values found:")
            print(missing[missing > 0])
        else:
            print("\nNo missing values found")
        return missing
    
    def engineer_features(self, df):
        """
        Create new features from existing data
        """
        df = df.copy()
        
        # NPK Ratios
        df['N_P_ratio'] = df['Nitrogen'] / (df['Phosphorus'] + 1)
        df['N_K_ratio'] = df['Nitrogen'] / (df['Potassium'] + 1)
        df['P_K_ratio'] = df['Phosphorus'] / (df['Potassium'] + 1)
        
        # Total NPK
        df['Total_NPK'] = df['Nitrogen'] + df['Phosphorus'] + df['Potassium']
        
        # Temperature-Humidity Index
        df['Temp_Humidity_Index'] = df['Temperature'] * df['Humidity'] / 100
        
        # pH Categories
        df['pH_acidic'] = (df['pH'] < 6.5).astype(int)
        df['pH_neutral'] = ((df['pH'] >= 6.5) & (df['pH'] <= 7.5)).astype(int)
        df['pH_alkaline'] = (df['pH'] > 7.5).astype(int)
        
        # Nutrient Deficiency Flags
        df['N_deficient'] = (df['Nitrogen'] < 40).astype(int)
        df['P_deficient'] = (df['Phosphorus'] < 20).astype(int)
        df['K_deficient'] = (df['Potassium'] < 20).astype(int)
        
        # Rainfall categories
        df['Low_Rainfall'] = (df['Rainfall'] < 100).astype(int)
        df['High_Rainfall'] = (df['Rainfall'] > 200).astype(int)
        
        print(f"\nFeature engineering complete. New shape: {df.shape}")
        print(f"New features added: {df.shape[1] - 9}")
        
        return df
    
    def encode_categorical(self, df, fit=True):
        """
        Encode categorical variables
        """
        df = df.copy()
        categorical_cols = df.select_dtypes(include=['object']).columns
        
        for col in categorical_cols:
            if col != 'Fertilizer':  # Don't encode target variable yet
                if fit:
                    self.label_encoders[col] = LabelEncoder()
                    df[col] = self.label_encoders[col].fit_transform(df[col])
                else:
                    df[col] = self.label_encoders[col].transform(df[col])
        
        return df
    
    def scale_features(self, X, fit=True):
        """
        Scale numerical features
        """
        if fit:
            X_scaled = self.scaler.fit_transform(X)
        else:
            X_scaled = self.scaler.transform(X)
        
        return X_scaled
    
    def prepare_data(self, df, target_col='Fertilizer'):
        """
        Complete preprocessing pipeline
        """
        # Separate features and target
        X = df.drop(target_col, axis=1)
        y = df[target_col]
        
        # Encode target variable
        if target_col not in self.label_encoders:
            self.label_encoders[target_col] = LabelEncoder()
            y = self.label_encoders[target_col].fit_transform(y)
        else:
            y = self.label_encoders[target_col].transform(y)
        
        return X, y
    
    def save_preprocessor(self, filepath='models/preprocessor.pkl'):
        """Save preprocessor objects"""
        joblib.dump({
            'label_encoders': self.label_encoders,
            'scaler': self.scaler
        }, filepath)
        print(f"\nPreprocessor saved to {filepath}")
    
    def load_preprocessor(self, filepath='models/preprocessor.pkl'):
        """Load preprocessor objects"""
        objects = joblib.load(filepath)
        self.label_encoders = objects['label_encoders']
        self.scaler = objects['scaler']
        print(f"\nPreprocessor loaded from {filepath}")


def main():
    """
    Main preprocessing pipeline
    """
    preprocessor = DataPreprocessor()
    
    # Load data
    df = preprocessor.load_data('data/raw/fertilizer_data.csv')
    
    # Check data quality
    print("\nDataset Info:")
    print(df.info())
    print("\nStatistical Summary:")
    print(df.describe())
    
    # Check missing values
    preprocessor.check_missing_values(df)
    
    # Feature engineering
    df_enhanced = preprocessor.engineer_features(df)
    
    # Encode categorical variables
    df_encoded = preprocessor.encode_categorical(df_enhanced, fit=True)
    
    # Prepare X and y
    X, y = preprocessor.prepare_data(df_encoded)
    
    # Scale features
    X_scaled = preprocessor.scale_features(X, fit=True)
    
    # Save processed data
    processed_df = pd.DataFrame(X_scaled, columns=X.columns)
    processed_df['Fertilizer'] = y
    processed_df.to_csv('data/processed/processed_data.csv', index=False)
    
    # Save preprocessor
    preprocessor.save_preprocessor()
    
    print("\n" + "="*50)
    print("Data preprocessing completed successfully!")
    print("="*50)
    print(f"Processed data saved to: data/processed/processed_data.csv")
    print(f"Final dataset shape: {processed_df.shape}")


if __name__ == "__main__":
    main()
