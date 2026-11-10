import pandas as pd
import random

crops = [
    "rice","maize","coffee","wheat","cotton","sugarcane",
    "banana","mango","apple","chickpea","lentil","pomegranate",
    "coconut","jute","papaya","grapes","orange","barley","millet"
]

data = []

for _ in range(2000):
    N = random.randint(10, 100)
    P = random.randint(10, 100)
    K = random.randint(10, 100)
    temp = round(random.uniform(15, 35), 1)
    humidity = random.randint(40, 90)
    ph = round(random.uniform(5.0, 7.5), 1)
    rainfall = random.randint(50, 300)

    crop = random.choice(crops)

    data.append([N,P,K,temp,humidity,ph,rainfall,crop])

df = pd.DataFrame(data, columns=[
    "N","P","K","temperature","humidity","ph","rainfall","label"
])

df.to_csv("crop_data.csv", index=False)

print("Dataset created successfully!")