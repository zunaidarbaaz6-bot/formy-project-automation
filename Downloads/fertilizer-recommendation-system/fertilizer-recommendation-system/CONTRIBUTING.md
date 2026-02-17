# Contributing to Fertilizer Recommendation System

Thank you for considering contributing to this project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Your environment (Python version, OS, etc.)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:
- Clear description of the enhancement
- Why it would be useful
- Potential implementation approach

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/fertilizer-recommendation-system.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Write clear, commented code
   - Follow existing code style
   - Add tests if applicable

4. **Test your changes**
   ```bash
   python src/generate_dataset.py
   python src/data_preprocessing.py
   python src/train_model.py
   python src/predict.py
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose

### Example:

```python
def calculate_npk_ratio(nitrogen, phosphorus, potassium):
    """
    Calculate NPK nutrient ratios.
    
    Args:
        nitrogen (float): Nitrogen content in kg/ha
        phosphorus (float): Phosphorus content in kg/ha
        potassium (float): Potassium content in kg/ha
    
    Returns:
        dict: Dictionary containing NPK ratios
    """
    return {
        'N_P_ratio': nitrogen / (phosphorus + 1),
        'N_K_ratio': nitrogen / (potassium + 1),
        'P_K_ratio': phosphorus / (potassium + 1)
    }
```

## Development Setup

1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install development dependencies:
   ```bash
   pip install pytest flake8 black
   ```

## Testing

Before submitting a PR:

1. **Run the complete pipeline:**
   ```bash
   python src/generate_dataset.py
   python src/data_preprocessing.py
   python src/train_model.py
   python src/visualize_data.py
   python src/predict.py
   ```

2. **Check code quality:**
   ```bash
   flake8 src/
   black src/
   ```

## Areas for Contribution

We especially welcome contributions in:

1. **New Features:**
   - Additional crop types
   - Weather API integration
   - Mobile app development
   - Web dashboard

2. **Model Improvements:**
   - Hyperparameter optimization
   - Alternative ML algorithms
   - Ensemble methods
   - Deep learning models

3. **Data Enhancements:**
   - Real agricultural datasets
   - Regional calibration
   - Soil micronutrients
   - Organic fertilizer options

4. **Documentation:**
   - Tutorial videos
   - Case studies
   - API documentation
   - Translations

5. **Testing:**
   - Unit tests
   - Integration tests
   - Performance benchmarks

## Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Follow the code of conduct

## Questions?

Feel free to open an issue for any questions or discussions!

Thank you for contributing! 🌱
