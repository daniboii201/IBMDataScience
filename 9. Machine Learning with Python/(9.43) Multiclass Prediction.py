import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd

### Utility Function 

# This function plots a different decision boundary. 
plot_colors = "ryb"
plot_step = 0.02

def decision_boundary (X,y,model,iris, two=None):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))
    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z,cmap=plt.cm.RdYlBu)
    
    if two:
        cs = plt.contourf(xx, yy, Z,cmap=plt.cm.RdYlBu)
        for i, color in zip(np.unique(y), plot_colors):
            
            idx = np.where( y== i)
            plt.scatter(X[idx, 0], X[idx, 1], label=y,cmap=plt.cm.RdYlBu, s=15)
        plt.show()
  
    else:
        set_={0,1,2}
        print(set_)
        for i, color in zip(range(3), plot_colors):
            idx = np.where( y== i)
            if np.any(idx):

                set_.remove(i)

                plt.scatter(X[idx, 0], X[idx, 1], label=y,cmap=plt.cm.RdYlBu, edgecolor='black', s=15)


        for  i in set_:
            idx = np.where( iris.target== i)
            plt.scatter(X[idx, 0], X[idx, 1], marker='x',color='black')

        plt.show()

# This function will plot the probability of belonging to each class; each column is the probability of belonging to 
# a class and the row number is the sample number.
def plot_probability_array(X,probability_array):

    plot_array=np.zeros((X.shape[0],30))
    col_start=0
    ones=np.ones((X.shape[0],30))
    for class_,col_end in enumerate([10,20,30]):
        plot_array[:,col_start:col_end]= np.repeat(probability_array[:,class_].reshape(-1,1), 10,axis=1)
        col_start=col_end
    plt.imshow(plot_array)
    plt.xticks([])
    plt.ylabel("samples")
    plt.xlabel("probability of 3 classes")
    plt.colorbar()
    plt.show()

# In ths lab we will use the  iris dataset,  it consists of three different types of irises’ (Setosa y=0, Versicolour y=1, 
# and Virginica y=2), petal and sepal length, stored in a 150x4 numpy.ndarray.
# The rows being the samples and the columns: Sepal Length, Sepal Width, Petal Length and Petal Width.
# The following plot uses the second two features:
pair=[1, 3]
iris = datasets.load_iris()
X = iris.data[:, pair]
y = iris.target
np.unique(y)

plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu)
plt.xlabel("sepal width (cm)")
plt.ylabel("petal width")


### Softmax Regression

lr = LogisticRegression(random_state=0).fit(X, y)
# We generate the probability using the method predict_proba:
probability=lr.predict_proba(X)

# We can plot the probability of belonging to each class; each column is the probability of belonging to a class and the 
# row number is the sample number.
plot_probability_array(X,probability)

# Here, is the output for the first sample:
probability[0,:]
# We see it sums to one.
probability[0,:].sum()

# We can apply the argmax function.
np.argmax(probability[0,:])
# We can apply the argmax function to each sample.
softmax_prediction=np.argmax(probability,axis=1)
softmax_prediction

# We can verify that sklearn does this under the hood by comparing it to the output of the method predict.
yhat =lr.predict(X)
accuracy_score(yhat,softmax_prediction)
# We can't use Softmax regression for SVMs, Let's explore two methods of Multi-class Classification that we can apply to SVM.


### SVM

# Sklean performs Multi-class Classification automatically, we can apply the method and calculate the accuracy. 
# Train a SVM classifier with the `kernel` set to `linear`, `gamma` set to `0.5`, and the `probability` parameter set to `True`,
# then train the model using the `X` and `y` data.
model = SVC(kernel='linear', gamma=.5, probability=True)
model.fit(X,y)

# Find the 'accuracy_score' on the training data.
yhat = model.predict(X)
accuracy_score(y,yhat)

# We can plot the decision_boundary.
decision_boundary (X,y,model,iris)


### One vs. All (One-vs-Rest) 

## Train Each Classifier

#dummy class
dummy_class=y.max()+1
#list used for classifiers 
my_models=[]
#iterate through each class
for class_ in np.unique(y):
    #select the index of our  class
    select=(y==class_)
    temp_y=np.zeros(y.shape)
    #class, we are trying to classify 
    temp_y[y==class_]=class_
    #set other samples  to a dummy class 
    temp_y[y!=class_]=dummy_class
    #Train model and add to list 
    model=SVC(kernel='linear', gamma=.5, probability=True)    
    my_models.append(model.fit(X,temp_y))
    #plot decision boundary 
    decision_boundary (X,temp_y,model,iris)

# For each sample we calculate the  probability of belonging to each class, not including the dummy class.
probability_array=np.zeros((X.shape[0],3))
for j,model in enumerate(my_models):

    real_class=np.where(np.array(model.classes_)!=3)[0]

    probability_array[:,j]=model.predict_proba(X)[:,real_class][:,0]

# Here, is the probability of belonging to each class for the first sample.
probability_array[0,:]

# As each is the probability of belonging to the actual class and not the dummy class, it does not sum to one. 
probability_array[0,:].sum()

# We can plot the probability of belonging to the class. The row number is the sample number.
plot_probability_array(X,probability_array)

# We can apply the argmax function to each sample to find the class.
one_vs_all=np.argmax(probability_array,axis=1)
one_vs_all

# We can calculate the accuracy. 
accuracy_score(y,one_vs_all)

# We see the accuracy is less than the one obtained by sklearn, and this is because for SVM, sklearn uses one vs one; let's verify it by comparing the outputs. 
accuracy_score(one_vs_all,yhat)


### One vs One 

# Here, we list each class.
classes_=set(np.unique(y))
classes_

# Determine the number of classifiers:
K=len(classes_)
K*(K-1)/2

# We then train a two-class classifier on each pair of classes. We plot the different training points for each of the two classes. 
pairs=[]
left_overs=classes_.copy()
#list used for classifiers 
my_models=[]
#iterate through each class
for class_ in classes_:
    #remove class we have seen before 
    left_overs.remove(class_)
    #the second class in the pair
    for second_class in left_overs:
        pairs.append(str(class_)+' and '+str(second_class))
        print("class {} vs class {} ".format(class_,second_class) )
        temp_y=np.zeros(y.shape)
        #find classes in pair 
        select=np.logical_or(y==class_ , y==second_class)
        #train model 
        model=SVC(kernel='linear', gamma=.5, probability=True)  
        model.fit(X[select,:],y[select])
        my_models.append(model)
        #Plot decision boundary for each pair and corresponding Training samples. 
        decision_boundary (X[select,:],y[select],model,iris,two=True)

pairs # As we can see, our data is left-skewed, containing more "5" star reviews. 

# Here, we are plotting the distribution of text length.
majority_vote_array=np.zeros((X.shape[0],3))
majority_vote_dict={}
for j,(model,pair) in enumerate(zip(my_models,pairs)):

    majority_vote_dict[pair]=model.predict(X)
    majority_vote_array[:,j]=model.predict(X)

# In the following table, each column is the output of a classifier for each pair of classes and the output is the prediction:
pd.DataFrame(majority_vote_dict).head(10)

# To perform classification on a sample, we perform a majority vote, that is, select the class with the most predictions. 
# We repeat the process for each sample. 
one_vs_one=np.array([np.bincount(sample.astype(int)).argmax() for sample  in majority_vote_array]) 
one_vs_one

# We calculate the accuracy:
accuracy_score(y,one_vs_one)

# If we compare it to `sklearn`, it's the same! 
accuracy_score(yhat,one_vs_one)