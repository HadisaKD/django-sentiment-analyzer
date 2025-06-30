from pathlib import Path

readme_content = """
# 🧠 Sentiment Analysis Web App

A simple web application built with Django that uses a machine learning model to analyze the **sentiment** of user-submitted text messages (positive or negative).

---

## 🚀 Features

- ✅ Custom trained ML model (Logistic Regression)
- 🧪 Text classification using TF-IDF vectorizer
- 💬 Form to input messages
- 📊 Displays prediction result (positive/negative)
- 💾 Stores each message and its sentiment in a database
- 🎨 Styled with Bootstrap for a clean and responsive UI
- 🧠 Trained on a custom dataset with balanced positive/negative samples

---


## ⚙️ Installation

### 1. Clone the repository

```bash
    git clone https://github.com/HadisaKD/django-sentiment-analyzer.git
    cd django-sentiment-analyzer
```
### 2. Create and activate virtual environment

```bash
    python -m venv .venv
    # Windows:
    .venv\\Scripts\\activate
    # macOS/Linux:
    source .venv/bin/activate
```
### 3. Install dependencies
```bash
    pip install -r requirements.txt
```

### 4. Run migrations
```bash
  python manage.py migrate
```

### 5. Train the ML model (optional)
```bash
  python train_model.py
```
### 6. Run the server
```bash
  python manage.py runserver
```
---

## 📊 Model Info
* Vectorizer: TfidfVectorizer (unigrams + bigrams)

* Classifier: Logistic Regression (class_weight balanced)

* Training Accuracy: ~86%

* Dataset: Custom 200-sample dataset (balanced)

---

## Author
**Made with ❤️ by HadisaKD**

"""

readme_path = Path("/mnt/data/README.md")
readme_path.write_text(readme_content.strip())
readme_path.name


Result
'README.md'