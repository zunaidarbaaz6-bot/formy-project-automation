"""
Generate synthetic fertilizer recommendation dataset
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Define fertilizer types
fertilizers = ['Urea', 'DAP', 'MOP', '10-26-26', '14-35-14', '17-17-17', '20-20', '28-28']

# Generate 1200 samples
n_samples = 1200

# Define crop types and their typical requirements
crops = {
    'Rice': {'N': (80, 100), 'P': (40, 50), 'K': (40, 50), 'pH': (5.5, 7.0)},
    'Wheat': {'N': (70, 90), 'P': (30, 45), 'K': (30, 45), 'pH': (6.0, 7.5)},
    'Maize': {'N': (60, 80), 'P': (35, 50), 'K': (35, 50), 'pH': (5.8, 7.5)},
    'Cotton': {'N': (50, 70), 'P': (20, 35), 'K': (40, 60), 'pH': (5.5, 7.0)},
    'Sugarcane': {'N': (80, 120), 'P': (40, 60), 'K': (50, 80), 'pH': (6.0, 7.5)},
    'Tobacco': {'N': (40, 60), 'P': (25, 40), 'K': (45, 65), 'pH': (5.5, 6.5)},
}

data = []

for _ in range(n_samples):
    crop = np.random.choice(list(crops.keys()))
    crop_req = crops[crop]
    
    # Generate soil parameters based on crop requirements with some variation
    nitrogen = np.random.normal(crop_req['N'][0] + (crop_req['N'][1] - crop_req['N'][0])/2, 15)
    phosphorus = np.random.normal(crop_req['P'][0] + (crop_req['P'][1] - crop_req['P'][0])/2, 10)
    potassium = np.random.normal(crop_req['K'][0] + (crop_req['K'][1] - crop_req['K'][0])/2, 10)
    
    # Clip values to reasonable ranges
    nitrogen = np.clip(nitrogen, 0, 140)
    phosphorus = np.clip(phosphorus, 5, 145)
    potassium = np.clip(potassium, 5, 205)
    
    # Environmental factors
    temperature = np.random.uniform(10, 43)
    humidity = np.random.uniform(20, 100)
    ph = np.random.uniform(crop_req['pH'][0], crop_req['pH'][1])
    rainfall = np.random.uniform(50, 300)
    
    # Determine fertilizer based on nutrient levels and ratios
    if nitrogen < 40:
        fertilizer = 'Urea'
    elif phosphorus < 20:
        fertilizer = 'DAP'
    elif potassium < 20:
        fertilizer = 'MOP'
    elif nitrogen > 80 and phosphorus > 40:
        fertilizer = '17-17-17'
    elif nitrogen < 60 and phosphorus > 50:
        fertilizer = '14-35-14'
    elif potassium > 60:
        fertilizer = '10-26-26'
    elif nitrogen > 90:
        fertilizer = '28-28'
    else:
        fertilizer = '20-20'
    
    data.append({
        'Nitrogen': round(nitrogen, 2),
        'Phosphorus': round(phosphorus, 2),
        'Potassium': round(potassium, 2),
        'Temperature': round(temperature, 2),
        'Humidity': round(humidity, 2),
        'pH': round(ph, 2),
        'Rainfall': round(rainfall, 2),
        'Crop': crop,
        'Fertilizer': fertilizer
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data/raw/fertilizer_data.csv', index=False)

print(f"Dataset generated successfully!")
print(f"Total samples: {len(df)}")
print(f"\nFertilizer distribution:")
print(df['Fertilizer'].value_counts())
print(f"\nCrop distribution:")
print(df['Crop'].value_counts())
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())
