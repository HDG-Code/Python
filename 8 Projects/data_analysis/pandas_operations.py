import pandas as pd

data = {
    "Name": ["Hit", "Raj", "Amit"],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print("Head:\n", df.head())
print("Average Marks:", df["Marks"].mean())