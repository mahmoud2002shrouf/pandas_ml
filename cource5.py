import numpy as np
from  sklearn import preprocessing
from  sklearn.preprocessing import OneHotEncoder
from pickle import dump,load
import pandas as pd

# stadard deviation : الانحراف المعياري 
# Sx = sqrt(Σ (xi - x̄)^2 / (n - 1))
# n=عدد القيم
# x_i=كل قيمة
# x̄=mean

# cource 5 : 
# 1-standardization : 
# هو اسلوب قياسي تتركز فيه القيم حول الوسط مع انحراف معياري و حدودي و هذا يعني ان متوسط السمة تصبح صفر و ان التوزيع الناتج له احراف معيار يو حدودي
# z=(x-u)/s
# z=standardization
# x=المتغير
# u= mean
# s=stadard deviation

x_train =np.array([[1,-1,10],[2,70,80],[0,1,-1]])
# scaler2=preprocessing.StandardScaler()
# new=scaler2.fit_transform(x_train)
# print(new)
# print("--------------------------------------")
# scaler=preprocessing.RobustScaler()
# x_train_rob_scal=scaler.fit_transform(x_train)
# print(x_train_rob_scal)
# print("--------------------------------------")

# scaler3=preprocessing.MinMaxScaler(feature_range=(0,10))
# x_train_rob_scal1=scaler3.fit_transform(x_train)
# print(x_train_rob_scal1)
# dump(x_train_rob_scal,open("model/scalers.pkl",'wb'))
# my_scler=load(open("model/scalers.pkl","rb"))
# scal_result=my_scler.transform(x_train)
# print(scal_result)
##################################
#2: Non linear Transformation : بستخدمه لما تكون العلاقة بين البيانات علاقة غير خطية بحيث تصبح القيم متناسقة مع بعضها البعض
##################################
# pt=preprocessing.PowerTransformer(method='yeo-johnson',standardize=False)
# x_train_pt=pt.fit_transform(x_train)
# print(x_train_pt)
# [[ 0.85236759 -1.53229592  3.10871248]
#  [ 1.53407145  3.83817638  7.18307707]
#  [ 0.          0.68124764 -1.37445943]]

##################################
#3: Normalization :  حصر القيم بين الصفر و الواحد لكي يسهل معاجتها مثلا حجم البكسل بيكون بين 0 و 255 بقسم هل 255 
##################################

# X_normaized=preprocessing.normalize(x_train)
# print(X_normaized)
# [[ 0.09901475 -0.09901475  0.99014754]
#  [ 0.01881109  0.65838809  0.75244353]
#  [ 0.          0.70710678 -0.70710678]]
##################################
#4:Encodeing: عشان اقدر احول القيم النصية الى قيم عددية  
##################################

# x_train_string=[
#     ["male","from Us","use chatgpt"],
#     ["female","from AR","use claoude"],
#     ["male","from UR","use blackbox"],
#     ["female","from Us","use blackbox"],
# ]
# lable=["palestine","hebron","nuba","palestine","India", "US", "Japan", "US", "Japan"]
# enc=preprocessing.OrdinalEncoder()
# x_enc=enc.fit_transform(x_train_string)
# print(x_enc)
# print("------------------------------")
# lable_enc=preprocessing.LabelEncoder()
# lable_encodeing=lable_enc.fit_transform(lable)
# print(lable_encodeing)
# print("------------------------------")

# print(lable_enc.inverse_transform([2,1]))
# print("------------------------------")

# [[1. 2. 1.]
#  [0. 0. 2.]
#  [1. 1. 0.]
#  [0. 2. 0.]]
# ------------------------------
# [2 0 1 2]
# ------------------------------
# ['palestine' 'nuba']
# ------------------------------

# lable_array=np.array(lable)
# X=OneHotEncoder().fit_transform(lable_array.reshape(-1,1)).toarray()

# print(X)


##################################
#5:Discretization: هي عملية تقوم بتجزئة البيانات الى فئات  مثلا العمر : (1-10) سنوات   (11-20) سنوات (21-30) سنوات 
##################################

X=np.array([[-3,15,5],[-5,80,7],[6,30,40]])
# Kd=preprocessing.KBinsDiscretizer(n_bins=[11,65,35],encode="ordinal").fit_transform(X)
# print(Kd)
# [[ 5.  0.  0.]
#  [ 0. 64. 17.]
#  [10. 32. 34.]]

##################################
#6: Binarization: عملية تقوم ب تحويل F الى صفر و واجد و بامكاني ان احدد العتبه او ان التطبيق نفسه يحدده الاكبر نت هاي بحظها واحد و الاقل صفر
##################################
# هان الي اكبر من 15 بوخذ واحد و الاقل 0
# binarize =preprocessing.Binarizer(threshold=15)
# X_binarize=binarize.fit_transform(X)
# print(X_binarize)
# [[0 0 0]
#  [0 1 0]
#  [0 1 1]]

##################################
# 7: Generating Polyonmial : انشاء خاصية متعددة الحدود
# في بعض الحالات تكون الخواص Fقليلة ف اطر على انشائ قيم جديدة عشان اقدر اميز بين الكلاسس 
# معادلة بطبيقعا عشان ارفع مسوى F
##################################
# X=np.arange(16).reshape(4,4)
# print(X)
# print("-----------------")
# # degree=2: يولد الميزات حتى الدرجة الثانية.
# # interaction_only=True: يعني عدم احتساب الأسس التربيعية لكل متغير على حدة، ويكتفي بإنشاء تفاعلات بين المتغيرات.
# poly=preprocessing.PolynomialFeatures(degree=2,interaction_only=True)
# print(poly)
# print("-----------------")
# x_poly=poly.fit_transform(X)
# print(x_poly)

# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
# -----------------
# PolynomialFeatures(interaction_only=True)
# -----------------
# [[  1.   0.   1.   2.   3.   0.   0.   0.   2.   3.   6.]
#  [  1.   4.   5.   6.   7.  20.  24.  28.  30.  35.  42.]
#  [  1.   8.   9.  10.  11.  72.  80.  88.  90.  99. 110.]
#  [  1.  12.  13.  14.  15. 156. 168. 180. 182. 195. 210.]]

##################################
# 8 : Custom Transformers : يسمح لك بانشائ فنكشن خاص بك
##################################

transformar=preprocessing.FunctionTransformer(np.square,validate=True)
X=np.arange(4).reshape(2,2)
X_tr=transformar.fit_transform(X)
new=np.hstack((X,X_tr))# دمج 
print(new)
# [[0.         1.         0.         0.69314718]
#  [2.         3.         1.09861229 1.38629436]]