import pandas as pd

df = pd.read_csv("ideal_weight.csv")
df.columns = ['id', 'sex', 'actual', 'ideal', 'diff']
# better way to strip characters?
df['sex'] = df['sex'].map(lambda x: x.lstrip('\'').rstrip('\''))
del df['id']








print df

#Plot the distributions of actual weight and ideal weight.
