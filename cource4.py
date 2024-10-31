import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("dataset/Salaries.csv", index_col=0)
# print(df.shape) //عدد الصفوف و الاعمدة
# print(df.info) //بتعرض dataset
# print(df.dtypes) //نوع البيانات
# print(df.columns) //اسماء الاعمدة
# print(df.describe()) //قيم احصائية حول الداتا
# print(df["salary"].describe())//قيم احصائية حول عمود محدد

# Histogram : مخطط احصائي في المحو الافقي دائما تكون الانواع و المحور العمودي العدد

# df["yrs.since.phd"].hist(figsize=(8,10),bins=100,legend=True,xlabelsize=8,ylabelsize=8)
# df.hist(figsize=(8,10),bins=100,legend=True,xlabelsize=8,ylabelsize=8)
# plt.show()

# figsize : حجم الشاشة
# bins : التباعد بين الاعمدة
# legend :مفتاج الخريطة
# 3
# df_num=df.select_dtypes(include=["int64"]) #\\هان بعرض بس الاعمدة الي فيها int64
# print(df_num.to_string())
# corr= df_num.corr () #العلاقة بين الاعمدة

# sns.heatmap(corr.round(2), annot=True, linewidth=0.01, square=True, cmap="RdBu", linecolor="black")
# plt.show()

# 3
# print(df["sex"].value_counts(normalize=True))
# plt.xlabel("gender",labelpad=14)
# plt.ylabel("cooun of people",labelpad=14)
# plt.title("titile",y=1.02)

# df["sex"].value_counts().plot(kind="bar",figsize=(8,12),rot=0)
# plt.show()
# 3
# df_copy=df.copy()
# df_copy["sex"]=df_copy["sex"].map({"Male":0,"Female":1})
# new=df_copy[df_copy["sex"]==1]
# print(new)
# 3
# distplot: يشبه الهاستقرام و لكن بدل ما يحسب القيم بحسب النسب
# sns.displot(df["yrs.service"])
# plt.show()


# df.groupby(["rank"])["salary"].count().plot(kind="bar") #in matplotlib
# sns.set_style("darkgrid")

# sns.barplot(x="rank",y="salary" ,data=df,estimator=len)
# sns.barplot(x="rank",y="salary" ,hue="sex",data=df,estimator=len)
# sns.barplot(x="rank" ,data=df,estimator=len)
# sns.barplot(x="rank" ,hue="sex",data=df,estimator=len)
# sns.catplot(x="rank" ,hue="sex",col="discipline",kind="swarm",data=df,estimator=len)
# sns.regplot(x="yrs.service" ,y="salary",data=df)
# plt.show()
# def remove_outlier(col):
#     sorted(col)
#     Q1,Q3=col.quantile([0.25,0.75])
#     IQR=Q3-Q1
#     lower_range=Q1-(1.5*IQR)
#     upper_range=Q3+(1.5*IQR)
#     return lower_range,upper_range


# # 3
# ## outlier: القيم الشاذة ##
# # new_df=df.select_dtypes(include="int64")
# new_df=df.copy()
# lower_rang,upper_range=remove_outlier(new_df["salary"])
# new_df["salary"]=np.where(new_df["salary"]<lower_rang,lower_rang,new_df["salary"])
# new_df["salary"]=np.where(new_df["salary"]>upper_range,upper_range,new_df["salary"])
# new_df.boxplot(column=["salary"])
# # sns.boxenplot(x="rank",y="salary",hue="sex",data=new_df,)
# new_df.boxplot(column=['salary'])
# # sns.swarmplot(x="rank",y="salary",hue="sex",data=df,color=".25")
# plt.show()
############################################################################################


