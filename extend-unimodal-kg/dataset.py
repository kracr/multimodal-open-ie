import pandas as pd

df1=pd.read_csv('FIFAWorldCup - Metadata.csv')
# df2=pd.read_csv('GlobalWarming - Metadata.csv')
# df3=pd.read_csv('Earthquake - Metadata.csv')
# df=pd.concat([df1,df2,df3])

# import re
# # EKG = Graph()
# # df = pd.read_csv('dataset.csv')
# df['Language+ID'] = df['Language+ID'].apply(lambda x: re.sub(r'[0-9]', '',x))
# df['Language+ID'] = df['Language+ID'].apply(lambda x: re.sub(r'\([^)]*\)', '',x))
# df['Event'] = df['Event'].apply(lambda x: re.sub(r'\([^)]*\)', '',x).strip())
# df.rename(columns = {'Language+ID':'Language'}, inplace = True)


# df=df.drop(['Class','Weight'], axis=1)
# df=df.sample(frac=1)
# df=df.replace(to_replace="Global Warming",value="Climate Change")
# df.to_csv('dataset.csv', index=False)

df=pd.read_csv('dataset.csv')

print(df['Language'].unique())
