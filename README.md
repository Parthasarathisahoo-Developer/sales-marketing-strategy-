# 📊 Sales Analytics & Forecasting System

## 📌 Project Overview

The **Sales Analytics & Forecasting System** is a database-driven application that allows users to manage sales data, visualize insights, and predict future sales using machine learning.

This project combines **DBMS concepts, Python backend, data visualization, and a modern GUI** to create a complete real-world solution.

---

## 🚀 Features

### 🔐 Authentication

* User Registration & Login system
* Session-based authentication

### 📦 Sales Management (CRUD)

* Add new sales records
* View all sales data
* Update existing records
* Delete records

### 📊 Dashboard (KPIs)

* Total Sales
* Total Revenue
* Average Sales

### 📈 Data Visualization

* Product-wise sales graph
* Time-based sales trends

### 🎯 Filters

* Filter by product
* Filter by date range

### 🔮 Sales Prediction

* Predict future sales using **Linear Regression**

### 📥 Export

* Download filtered data as Excel file

### 🎨 UI & Branding

* Modern dashboard layout
* KPI cards with colors
* Custom logo support

---

## 🛠️ Tech Stack

| Category      | Technology   |
| ------------- | ------------ |
| Language      | Python       |
| Database      | SQLite       |
| GUI Framework | Streamlit    |
| Data Handling | Pandas       |
| Visualization | Matplotlib   |
| ML Model      | Scikit-learn |
| Export        | OpenPyXL     |

---

## 📂 Project Structure

```
sales_project/
│
├── app.py           # Main Streamlit app
├── database.py      # Database operations (CRUD)
├── model.py         # Sales prediction model
├── auth.py          # Login & authentication
├── sales.db         # SQLite database
├── logo.png         # Project logo
└── requirements.txt # Dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/sales-project.git
cd sales-project
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

The app will open in your browser.

---

## 🌐 Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Go to https://streamlit.io/cloud
3. Click **New App**
4. Select your repository
5. Choose `app.py`
6. Click **Deploy**

---

## 📊 How It Works

1. User logs in or registers
2. Sales data is stored in SQLite database
3. Dashboard displays KPIs and graphs
4. Filters allow data analysis
5. ML model predicts future sales

---

## 📚 DBMS Concepts Used

* Relational Database Design
* Normalization (1NF, 2NF, 3NF)
* CRUD Operations
* Entity Relationships
* Data Integrity

---

## 🎯 Future Enhancements

* Password encryption (security improvement)
* Advanced forecasting models
* Interactive charts (Plotly)
* Multi-user roles (Admin/User)
* Cloud database (MySQL/PostgreSQL)

---

## 👨‍💻 Author

**Parthasarathi sahoo**

---

## ⭐ Conclusion

This project demonstrates how **database systems, data analytics, and machine learning** can be integrated into a single application to solve real-world business problems.

It provides both **data management** and **decision-making insights**, making it a complete end-to-end solution.

---
