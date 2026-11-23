# ☀️ Solar Power Generation Prediction

## 📌 Project Overview

This project focuses on analyzing and predicting **AC power generation** in a Solar Photovoltaic (PV) plant using Machine Learning.

The project follows an end-to-end Data Science and application development pipeline, including:

- Data Understanding
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning
- Model Evaluation
- Frontend Development
- Backend Development
- ML Model Integration

The objective is to identify important factors affecting solar power generation and develop a regression model that predicts AC power from environmental conditions, inverter information, and time-based features.

The trained model is integrated into a web application that supports manual predictions and estimated predictions using weather data retrieved through the Open-Meteo API.

---

## 📂 Dataset

The project uses the **Solar Power Generation Dataset**, consisting of plant generation data and weather sensor data.

### Key Features

- Plant ID
- Inverter ID
- AC Power
- DC Power
- Daily Yield
- Total Yield
- Ambient Temperature
- Module Temperature
- Irradiation
- Date and Time

AC Power (`AC_POWER`) is the target variable that the machine learning models are trained to predict.

---

## 🛠 Tech Stack

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Development Environment:** Jupyter Notebook
- **Backend:** Flask, Flask-CORS
- **Model Serialization:** Joblib
- **Frontend:** HTML, CSS, JavaScript
- **Weather API:** Open-Meteo API
- **Version Control:** Git, GitHub, Git LFS

---

## 📁 Project Structure

```text
Solar/
│
├── Data/
│   ├── Raw/
│   │   ├── Plant_1_Generation_Data.csv
│   │   ├── Plant_1_Weather_Sensor_Data.csv
│   │   ├── Plant_2_Generation_Data.csv
│   │   └── Plant_2_Weather_Sensor_Data.csv
│   │
│   └── Cleaned/
│       ├── Plant_1_Generation_Cleaned.csv
│       ├── Plant_1_Weather_Cleaned.csv
│       ├── Plant_1_Feature_Engineered.csv
│       ├── Plant_2_Generation_Cleaned.csv
│       ├── Plant_2_Weather_Cleaned.csv
│       └── Plant_2_Feature_Engineered.csv
│
├── Notebooks/
│   ├── Data_understanding.ipynb
│   ├── Data_cleaning.ipynb
│   ├── Data_cleaning_Plant_2.ipynb
│   ├── EDA.ipynb
│   ├── EDA_Plant_2.ipynb
│   ├── Feature_Engineering.ipynb
│   ├── Feature_Engineering_Plant_2.ipynb
│   ├── Machine_Learning.ipynb
│   └── Machine_Learning_Plant_2.ipynb
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── report/
│   └── Data_Dictionary.md
│
├── random_forest_model.pkl          # Trained model for Plant 1
├── random_forest_model_plant_2.pkl  # Trained model for Plant 2
├── .gitattributes
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 Project Workflow

### 1. Data Understanding

- Loaded and inspected the generation and weather datasets.
- Examined dataset dimensions, column names, and data types.
- Checked missing values and duplicate records.
- Prepared a data dictionary to describe the dataset features.

### 2. Data Cleaning

- Converted date-time columns into a suitable datetime format.
- Inspected data quality and prepared cleaned datasets.
- Organized the data for exploratory analysis and feature engineering.

### 3. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand patterns in solar power generation and its relationship with environmental conditions.

The analysis included:

- AC Power Distribution
- Ambient and Module Temperature Distribution
- Irradiation Distribution
- Correlation Analysis
- Hourly Power Generation
- Daily Power Generation Patterns
- Weather Trends
- Relationships between Weather Parameters and AC Power

### 4. Feature Engineering

The feature engineering stage prepares the input variables required by the machine learning models.

- Combined generation and weather data.
- Extracted time-based features:
  - `HOUR`
  - `DAY`
  - `MONTH`
  - `WEEKDAY`
  - `IS_WEEKEND`
- Encoded the inverter identifier as `SOURCE_KEY_x`.
- Removed `DC_POWER`, `DAILY_YIELD`, `TOTAL_YIELD`, `SOURCE_KEY_y`, and `PLANT_ID` from the model inputs.

These exclusions reduce dependence on variables that may be highly correlated with generation output or are not useful for the intended prediction setup.

### 5. Machine Learning

The project formulates solar power prediction as a **supervised regression problem**.

The target variable is:

```text
y = AC_POWER
```

The input features are:

```text
SOURCE_KEY_x
AMBIENT_TEMPERATURE
MODULE_TEMPERATURE
IRRADIATION
HOUR
DAY
MONTH
WEEKDAY
IS_WEEKEND
```

Five regression algorithms were implemented and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

The dataset is split into training and testing subsets using an **80/20 train-test split**, with `random_state=14`.

The models are evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the R² score.

Models are saved as `random_forest_model.pkl` (Plant 1) and `random_forest_model_plant_2.pkl` (Plant 2), loaded by the Flask backend for predictions.

---

## 📊 Model Performance

### Plant 1 (Plant ID: 4135001)

Results from the execution of `Machine_Learning.ipynb`:

| Model | MAE ↓ | RMSE ↓ | R² Score ↑ |
|---|---:|---:|---:|
| Linear Regression | 26.4128 | 58.5295 | 0.9781 |
| Decision Tree Regressor | 18.7169 | 56.1634 | 0.9799 |
| Gradient Boosting Regressor | 18.3376 | 49.8359 | 0.9842 |
| Random Forest Regressor | 15.1623 | 47.5860 | 0.9856 |
| **XGBoost Regressor** | **14.7004** | **40.4904** | **0.9895** |

*For Plant 1, **XGBoost Regressor** achieved the best overall performance with the lowest MAE (14.70 kW), lowest RMSE (40.49 kW), and highest R² score (0.9895).*

### Plant 2 (Plant ID: 4136001)

Results from the execution of `Machine_Learning_Plant_2.ipynb`:

| Model | MAE ↓ | RMSE ↓ | R² Score ↑ |
|---|---:|---:|---:|
| Linear Regression | 124.7696 | 222.9505 | 0.6172 |
| Gradient Boosting Regressor | 87.2231 | 195.3147 | 0.7062 |
| Decision Tree Regressor | 42.7057 | 162.7102 | 0.7961 |
| XGBoost Regressor | 56.6153 | 141.5564 | 0.8457 |
| **Random Forest Regressor** | **42.8340** | **120.9530** | **0.8873** |

*For Plant 2, **Random Forest Regressor** achieved the best overall performance with the lowest RMSE (120.95 kW), lowest MAE (42.83 kW), and highest R² score (0.8873), followed closely by XGBoost (R² 0.8457).*

**Evaluation metrics:**

- **Mean Absolute Error (MAE):** Measures the average absolute difference between actual and predicted AC power.
- **Root Mean Squared Error (RMSE):** Measures prediction error while penalizing larger errors more heavily.
- **R² Score:** Indicates how much variation in the target variable is explained by the model.

---

## 📈 Feature Importance Comparison

Feature importance was extracted from the trained models for each plant:

| Feature | Plant 1 (RF) | Plant 1 (XGBoost) | Plant 2 (RF) | Plant 2 (XGBoost) |
|---|---:|---:|---:|---:|
| `IRRADIATION` | 98.49% | 97.94% | 70.74% | 56.37% |
| `SOURCE_KEY_x` | 0.75% | 0.20% | 11.14% | 4.07% |
| `DAY` | 0.13% | 0.37% | 5.40% | 5.79% |
| `MODULE_TEMPERATURE` | 0.21% | 0.18% | 4.27% | 2.34% |
| `AMBIENT_TEMPERATURE` | 0.16% | 0.17% | 3.15% | 2.17% |
| `WEEKDAY` | 0.10% | 0.44% | 2.80% | 5.99% |
| `HOUR` | 0.12% | 0.38% | 1.38% | 2.84% |
| `MONTH` | 0.03% | 0.32% | 0.70% | 20.44% |
| `IS_WEEKEND` | 0.01% | 0.00% | 0.04% | 0.00% |

### Key Findings & Cross-Plant Analysis

- **Irradiation is the primary predictor** across both facilities, accounting for ~98% of importance in Plant 1 and ~56–71% in Plant 2.
- **Inverter heterogeneity in Plant 2**: In Plant 2, inverter identity (`SOURCE_KEY_x`) accounts for a significantly larger share of importance (11.14% in RF), reflecting notable operational divergence, shading differences, or panel degradation across individual inverter strings at Plant 2.
- **Ensemble comparisons**: Gradient boosting architectures (XGBoost) proved most effective at minimizing residual errors for Plant 1, while bagging ensembles (Random Forest) provided superior robustness and stability against inverter variance in Plant 2.

---

## 🌐 Web Application

The project includes a web application that integrates the trained machine learning model with a user-friendly interface.

### Frontend

The frontend is developed using HTML, CSS, and JavaScript.

- **HTML:** Defines the structure of the application.
- **CSS:** Provides styling and layout.
- **JavaScript:** Handles user interactions, weather data retrieval, input preparation, and communication with the backend API.

The interface provides options for live-weather-based predictions and manual predictions.

### Backend

The backend is developed using **Flask**, a lightweight Python web framework, with Flask-CORS for cross-origin communication.

The backend exposes a `/predict` API endpoint that:

1. Receives model input features from the frontend.
2. Arranges the input data in the format expected by the trained model.
3. Loads the corresponding saved Random Forest model (`random_forest_model.pkl` for Plant 1 or `random_forest_model_plant_2.pkl` for Plant 2).
4. Generates an AC power prediction.
5. Returns the predicted value as a JSON response.

Example response:

```json
{
  "predicted_ac_power": 829.44,
  "plant": 2
}
```

The value shown above is only an illustrative example, not an actual model result.

### Live Weather Integration

The application uses the **Open-Meteo API** to retrieve weather information for a selected location.

The live prediction workflow is:

1. The user selects or enters a location.
2. The frontend retrieves the relevant weather information.
3. Ambient temperature and irradiation-related inputs are prepared.
4. Module temperature is estimated, and the configured inverter key is supplied.
5. Time-based features are derived from the selected date and time.
6. The prepared inputs are sent to the Flask `/predict` endpoint.
7. The backend uses the trained Random Forest model to predict AC power.
8. The prediction is displayed in the frontend.

Some model inputs are estimated or fixed because they are not directly available from the weather API. Consequently, live predictions are estimates under the selected model configuration.

### Manual Prediction

The manual prediction interface allows users to provide the model's input features directly.

The inputs are sent to the same Flask prediction endpoint, and the resulting AC power prediction is displayed by the application.

---

## ⚙️ Installation and Setup

### Prerequisites

- Python installed on the system
- A modern web browser
- Git
- Git LFS to retrieve the saved model when cloning the repository

### 1. Clone the Repository

```bash
git clone https://github.com/Shivansh1236/Solar.git
cd Solar
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Retrieve the Model

The saved model is tracked using Git LFS because of its large file size.

```bash
git lfs install
git lfs pull
```

Ensure that `random_forest_model.pkl` contains the actual model file and not an LFS pointer before starting the backend.

### 4. Start the Backend

From the project root directory, run:

```bash
python backend/app.py
```

The Flask server is expected to run at:

```text
http://127.0.0.1:5000
```

Keep the terminal running while using the prediction functionality.

### 5. Open the Frontend

Open `frontend/index.html` in a web browser.

The frontend interface may load independently, but prediction requests require the Flask backend to be running on the same computer.

---

## 💡 Key Insights

- Solar irradiation is the dominant feature in the trained Random Forest model.
- Random Forest outperformed Linear Regression and Decision Tree on the three reported test metrics.
- The model achieved an R² score of 0.9856 on the current random test split.
- Combining a trained regression model with a Flask API makes predictions accessible through a web interface.
- Weather API integration provides a way to prepare estimated environmental inputs for live prediction.

---

## 🔮 Future Improvements

- Evaluate the model using chronological train-test splitting to assess performance on future timestamps.
- Validate predictions on unseen inverters and different operating conditions.
- Improve module-temperature estimation using additional sensor measurements.
- Deploy the frontend and backend for public access.
- Add prediction history and downloadable prediction results.
- Perform further testing across different weather conditions and irradiation levels.

---

## 👨‍💻 Author

**Minor Project Team**  
Punjab Engineering College, Chandigarh
