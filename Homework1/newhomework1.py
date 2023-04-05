# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv('Starbucks satisfactory survey.csv')

#這個數據集有多少個觀測值和變數？
print("Number of Observations: ", df.shape[0])
print("Number of Variables: ", df.shape[1])
print("##################################################################################")

#有多少人參與了這個調查？
print("Number of Respondents: ", df["Gender"].count())
print("##################################################################################")

#這個數據集中最常見的年齡層是多少？
#年齡層的眾數
print("Most Common Age Group: ", df["Age"].mode().values[0])
print("##################################################################################")

#在這個數據集中，參與者最多的職業是什麼？
print("Most Common Occupation: ", df["Job"].mode().values[0])
print("##################################################################################")

#在這個數據集中，哪個地區的參與者最多？
#參與者最多的地區
print("Region with Most Respondents: ", df["Location"].mode().values[0])
print("##################################################################################")

#我想要知道學生擁有星巴克會員的名單
filt = (df['Job'] == 'Student')
print(df.loc[filt, ['Job', 'VisitFrequency', 'EnjoyType']])
print("##################################################################################")

#在所有客戶中，男性和女性客戶的比例是多少？
gender_count = df['Gender'].value_counts(normalize=True)
print(f"Male customers make up {gender_count['Male']*100:.2f}% and female customers make up {gender_count['Female']*100:.2f}% of respondents.")
print("##################################################################################")

#年齡最大的客戶是誰？年齡最小的客戶是誰？
#oldest = df.loc[df['Age'].idxmax()]
#youngest = df.loc[df['Age'].idxmin()]
#print(f"The oldest customer is {oldest['Name']} ({oldest['Age']} years old) and the youngest customer is {youngest['Name']} ({youngest['Age']} years old).")

print("##################################################################################")

#受訪者中各種收入水平的比例是多少？
income_count = df['AannualIncome'].value_counts(normalize=True)
print(income_count)

print("##################################################################################")

#訪問星巴克的頻率和客戶的收入水平之間是否存在關聯？
freq_income = df[['VisitFrequency', 'AannualIncome']]
freq_income['AannualIncome'] = pd.Categorical(freq_income['AannualIncome'], categories=['Below RM25,000', 'RM25,000 - RM50,000', 'RM50,000 - RM100,000', 'Above RM100,000'])
freq_income_grouped = freq_income.groupby('AannualIncome').mean()
print(freq_income_grouped)
print("##################################################################################")
