import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load datasets
careers_df = pd.read_csv("dataset/careers_dataset.csv")
skills_df = pd.read_csv("dataset/skills_mapping.csv")

# Label Encode career names
label_encoder = LabelEncoder()
careers_df['career_label'] = label_encoder.fit_transform(careers_df['Career'])

# Train model
X = skills_df.drop(columns=['Career'])
y = careers_df['career_label']
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("career_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model training completed & saved!")