# 🌸 OIBSIP — Oasis Infobyte Data Science Internship Projects

> **Internship:** Oasis Infobyte — Data Science Track  
> **Intern:** Ayesha Khan  
> **Institution:** Oriental Institute of Science and Technology, Bhopal  
> **Program:** B.Tech CSE (Data Science), Batch 2027

---

## 📌 Repository Overview

This repository contains **3 machine learning projects** completed as part of the **Oasis Infobyte Data Science Internship (OIBSIP)**. Each task demonstrates end-to-end data science workflow — from data loading and EDA to model building, evaluation, and deployment.

| Task | Project | Type | Notebook |
|------|---------|------|---------|
| Task 1 | 🌸 Iris Flower Classification | Multi-class Classification | [AyeshKhan_1.ipynb](./AyeshKhan_1.ipynb) |
| Task 3 | 🚗 Car Price Prediction | Regression | [AyeshaKhan_3.ipynb](./AyeshaKhan_3.ipynb) |
| Task 4 | 📧 Email Spam Detection | Binary Classification | [AyeshaKhan_4.ipynb](./AyeshaKhan_4.ipynb) |

---

## 🔗 Live Demo Links

| Project | Live App |
|---------|----------|
| 📧 Email Spam Detector | 🔗 https://smart-email-assistant-3ovqtpn3nem4qcmvjyzdav.streamlit.app/  |

---

## 📁 Repository Structure

```
OIBSIP/
│
├── AyeshKhan_1.ipynb          # Task 1 — Iris Flower Classification
├── AyeshaKhan_3.ipynb         # Task 3 — Car Price Prediction
├── AyeshaKhan_4.ipynb         # Task 4 — Email Spam Detection
│
├── app.py                     # Streamlit Web App — Email Spam Detector
├── email_model.pkl            # Trained Email Classification Model
├── tfidf.pkl                  # Saved TF-IDF Vectorizer
│
├── Car_Price_Prediction_Report.docx  # Detailed Project Report
├── Iris_ML_Report.docx               # Detailed Project Report
├── requriements.txt           # Python dependencies
└── README.md
```

---

## 🌸 Task 1 — Iris Flower Classification

### 📖 Overview
A classic multi-class classification project to identify **three species of Iris flowers** (Setosa, Versicolor, Virginica) based on their physical measurements — sepal length, sepal width, petal length, and petal width.

### 🎯 Objective
Build a machine learning model that accurately classifies iris flower species from 4 numerical input features.

### 📊 Dataset
- **Source:** UCI Machine Learning Repository / Scikit-learn built-in dataset
- **Size:** 150 samples × 5 features
- **Target Classes:** Iris-setosa, Iris-versicolor, Iris-virginica
- **Features:** Sepal Length, Sepal Width, Petal Length, Petal Width (all in cm)

### 🔬 Methodology
| Step | Description |
|------|-------------|
| EDA | Pair plots, violin plots, correlation heatmap to understand feature separability |
| Preprocessing | Feature scaling with StandardScaler, train-test split (80-20) |
| Models Applied | Logistic Regression, K-Nearest Neighbors (KNN), Decision Tree, Random Forest, SVM |
| Evaluation | Accuracy Score, Confusion Matrix, Classification Report |

### 📈 Results
| Model | Accuracy |
|-------|----------|
| Logistic Regression | ~96–97% |
| K-Nearest Neighbors | ~96–98% |
| Decision Tree | ~94–96% |
| Random Forest | ~96–98% |
| SVM | ~97–98% |

### 💡 Key Insights
- **Petal Length and Petal Width** are the most discriminative features — Setosa is completely linearly separable from the other two species
- **Versicolor and Virginica** have slight overlap, making them the harder pair to classify
- SVM and Random Forest achieved the highest generalization accuracy

### 🛠️ Tech Stack
`Python` `Pandas` `NumPy` `Scikit-learn` `Matplotlib` `Seaborn` `Jupyter Notebook`

### 📂 Files
- `AyeshKhan_1.ipynb` — Full notebook with EDA, model training, and evaluation
- `Iris_ML_Report.docx` — Detailed project report

---

## 🚗 Task 3 — Car Price Prediction

### 📖 Overview
A regression project to **predict used car prices** based on vehicle attributes using the Ford used car dataset. Two encoding strategies were compared to identify the best approach for categorical feature handling.

### 🎯 Objective
Develop a regression model that accurately estimates used Ford car prices from features like model, year, mileage, transmission, fuel type, tax, MPG, and engine size.

### 📊 Dataset
- **Source:** Ford Used Car Dataset (ford.csv)
- **Features:** model, year, transmission, mileage, fuelType, tax, mpg, engineSize
- **Target:** price (GBP)
- **Data Quality:** No missing values, cleaned dataset

### 🔬 Methodology
| Step | Description |
|------|-------------|
| EDA | Histplot (price distribution), correlation heatmap, boxplots per feature |
| Encoding A | One-Hot Encoding via `pd.get_dummies()` — expands categorical features to binary columns |
| Encoding B | Label Encoding via `LabelEncoder` — assigns integer codes to categories |
| Scaling | StandardScaler applied to: year, mileage, tax, mpg, engineSize |
| Model | Linear Regression (trained under both encoding schemes) |
| Evaluation | R² Score, Adjusted R² Score |
| Split | 67% train / 33% test (`random_state=42`) |

### 📈 Results
| Model | Encoding | R² Score | Adjusted R² |
|-------|----------|----------|-------------|
| Linear Regression A | One-Hot Encoding | ~0.85–0.86 | ~0.84–0.85 |
| Linear Regression B | Label Encoding | ~0.79–0.83 | ~0.79–0.82 |

> **Winner:** One-Hot Encoding — better handles nominal categories without imposing false ordinal relationships

### 💡 Key Insights
- **Year** is the strongest price predictor — newer cars consistently command higher prices
- **Mileage** shows negative correlation — depreciation with usage
- **Engine Size** positively correlates with price — reflects performance tier
- **Automatic/Hybrid** vehicles priced significantly higher than Manual/Petrol counterparts

### 🛠️ Tech Stack
`Python` `Pandas` `NumPy` `Scikit-learn` `Matplotlib` `Seaborn` `Jupyter Notebook`

### 📂 Files
- `AyeshaKhan_3.ipynb` — Full notebook with complete ML pipeline
- `Car_Price_Prediction_Report.docx` — Detailed project report

---

## 📧 Task 4 — Email Spam Detection

### 📖 Overview
A binary text classification project that builds an **Email Spam Detector** using NLP and machine learning. The trained model is deployed as an interactive **Streamlit web application** where users can input any email text and get instant spam/ham classification.

### 🎯 Objective
Train a machine learning classifier to detect whether an email is **Spam** or **Not Spam (Ham)**, and deploy it as a live web app.

### 📊 Dataset
- **Source:** Email/SMS Spam Collection Dataset
- **Classes:** Spam (1) / Ham — Not Spam (0)
- **Features:** Raw email text

### 🔬 Methodology
| Step | Description |
|------|-------------|
| Text Preprocessing | Lowercasing, punctuation removal, stopword removal |
| Feature Extraction | TF-IDF Vectorizer (Term Frequency–Inverse Document Frequency) |
| Model | Naive Bayes / Logistic Regression classifier |
| Evaluation | Accuracy, Precision, Recall, F1-Score, Confusion Matrix |
| Deployment | Streamlit web app with saved `email_model.pkl` and `tfidf.pkl` |

### 📈 Results
| Metric | Score |
|--------|-------|
| Accuracy | ~97–98% |
| Precision (Spam) | ~95–97% |
| Recall (Spam) | ~94–96% |
| F1-Score | ~95–97% |

### 🌐 Web App — How to Run Locally

```bash
# Clone the repository
git clone https://github.com/ayshakhan78/OIBSIP.git
cd OIBSIP

# Install dependencies
pip install -r requriements.txt

# Run the Streamlit app
streamlit run app.py
```

Open your browser at `http://localhost:8501` — paste any email text and get instant spam/ham prediction!

### 💡 Key Insights
- **TF-IDF** outperforms simple Bag-of-Words by accounting for word importance across the corpus
- Words like "free", "win", "click here", "congratulations" are highly predictive of spam
- The model achieves high precision — minimizes false positives (legitimate emails marked as spam)

### 🛠️ Tech Stack
`Python` `Pandas` `NumPy` `Scikit-learn` `NLTK` `Streamlit` `Pickle` `Jupyter Notebook`

### 📂 Files
- `AyeshaKhan_4.ipynb` — Training notebook: EDA, preprocessing, model building
- `app.py` — Streamlit web application
- `email_model.pkl` — Serialized trained classifier
- `tfidf.pkl` — Serialized TF-IDF vectorizer
- `requriements.txt` — Python dependencies

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/ayshakhan78/OIBSIP.git
cd OIBSIP

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requriements.txt

# 4. Launch Jupyter to explore notebooks
jupyter notebook

# 5. Run the Email Spam Detector web app
streamlit run app.py
```

---

## 🧰 Common Dependencies

```
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
nltk
jupyter
```

---

## 👩‍💻 About the Intern

**Ayesha Khan**  
B.Tech CSE (Data Science) — Batch 2027  
Oriental Institute of Science and Technology, Bhopal  

🔗 [GitHub](https://github.com/ayshakhan78) &nbsp;|&nbsp; 🔗 [LinkedIn](https://www.linkedin.com/in/ayesha-khan) &nbsp;|&nbsp; 📧 *ayesha.khan@email.com*

---

## 🏢 About Oasis Infobyte

[Oasis Infobyte](https://oasisinfobyte.com/) is a tech-education company offering real-world internship programs in Data Science, Web Development, Android Development, and more. The OIBSIP (Oasis Infobyte Summer Internship Program) provides hands-on industry exposure to students.

---

This project is for **educational and internship submission purposes** only.  
© 2025 Ayesha Khan — Oasis Infobyte Internship

---

> ⭐ *If you found this helpful, consider starring the repository!*
