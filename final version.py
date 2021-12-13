#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

def read_contents(file):
    data = pd.read_json(file)
    df = data.copy()
    return df

def BMI(df):
    df['BMI'] = ''
    x =df['HeightCm']
    y = df['WeightKg']
    df['BMI'] = round(y/((x/100)**2),2)
    return df

def BMI_Category(df):    
    df['BMI Category'] = ''
    df.loc[df['BMI']<=18.4, 'BMI Category'] = df.loc[df['BMI']<=18.4, 'BMI Category'].replace('', 'Underweight')
    df.loc[(df['BMI']>=18.5) & (df['BMI']<=24.9), 'BMI Category'] = df.loc[(df['BMI']>=18.5) & (df['BMI']<=24.9), 'BMI Category'].replace('', 'Normal weight')
    df.loc[(df['BMI']>=25) & (df['BMI']<=29.9), 'BMI Category'] = df.loc[(df['BMI']>=25) & (df['BMI']<=29.9), 'BMI Category'].replace('', 'Overweight')
    df.loc[(df['BMI']>=30) & (df['BMI']<=34.9), 'BMI Category'] = df.loc[(df['BMI']>=30) & (df['BMI']<=34.9), 'BMI Category'].replace('', 'Moderately obese')
    df.loc[(df['BMI']>=35) & (df['BMI']<=39.9), 'BMI Category'] = df.loc[(df['BMI']>=35) & (df['BMI']<=39.9), 'BMI Category'].replace('', 'Severely obese')
    df.loc[df['BMI']>40, 'BMI Category'] = df.loc[df['BMI']>40, 'BMI Category'].replace('', 'Very severely obese')
    return df

def Health_risk(df):
    df['Health risk'] = ''
    df.loc[df['BMI']<=18.4, 'Health risk'] = df.loc[df['BMI']<=18.4, 'Health risk'].replace('', 'Malnutrition risk')
    df.loc[(df['BMI']>=18.5) & (df['BMI']<=24.9), 'Health risk'] = df.loc[(df['BMI']>=18.5) & (df['BMI']<=24.9), 'Health risk'].replace('', 'Low risk')
    df.loc[(df['BMI']>=25) & (df['BMI']<=29.9), 'Health risk'] = df.loc[(df['BMI']>=25) & (df['BMI']<=29.9), 'Health risk'].replace('', 'Enhanced risk')
    df.loc[(df['BMI']>=30) & (df['BMI']<=34.9), 'Health risk'] = df.loc[(df['BMI']>=30) & (df['BMI']<=34.9), 'Health risk'].replace('', 'Medium risk')
    df.loc[(df['BMI']>=35) & (df['BMI']<=39.9), 'Health risk'] = df.loc[(df['BMI']>=35) & (df['BMI']<=39.9), 'Health risk'].replace('', 'High risk')
    df.loc[df['BMI']>40, 'Health risk'] = df.loc[df['BMI']>40, 'Health risk'].replace('', 'Very high risk')
    return df

def save_file(df):
    df.to_csv('output.csv',index=False)
    
def count_overweight(df):
    overweight= (df['BMI Category']=='Overweight')
    overweight= overweight.sum()   
    return overweight

if __name__ == '__main__':
    input_file = 'sample.json'
    df = read_contents(input_file)
    df = BMI(df)
    df = BMI_Category(df)
    df = Health_risk(df)
    # print(result)
    print(df)
    # save result into excel
    save_file(df)
    #number of overweight people
    print('')
    print('The number of overweight people are ' + str(count_overweight(df)) )


# In[ ]:




