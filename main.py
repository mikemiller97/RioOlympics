import pandas as pd
import numpy as np
import datetime as DT

df = pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/athletes.csv')

# Nations value
#print(df['nationality'].value_counts()[:30])

#print total medals
gold = df.groupby('nationality').sum()['gold']
silver = df.groupby('nationality').sum()['silver']
bronze = df.groupby('nationality').sum()['bronze']

total_medals = gold + silver + bronze

#print(total_medals)
#print(gold['IND'])

#Age now
#now = pd.Timestamp(DT.datetime.now())

#Age as they were in 2016!!
now = pd.Timestamp(DT.datetime(2016, 10, 5, 18, 00))

df['dob'] = pd.to_datetime(df['dob'])
df['dob'] = df['dob'].where(df['dob'] < now, df['dob'] - np.timedelta64(100, 'Y'))
df['age'] = (now - df['dob']).astype('<m8[Y]')
print(df)

print("Something to make this different.")