#Data Probability and Prediction
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
#No need from jupyter lab setup, now on vscode

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

#Checking old page error percentage in comparison to new page
def calc_p_new(df): #Conver rate for old
    """
    The function calculates the proportion of new pages that have a successful converted rate
    """
    p_new_succ = df.query('landing_page == "new_page" and converted == 1').shape[0]
    p_new = df.query('landing_page == "new_page"').shape[0]
    prop_p_new = p_new_succ/p_new
    return prop_p_new

#compute proportion of new pages with successful convertion
p_new_prop = calc_p_new(df2)
print('p_new under sample  : {:.4f} %'.format(100.0*p_new_prop))

# H0: assumed that the nul p_new and p_old converted success rates are equal.
p_new_null = df2.converted.mean()
print('p_new under the assumed H0 conditions: {:.4f}%'.format(100.0*p_new_null))



def calc_p_old(df): #Convert rate for new
    """
    The function calculates the proportion of old pages that have a successful converted rate
    """
    p_old_succ = df.query('landing_page == "old_page" and converted == 1').shape[0]
    p_old = df.query('landing_page == "old_page"').shape[0]
    prop_p_old = p_old_succ/p_old
    return prop_p_old

#Finding proportion of old pages with successful convertion
p_old_prop = calc_p_old(df2)
print('p_old under sample : {:.4f} %'.format(100.0*p_old_prop))

# H0: assumed that the nul p new and p old converted success rates are equal.
p_old_null = p_new_null
print('p_old under the assumed H0 conditions: {:.4f}%'.format(100.0*p_old_null))

# Size of new 
sample_size_new_page = df2.query('landing_page == "new_page"').shape[0]
print('Sample size new_page: {}'.format(sample_size_new_page))

# Size of old 
sample_size_old_page = df2.query('landing_page == "old_page"').shape[0]
print('Sample size old_page: {}'.format(sample_size_old_page)) 

# H0 : new page and old pag data
new_page_converted = np.random.choice([1,0], size=sample_size_new_page, p=[p_new_null,1-p_new_null])
old_page_converted = np.random.choice([1,0], size=sample_size_old_page, p=[p_old_null, 1-p_old_null])

def calc_p(array): #NumPy takes the mean of array
    p = array.mean()
    return p
#Calculating mean for H0 and H1:
p_new_null_mean = calc_p(new_page_converted)
p_old_null_mean = calc_p(old_page_converted)

p_diff = p_new_prop - p_old_prop

p_diff_sim = p_new_null_mean - p_old_null_mean

print('No simulated p_diff (under the sample): {:.4f} %'.format(100.0*p_diff))
print('Simulated samples p_diff (under H0 assumed conditions): {:.4f}%'.format(100.0*p_diff_sim))

# Simulating the null values with 10000 samples 
p_diffs = []

for _ in range(10000):
    new = np.random.choice([1,0], size=sample_size_new_page, p=[p_new_null,1-p_new_null])
    old = np.random.choice([1,0], size=sample_size_old_page, p=[p_old_null,1-p_old_null])
    p_new_mean = calc_p(new)
    p_old_mean = calc_p(old)
    p_diffs.append(p_new_mean - p_old_mean)
    
p_diffs = np.array(p_diffs)
p_diffs_sim10000 = p_diffs.mean()
print('Mean: {:.4f}%\nStd: {:.4f}'.format(p_diffs_sim10000,p_diffs.std()))

#Plotting
plt.figure(figsize=(12,5))
plt.hist(p_diffs)
plt.axvline(p_diff,c='r',lw=4,label='Dataset Proportion/Mean')
plt.axvline(p_diff_sim, c='c', lw=4, label='Simulated < 10000')
plt.axvline(p_diffs_sim10000, c='m', lw=4, label='Simulated = 10000')
plt.xlabel('Converted P_diff')
plt.ylabel('Frequency')
plt.title('Histogram of P_diff Null Distribution')
plt.legend();

#Mean of mean and histogram value, checks to see if rejected
print('No simulated p_diff (under the sample): {:.4f} %'.format(100.0*p_diff))
print('Simulated 10000 samples p_diff (under H0 assumed conditions): {:.4f}%'.format(100.0*p_diffs_sim10000))

prop_greater_pdiffs = p_diffs_sim10000 - p_diff
print('Proportion greater {:.4f}%'.format(100.0*prop_greater_pdiffs))

p_val = (p_diffs > p_diff).mean()
print('Pval: {:.4f}'.format(p_val))


# Getting back the sample sizes for the data and success rate mean
convert_old = df2.query('landing_page == "old_page" and converted == 1').shape[0]
convert_new = df2.query('landing_page == "new_page" and converted == 1').shape[0]
n_old = sample_size_old_page
n_new = sample_size_new_page


