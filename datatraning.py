import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

# ==========================================
# 1. DATA LOADING & EXPLORATION
# ==========================================
def load_and_explore():
    print("--- Loading Dataset ---")
    # Using the famous Iris dataset
    from sklearn.datasets import load_iris
    iris = load_iris()
    
    # Create a DataFrame for easier manipulation
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    
    print(f"Dataset Shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
    return iris, df

# ==========================================
# 2. DATA PREPROCESSING
# ==========================================
def preprocess_data(iris_data):
    X = iris_data.data  # Features: sepal length/width, petal length/width
    y = iris_data.target # Target: species
    
    # Split data: 80% Training, 20% Testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Feature Scaling (Crucial for many algorithms)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test, scaler

# ==========================================
# 3. MODEL TRAINING
# ==========================================
def train_model(X_train, y_train):
    print("\n--- Training Random Forest Classifier ---")
    # Initialize the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Fit the model to the training data
    model.fit(X_train, y_train)
    return model

# ==========================================
# 4. EVALUATION
# ==========================================
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    
    acc = accuracy_score(y_test, predictions)
    print(f"\nModel Accuracy: {acc * 100:.2f}%")
    
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))
    
    # Display Confusion Matrix
    cm = confusion_matrix(y_test, predictions)
    print("\nConfusion Matrix:")
    print(cm)

# ==========================================
# 5. SAVING THE MODEL (PERSISTENCE)
# ==========================================
def save_artifacts(model, scaler):
    print("\n--- Saving Model and Scaler ---")
    joblib.dump(model, 'iris_model.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    print("Files 'iris_model.pkl' and 'scaler.pkl' saved successfully.")

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    # Step 1: Get Data
    raw_data, dataframe = load_and_explore()
    
    # Step 2: Prep Data
    X_train, X_test, y_train, y_test, scaler = preprocess_data(raw_data)
    
    # Step 3: Train
    clf = train_model(X_train, y_train)
    
    # Step 4: Evaluate
    evaluate_model(clf, X_test, y_test)
    
    # Step 5: Save
    save_artifacts(clf, scaler)
    
    print("\nTraining Pipeline Complete.")