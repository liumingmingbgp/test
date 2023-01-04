import pandas as pd
s1 = pd.Series([1,2,3], index=[1,2,3], name='A')
print(s1)
print(s1.index)
print(s1[1])
s2 = pd.Series([10,20,30], index=[1,2,3], name='B')
s3 = pd.Series([100,200,300], index=[1,2,3], name='C')
df = pd.DataFrame([s1,s2,s3])
print(df)
df2 = pd.DataFrame({
    s1.name:s1,
    s2.name:s2,
    s3.name:s3
})
print(df2)