# 🌸 Iris Dataset Exploration using Scikit-learn and Pandas

##  Description

This Python script demonstrates how to load, explore, and split the famous **Iris dataset** using the `scikit-learn` and `pandas` libraries. 
The Iris dataset is a classic dataset in machine learning and statistics, consisting of 150 samples from three species of iris flowers — *Setosa*, *Versicolor*, and *Virginica*.

---

## 📁 Dataset Information

- **Features (columns):**
  - sepal length (cm)
  - sepal width (cm)
  - petal length (cm)
  - petal width (cm)
- **Target Classes:**
  - 0: setosa
  - 1: versicolor
  - 2: virginica

---

##  Requirements

Ensure you have the following Python packages installed:
```bash
pip install scikit-learn pandas
```

---

## 🧠 What the Script Does

### 1. **Load the Dataset**
```python
from sklearn import datasets
iris = datasets.load_iris()
```
Loads the built-in Iris dataset from `scikit-learn`.

### 2. **Print Dataset Description**
```python
print(iris.DESCR)
```
Displays a full summary of the dataset including feature information and statistics.

### 3. **Convert to DataFrame**
```python
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = pd.Series(iris.target)
df['target_names'] = df['target'].apply(lambda y: iris.target_names[y])
```
Converts the dataset into a **pandas DataFrame** for easier analysis and adds:
- a `target` column [output column] with numeric class labels
- a `target_names` column with the flower species names

### 4. **Display Samples**
```python
df.head(5)        # First 5 rows
df.sample(5)      # 5 random rows
```
You can print the no.of rows using `.head()` and `.sample()`.
head() -> first few rows
sample() -> randow few rows 
### 5. **Split the Dataset**
```python
from sklearn.model_selection import train_test_split
df_train, df_test = train_test_split(df, test_size=0.3)
```
Splits the data into **70% training** and **30% testing**.

### 6. **Show Dataset Sizes**
```python
print(df.shape[0])        # Total samples
print(df_train.shape[0])  # Training samples
print(df_test.shape[0])   # Testing samples
```
Displays the number of records in the full, training, and testing sets.

---

## 📊 Sample Output

The output shows:
- Description of the dataset
- A table of first 5 and random 5 samples
- Size of training and testing data
- First 5 samples from both training and testing sets

---

##  Usage

Simply run the script using Python:
```bash
python iris_dataset_analysis.py
```

---

