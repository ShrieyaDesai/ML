#Program to Implement a Decision TREE -- Classifier Problem

print('PROGRAM To Implement a Decision Tree AND to DISPLAY IT') 
from sklearn import datasets 
import pandas as pd 

iris=datasets.load_iris() 
# df will fold dataset as a table 
df=pd.DataFrame( 
iris.data, 
columns=iris.feature_names 
) 

#labels are assigned to df[target] table or array 
df['target']=pd.Series( 
iris.target 
) 

from sklearn.model_selection import train_test_split 
# Train Test Split Ratio 
df_train,df_test=train_test_split(df,test_size=0.3) 
df['target_names']=df['target'].apply(lambda y:iris.target_names[y]) 
print('Number of Training samples') 
print(df_train.shape[0]) 
print('Number of Testing samples') 
print(df_test.shape[0]) 


#Importing Decision Tree Classifier 
from sklearn.tree import DecisionTreeClassifier 
clf=DecisionTreeClassifier()
x_train=df_train[iris.feature_names] 
x_test=df_test[iris.feature_names] 
y_train=df_train['target'] 
y_test=df_test['target'] 
#Training Decision Tree Classifier 
clf.fit(x_train,y_train) 
#Testing the data 
y_test_pred=clf.predict(x_test) 
print('Class of Testing Samples') 
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
feature_names=iris.feature_names, 
class_names=iris.target_names, 
filled=True) 
fig.savefig("decistion_tree.png")
