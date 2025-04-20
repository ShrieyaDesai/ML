from sklearn import datasets
import pandas as pd

print('THIS IS  THE PROGRAM TO ACCESS  IRIS DATASET')
iris=datasets.load_iris()
print(" To print the description of Iris Dataset")
print(iris.DESCR)

print('\n\n\n\n')

# df will fold dataset as a table
df=pd.DataFrame(
   iris.data,
   columns=iris.feature_names
   )

#labels are assigned to df[target] table or array
df['target']=pd.Series(
    iris.target
   )

df['target_names']=df['target'].apply(lambda y:iris.target_names[y])

print(iris.target_names)
print('To display First 5 samples')

# df.head(5) will return the first five samples in the dataset
print(df.head(5))
print(df.head(15))

print('To display randomply 5 samples')
#df.sample(5) will return randomly five samples from the dataset
print(df.sample(5))

from sklearn.model_selection import train_test_split
df_train,df_test=train_test_split(df,test_size=0.3)

print("total samples: ")
print(df.shape[0])

print('train samples: ', df_train.shape[0])
print('test samples: ',df_test.shape[0])