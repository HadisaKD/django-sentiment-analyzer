import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import joblib

def preprocess(text):
    return text.lower()

# Load dataset (ensure it's clean and in the project directory)
data = pd.read_csv("custom_dataset.csv", quotechar='"')
data['label'] = data['label'].map({0: 'negative', 1: 'positive'})
data['tweet'] = data['tweet'].apply(preprocess)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    data['tweet'], data['label'], test_size=0.2, random_state=42, stratify=data['label']
)

# Build and train model
model = make_pipeline(
    TfidfVectorizer(ngram_range=(1, 2)),
    LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42)
)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'sentiment_model.pkl')
