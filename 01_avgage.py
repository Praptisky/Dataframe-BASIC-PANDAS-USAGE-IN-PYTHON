"""
Simple pandas example:
- Creates a DataFrame
- Displays it
- Calculates the average age
"""
import pandas as pd
data ={
    "Name" : ["Adam", "Prapti", "Ankita", "John"],
    'Age' : [15, 16, 15, 14 ],
    'City' : ['Bhopal', 'Nagpur', 'Pune', 'Gavrada']
}

df = pd.DataFrame(data)
print('Dataframe:\n',df)

avgage = df['Age'].mode()
print('Average age is',avgage)

median = df['Age'].median()
print('Median age is', median)

mod = df['Age'].mode()
mode = mod.iloc[0] if not mod.empty else None
print('Mode of age is', mode)