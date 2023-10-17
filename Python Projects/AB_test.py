#Data Probability and Prediction
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
%matplotlib inline

random.seed(42)

#Reads in data set
df = pd.read_csv('ab_data.csv')
df.head(10)

# Values in columns and common
print('Groups: {}'.format(df['group'].unique()))
print('Landing pages: {}'.format(df['landing_page'].unique()))
print('Converted: {}'.format(df['converted'].unique()))

df.info()

# obtaining unique number of values of user_id column
unique_users_num = df.user_id.nunique()
print('Unique users: {}'.format(unique_users_num)) 
#Converted users
users_conv = df.query('converted == 1').user_id.nunique()
print('Proportion of users converted : {:.3f} %'.format(100.0*users_conv/unique_users_num))

df_new_page = df.query('landing_page == "new_page"')
df_new_page_not_treatment = df_new_page.query('group != "treatment"')

# parsing control and old_page 
df_old_page = df.query('landing_page == "old_page"')
df_old_page_not_control = df_old_page.query('group != "control"')

new_page_not_treatment = df_new_page_not_treatment.shape[0]
old_page_not_control = df_old_page_not_control.shape[0]

#Data Visualization
print('New page not allignes with treatment {} times'.format(new_page_not_treatment))
print('Old page allignes with treatment (not control) {} times'.format(old_page_not_control)) 
print('Treatment not alligned with new_page {} times'.format(new_page_not_treatment+old_page_not_control))

#rows dropped that do not allign new_page w/ treatment and old_page w/ control High
df2 = df.drop(df_new_page_not_treatment.index).copy()
df2.drop(df_old_page_not_control.index, inplace=True)
print('df2 should have: {} rows\n'.format(df.shape[0]-(new_page_not_treatment+old_page_not_control)) )
df2.info()

#Checking for unique ids
print('Unique user id in df2: {}'.format(df2.user_id.nunique()))

# Checking for the duplicated user_id
dup_id = df2.user_id.value_counts().argmax()
print('Duplicated user_id: {}'.format(dup_id))
df2.query('user_id == {}'.format(dup_id)).head()

#Removing it
df2.drop_duplicates('user_id',inplace=True)
df2.info()

#Probabibility Calculation
conv_ind = df2.query('converted == 1')
num_conv = conv_ind.shape[0]
print('Probability of converted individual regardless of the page: {:.4f}'.format(num_conv/df2.shape[0]))

#Control Group Conversion Rate
control_conv = conv_ind.query('group == "control"').shape[0]
control_group = df2.query('group=="control"').shape[0]
print('Probability of CONTROL page converted individual: {:.4f}'.format(control_conv/control_group))

#Treatment Group Conversion Rate
treatment_conv = conv_ind.query('group == "treatment"').shape[0]
treatment_group = df2.query('group == "treatment"').shape[0]
print('Probability of TREATMENT page converted individual: {:.4f}'.format(treatment_conv/treatment_group))

#Probabibility of new page
new_page_ind = df2.query('landing_page == "new_page"').shape[0]
print('Probability and individual got the NEW PAGE: {:.4f}'.format(new_page_ind/df2.shape[0]))

