import pandas as pd
% matplotlib inline

df_census[''].value_counts().plot(kind='bar');
df_census[''].value_counts().plot(kind='pie', figsize(8,8));
df_cancer.plot(x='', y='', kind='scatter');
df_cancer[''].plot(kind='box');



# import and load data
import pandas as pd
% matplotlib inline

df = pd.read_csv('powerplant_data_edited.csv')
df.head()

df.plot(x='Temperature', y='Energy Output', kind='scatter');

df[''].plot(kind='hist')


df_m = df[df['diagnosis'] == 'M']


187:199


df_a = df_census[df_census['income'] == ' >50K']
df_b = df_census[df_census['income'] == ' <=50K']


ind = df_a['education'].value_counts().index
df_a['education'].value_counts()[ind].plot(kind='bar');
df_b['education'].value_counts()[ind].plot(kind='bar');


ind = df_a['workclass'].value_counts().index
df_a['workclass'].value_counts()[ind].plot(kind='pie', figsize=(8,8));
df_a['age'].hist()
df_b['age'].hist()



