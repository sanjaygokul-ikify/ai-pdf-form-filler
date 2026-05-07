import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Define the AI model
class AIModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    # Define the train method
    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    # Define the predict method
    def predict(self, X):
        return self.model.predict(X)