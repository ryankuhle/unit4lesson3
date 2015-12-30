import pandas as pd
import matplotlib.pylab as plt
from sklearn.naive_bayes import GaussianNB

show_weight_dist = 'N' # Show weight distribution plot, Y or N
show_weight_diff = 'N' # Show weight difference plot, Y or N
show_predict_sex = 'Y' # Show predicted sex of 2 people, Y or N

df = pd.read_csv("ideal_weight.csv")
df.columns = ['id', 'sex', 'actual', 'ideal', 'diff']
# better way to strip characters?
df['sex'] = df['sex'].map(lambda x: x.lstrip('\'').rstrip('\''))
df['sex'] = df['sex'].astype('category')
del df['id']

def weight_distribution():
    '''
    weight_distribution
    Plot histogram of actual weight versus ideal weight.
    '''
    plt.hist(df['actual'], alpha=0.5, label="Actual Weight")
    plt.hist(df['ideal'], alpha=0.5, label="Ideal Weight")
    plt.legend(loc='upper right')
    plt.show()

def weight_difference():
    '''
    weight_difference
    Plot histogram of difference between actual weight and ideal weight.
    '''
    plt.hist(df['diff'], alpha=0.5)
    plt.show()

def predict_sex(actual, ideal, diff):
    '''
    predict_sex
    Predict sex of individual based on their actual weight, ideal weight, and difference between the two using Naive Bayes.
    '''
    #need to define training data
    classifier = GaussianNB()
    classifier.fit(features, label)
    sex = classifier.predict([[actual, ideal, diff]])
    print "The predicted sex of someone with an actual weight of %s and ideal weight of %s is %s" % (actual, ideal, sex)

if show_weight_dist == 'Y':
    weight_distribution()

if show_weight_diff == 'Y':
    weight_difference()

if show_predict_sex == 'Y':
    predict_sex(145, 160, -15)
    # predict_sex(160,145, 15)

#Fit a Naive Bayes classifier of sex to actual weight, ideal weight, and diff.
#How many points were mislabeled? How many points were there in the dataset, total?
#make sure that predict_sex function is working
