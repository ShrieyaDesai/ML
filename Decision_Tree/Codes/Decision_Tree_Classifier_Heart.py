#Program To Implement a Decision Tree -- Regression Problem
print('Program To Implement a Decision Tree  -- Classifier Problem - Heart Dataset')

#from sklearn import datasets
import pandas as pd

df = pd.read_csv("heart.csv")
print(df.columns)

#we identify the target varibale [output variable ] -- as per the column names given we can

df = df.dropna() #drop rows that have NA values

print("Dataset Size:", df.shape)

# Print number of rows and columns separately
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])
print("Total Dataset Size (Total Elements):", df.size)

# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
print("Categorical Columns:", categorical_cols)

# Convert categorical columns to numeric using One-Hot Encoding
df = pd.get_dummies(df, drop_first=True)  # Converts categorical values into numeric


from sklearn.model_selection import train_test_split

# Identify the target column (target) and feature columns
X = df.drop(columns=['target'])  # Features are all columns except target
print('Feature values:  ',X.columns)

#since target column is the target/ output variable let us keep all columns n drop only target

#  create an empty column named target for output variable
Y = df['target']  # Target variable

# Train Test Split Ratio
X_train,X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)


print('Number of Training samples of features')
print(X_train.shape[0])
print('Number of Testing samples of features')
print(X_test.shape[0])

print('Number of Training samples of target')
print(Y_train.shape[0])
print('Number of Testing samples of target')
print(Y_test.shape[0])

#Importing Decision Tree Classifier
from sklearn.tree import DecisionTreeRegressor

clf = DecisionTreeRegressor()    #since heart disease prediction -- 1 if present 0 if absent 
clf.fit(X_train, Y_train) #Training Decision Tree Classifier


y_test_pred = clf.predict(X_test)
print('Predicted Disease result of Testing Samples:')
print(y_test_pred)


#To display the decision tree in command shell
from sklearn.tree import export_text
from sklearn import tree
from matplotlib import pyplot as plt

text_representation = tree.export_text(clf)
print(text_representation)
with open("decistion_tree.log", "w") as fout:
  fout.write(text_representation)
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(clf,
feature_names=X.columns,
filled=True)
fig.savefig("decistion_tree.png")

plt.show()