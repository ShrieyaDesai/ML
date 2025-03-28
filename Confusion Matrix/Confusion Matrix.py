from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
# actual values
#A=1= Positive Class , B=0=Negative Class
actual = [1,0,0,1,0,1,1,1,0,1,0]
# predicted values
predicted = [1,0,0,1,0,0,0,1,0,0,1]

#actual = [1,0,0,1,0,1,1,1,0,1,0,1,1,1,1,0,0,1]
# predicted values
#predicted = [1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0] 

# confusion matrix
matrix = confusion_matrix(actual,predicted, labels=[1,0])
print('Confusion matrix : \n',matrix)
acc=accuracy_score(actual,predicted)
print('Accuracy = ',acc)
matrix = classification_report(actual,predicted,labels=[1,0])
print('Classification Report \n')
print(matrix)
fpr, tpr , _= metrics.roc_curve(actual, predicted) #create ROC curve
print('fpr = ',fpr)
print('tpr = ',tpr)
plt.plot(fpr,tpr)
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
