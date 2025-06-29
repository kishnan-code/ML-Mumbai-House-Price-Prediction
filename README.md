## Designed and Developed by Vishal Jamalpuri & Kishan Prajapati

# 🏠 Mumbai House Price Prediction

A web-based machine learning application to predict house prices in Mumbai using a trained Random Forest Regressor model and real estate data.

## 🧠 Key Features

* 📊 Predicts Mumbai house prices using trained ML model.
* ⚙️ Flask-based REST API backend.
* 🐘 MySQL for data storage and retrieval.
* 🌟 Real-time price prediction with both numeric and word format.
* 📄 HTML front-end form for user interaction.
* 📈 Modular and extensible ML pipeline for future improvement.
* 🧪 Error handling with full stack trace for debugging.
* 🔐 CORS enabled for frontend-backend communication.
* 🐳 Dockerized for easy deployment.

---

## 📁 Project Structure

```
├── app.py              # Flask app with model and API
├── Dockerfile          # For containerization
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Main UI page (form-based input)
├── static/             # (Optional) for CSS/JS/images
└── README.md
```

---

## 🔧 Setup Instructions

### 👤 Local Development

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/mumbai-house-price-predictor.git
   cd mumbai-house-price-predictor
   ```

2. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Start your MySQL server** and ensure a database called `mumbai` exists with the cleaned dataset:

   * Table: `mumbai-house-price-data-cleaned`

4. **Run the application**

   ```bash
   python app.py
   ```

5. Visit `http://localhost:5000` in your browser.

---

## 🐳 Docker Deployment

1. **Build the Docker image**

   ```bash
   docker build -t mumbai-price-predictor .
   ```

2. **Run the container**

   ```bash
    run app.py
   ```

---



## 🧪 Development Notes

* 🗃️ Model training is done in `app.py` on app start using MySQL data.
* 🧠 Random Forest is used for prediction; can be swapped with XGBoost/SVR.
* 📊 Encoders and scalers are reused during prediction to maintain consistency.
* 🧵 Future features may include model versioning, UI themes, and analytics.

---

## 📦 Requirements

* Python 3.8+
* Flask
* Pandas
* scikit-learn
* mysql-connector-python
* inflect

---

## 📍 Dataset Columns Used

* `Region`
* `locality`
* `property_type`
* `bedroom_num`
* `bathroom_num`
* `balcony_num`
* `furnished`
* `latitude`
* `longitude`
* `price` (target)

---

## 🙏 Acknowledgements

* Real estate data: Mumbai housing dataset (cleaned version)
* UI and deployment assistance by community examples

---

## 📬 Contact

For improvements or issues, please open an issue or contact \[your email/username].

---

## 🚀 Future Improvements

* Integrate frontend framework like React or Vue.
* Add model training UI for live retraining.
* Host database on cloud (e.g., AWS RDS or PlanetScale).
* Improve visualizations for predictions.
* Add authentication for API security.
* Extend to other cities.
#
