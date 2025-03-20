# Decision Tree Implementation on Hitters & Heart Datasets

This repository contains **Decision Tree** implementations on two datasets:
1. **Hitters Dataset** - Predicting a player's salary based on baseball performance.
2. **Heart Disease Dataset** - Predicting the likelihood of heart disease based on medical features.

---

## 📌 Dataset 1: Hitters (Baseball Player Salaries)
The **Hitters dataset** contains statistics for professional baseball players and their respective salaries.

### **🔹 Features:**
| Feature Name  | Description |
|--------------|------------------------------------------------|
| `AtBat`      | Number of times at bat in a season |
| `Hits`       | Number of hits |
| `HmRun`      | Number of home runs |
| `Runs`       | Number of runs |
| `RBI`        | Runs Batted In |
| `Walks`      | Number of walks |
| `Years`      | Number of years played in major leagues |
| `CAtBat`     | Career at-bats |
| `CHits`      | Career hits |
| `CHmRun`     | Career home runs |
| `CRuns`      | Career runs |
| `CRBI`       | Career Runs Batted In |
| `CWalks`     | Career walks |
| `League`     | League the player belongs to (A or N) |
| `Division`   | Player's division (E or W) |
| `Salary`     | **Target Variable** (Player's salary in thousands) |



## 📌 Dataset 2: Heart Disease 
The **Heart Disease Dataset** is a commonly used dataset for heart disease classification. The goal is to predict whether a patient has heart disease (`1`) or not (`0`).

### **🔹 Features in the Dataset**
| Feature Name  | Description |
|--------------|-------------------------------------------|
| `Age`        | Age of the patient |
| `Sex`        | Gender (0 = Female, 1 = Male) |
| `ChestPain`  | Type of chest pain (0-3 categorical) |
| `RestBP`     | Resting blood pressure (in mm Hg) |
| `Chol`       | Serum cholesterol level (mg/dL) |
| `FBS`        | Fasting blood sugar (> 120 mg/dL, 1 = True, 0 = False) |
| `RestECG`    | Resting electrocardiogram results (0-2 categorical) |
| `Thalach`    | Maximum heart rate achieved |
| `Exang`      | Exercise-induced angina (1 = Yes, 0 = No) |
| `Oldpeak`    | ST depression induced by exercise |
| `Slope`      | Slope of the peak exercise ST segment (0-2 categorical) |
| `Ca`         | Number of major vessels (0-4) |
| `Thal`       | Thalassemia (0-3 categorical) |
| `Target`     | **Target Variable** (1 = Heart disease, 0 = No heart disease) |

---
