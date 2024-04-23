import pandas as pd

dict={"Name":["Garv","Hriday","Hriday","Hriday","Hriday","Hriday","Hriday","Hriday"],
      "Roll no":[20,54,67,88,45,23,76,35],
      "Score":[100,34,245,23,45,23,32,242],
      "Class":["Shreya","","20","IT","2005","","",""]}

gd=pd.DataFrame(dict)
gd.info()
df=gd[['Score','Class']]
m=gd['Score'].mean()
print(df)
print(m)