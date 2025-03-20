# 📊 Confusion Matrix: Understanding Model Performance

A **Confusion Matrix** is a performance evaluation metric for classification models. It provides a summary of prediction results by comparing actual vs. predicted values.

## What is a Confusion Matrix?
A **Confusion Matrix** is a table used to describe the performance of a classification algorithm. It consists of **True Positives (TP)**, **False Positives (FP)**, **True Negatives (TN)**, and **False Negatives (FN)**.

### **Example Confusion Matrix for Binary Classification**
| Actual \ Predicted | Positive (1) | Negative (0) |
|--------------------|-------------|-------------|
| **Positive (1)**  | TP (True Positive)  | FN (False Negative)  |
| **Negative (0)**  | FP (False Positive) | TN (True Negative) |

---

## Confusion Matrix Metrics
From the confusion matrix, we can derive key classification metrics:

1️⃣ **Accuracy** = (TP + TN) / (TP + TN + FP + FN)  
2️⃣ **Precision** (Positive Predictive Value) = TP / (TP + FP)  
3️⃣ **Recall** (Sensitivity) = TP / (TP + FN)  
4️⃣ **F1 Score** = 2 × (Precision × Recall) / (Precision + Recall)  

---


### **Import Necessary Libraries to implement confusion matrix in Python**
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
