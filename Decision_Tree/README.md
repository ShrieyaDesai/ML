# Decision Tree

A **Decision Tree** is a supervised learning algorithm used for classification and regression tasks. It works by splitting data into branches based on feature conditions, leading to a final decision.

---

## 📌 Decision Tree Structure
# Decision Tree

A **Decision Tree** is a supervised learning algorithm used for classification and regression tasks. It works by splitting data into branches based on feature conditions, leading to a final decision.




## Steps to Implement a Decision Tree

### **1.  Import Libraries**
### **2.  Load Dataset**
### **3.  Create and Train the Model by calling the DecisionTreeClassifier() function**
### **4.  Make Predictions with train data**
### **5. Evaluate the Model based on its accuracy**
### **6. Visualize the Decision Tree**


# Some definitions of functions in the code 


**df.select_dtypes(include=['object'])**  → Selects columns that contain text (categorical) data.

**.columns** → Gets the names of those columns.
Prints out the categorical column names so you can see which ones need conversion.

**pd.get_dummies(df, drop_first=True):**


*   Creates new columns for each unique category (One-Hot Encoding).
*   Replaces text values with 0s and 1s.


*  Removes one category (drop_first=True) to avoid redundancy (Dummy Variable Trap)




these are the main changes made between iris dataset to hitters dataset
*italicized text*
