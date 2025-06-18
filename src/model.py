from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor
import joblib

def split_data(df):
    X = df.drop("price", axis=1)
    y = df["price"]
    return train_test_split(X, y, test_size=0.2, random_state=1)

def train_model(X_train, y_train):
    model = CatBoostRegressor(verbose=0, iterations=500)
    model.fit(X_train, y_train)
    joblib.dump(model, "models/model.pkl")
    return model
