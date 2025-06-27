import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# دانلود دیتاست ساده
data = pd.read_csv("https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/train.csv")

# انتخاب ستون‌های مورد نیاز
data = data[['label', 'tweet']]
data['label'] = data['label'].map({0: 'negative', 1: 'positive'})

# تقسیم داده‌ها
X_train, X_test, y_train, y_test = train_test_split(data['tweet'], data['label'], test_size=0.2, random_state=42)

# ساخت مدل
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# ارزیابی مدل
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# ذخیره مدل
joblib.dump(model, 'sentiment_model.pkl')
