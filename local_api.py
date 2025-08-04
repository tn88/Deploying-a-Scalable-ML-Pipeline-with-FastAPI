import json

import requests

# TODO: send a GET using the URL http://127.0.0.1:8000
r = requests.get("http://127.0.0.1.8000/")
# TODO: print the status code
print(f"GET status code: {r.status_code}")

# TODO: print the welcome message
try:
    print(f"GET response: {r.text}")
except Exception as e:
    print(f"GET failed to decode JSON:, {e}")


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education_num": 10,
    "marital_status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital_gain": 0,
    "capital_loss": 0,
    "hours_per_week": 40,
    "native_country": "United-States"
}

# TODO: send a POST using the data above
r = requests.post("http://127.0.0.1.8000/data/", json=data)

# TODO: print the status code
print(f"POST status code: {r.status_code}")
try:
    print(f"POST response: {r.text}")
except Exception as e:
    print(f"POST failed to decode JSON:, {e}")

