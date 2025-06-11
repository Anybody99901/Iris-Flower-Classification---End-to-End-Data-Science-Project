COMPANY : CODTECH IT SOLUTIONS

NAME : YASEER SHAIK

INTERN ID : CT06DM03

DOMAIN : DATA SCEINCE

DURATION : 6 WEEKS

MENTOR : NEELA SANTHOSH

# 🌸 Iris Flower Classification - End-to-End Data Science Project

This project is developed as part of **CodTech Internship - Task 3**. It is an end-to-end data science project that includes:
- Data collection and preprocessing
- Model training and evaluation
- Web app development using Flask
- Deployment-ready structure with both UI and API

---

## 🚀 Tech Stack

- Python
- Scikit-learn
- Flask
- HTML (Jinja2 template)

---

## 📊 Dataset

We use the built-in **Iris dataset** from `sklearn.datasets`.

It contains:
- 150 samples
- 4 features:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- 3 classes:
  - Iris Setosa
  - Iris Versicolor
  - Iris Virginica

---

## 🔧 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/iris-flower-classifier.git
cd iris-flower-classifier
```
### 2. Install Requirements
```bash
pip install -r requirements.txt
```
If requirements.txt is not present, you can install manually:

```
pip install flask scikit-learn joblib
```
### 3. Train the Model
```
python iris_model_training.py
```
This will create model.pkl and scaler.pkl.

### 4. Run the Flask App
```
python app.py
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the app.

# 📡 API Endpoint
You can also use the REST API at:

POST /api/predict

> Sample JSON Body:


```
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```
> Sample Response:

```
{
  "prediction": "Setosa"
}
```
