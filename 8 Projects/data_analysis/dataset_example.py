import pandas as pd

data = {
    "Name": ["Hit", "Raj", "Amit"],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

# Filter students with marks > 85
result = df[df["Marks"] > 85]

print(result)