import pytest
# TODO: add necessary import
from ml.model import train_model
from ml.data import process_data
import pandas as pd
from ml.model import compute_model_metrics
import numpy as np
from sklearn.model_selection import train_test_split

# TODO: implement the first test. Change the function name and input as needed
# load sample data for test
@pytest.fixture
def sample_data():
    
    df = pd.read_csv("data/census.csv")
    
    cat_features = [
        "workclass", "education", "marital-status", "occupation",
        "relationship", "race", "sex", "native-country"
    ]
    train, _ = train_test_split(df, test_size=0.20)
    X_train, y_train, encoder, lb = process_data (
        train, categorical_features=cat_features, label="salary", training=True
    )
    return X_train, y_train

def test_train_model_returns_classifier(sample_data):
    """
    Test that train model retunrns a trained classifier object
    """
    X_train, y_train = sample_data
    model = train_model(X_train, y_train)
    from sklearn.base import ClassifierMixin
    assert isinstance(model, ClassifierMixin)
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics_output():
    """
    Test that compute_model_metrics t=returns float precision, recall, f1
    """
    y = np.array([1, 0, 1, 0])
    preds = np.array([1, 0, 1, 1])
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)
        
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_process_data_shape():
    """
    Test that process_data returns arrayswith matching number of rows
    """
    df = pd.read_csv("data/census.csv")
    
    cat_features = [
        "workclass", "education", "marital-status", "occupation",
        "relationship", "race", "sex", "native-country"
    ]
    train, _ = train_test_split(df, test_size=0.20)
    x, y, _, _ = process_data(train, categorical_features=cat_features, label="salary", training=True)
    assert len(x) == len(y)
    pass
