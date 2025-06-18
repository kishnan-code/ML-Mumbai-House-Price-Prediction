import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df.drop(columns=['title', 'age', 'total_floors', 'price_per_sqft', 'area'], inplace=True)
    return df

def encode_categorical_columns(df):
    label_encoders = {}
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    joblib.dump(label_encoders, "models/Encoder.pkl")
    return df, label_encoders

def scale_features(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    joblib.dump(scaler, "models/scaler.pkl")
    return X_train_scaled, X_test_scaled, scaler
