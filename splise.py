import pandas as pd
import numpy as np
#############################################
##
# تقسيم البيانات :
#     1-بيانات تدريب
#     2-بيانات اختبار

# df = pd.read_json("dataset/animals.json")
# data_copy = df.copy()  # نسخة من الداتا
# # اخذنا 80% من الداتا للتدريب
# traning_set = data_copy.sample(frac=0.80, random_state=0)
# test_set = data_copy.drop(traning_set.index)  # باقي 80% بدي اخذها للاختبار

# traning_set_lable = traning_set.pop("label")
# test_set_lable = test_set.pop("label")
# print("________________________________________________________________________")
# print(traning_set_lable) ##بطيع بس lable
# print("________________________________________________________________________")
# print(test_set_lable)##بطيع بس lable
# print("________________________________________________________________________")
#############################################
##اكمال في الكورس ##
##txt##
# f=open("dataset/test.txt")
# for l in f:
#     info=l.split(",")
#     info[0]=float(info[0])
#     print(info)
    
# f.close()
#############################################
##حفظ بيانات في txt##
a=np.array([1,2,3,4,5,6])
# np.savetxt("dataset/np.txt",a,fmt="%d")
# b=np.loadtxt("dataset/np.txt",dtype=int)
# print(a==b)
##يوجد ملاحظات بخصوص %d في note من سطر 1 الى 28

##dat##
##بحفظ البانات مشفرة##
# a.tofile("dataset/dat.dat")
# b=np.fromfile("dataset/dat.dat",dtype=int)
# print(a==b)

##npy##
##بحفظ البانات مشفرة## 
np.save("dataset/file.npy",a)
b=np.load("dataset/file.npy")
print(a==b)

