import pandas as pd
import matplotlib.pylab as plt

show_weight_dist = 'N' # Show weight distribution plot, Y or N
show_weight_diff = 'Y' # Show weight difference plot, Y or N

df = pd.read_csv("ideal_weight.csv")
df.columns = ['id', 'sex', 'actual', 'ideal', 'diff']
# better way to strip characters?
df['sex'] = df['sex'].map(lambda x: x.lstrip('\'').rstrip('\''))
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

if show_weight_dist == 'Y':
    weight_distribution()

if show_weight_diff == 'Y':
    weight_difference()
