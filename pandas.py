import pandas as p
c=p.Series([1,2,3,4,5])
print(c)
print(type(c))
print(c.values)
df=p.DataFrame({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]})
print(df)
df=p.DataFrame({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]},index=[1,2,3])
print(df)
df1=p.DataFrame([[1,4,7],[2,5,8],[3,6,9]],index=[1,2,3],columns=['a','b','c'])
print(df1)
print(df.loc[3,:])
print(df.loc[:,'b'])
print(df.loc[:,'c'])
print( df.iloc[2,:])
print(df.descibe())
print(df.info())
df2=p.DataFrame([[1,4,4],[2,5,8],[5,6,1]],index=[1,2,3],columns=['a','b','c'])
print(df2)
print(df2.drop_duplicates(subset='a')) //it prioritize the row a
df.to_csv('C:/Users/Yogesh Tripathi/Desktop/pandas_data.csv')  //create files on desktop
df.to_csv('C:/Users/Yogesh Tripathi/Desktop/pandas_data.csv',index=False)   //creates file on desktop without index
data=p.read_csv('C:/Users/Yogesh Tripathi/Desktop/pandas_data.csv')
print(data)
