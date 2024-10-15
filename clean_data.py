import pandas as pd

#################################################
# ملاحظات مهمة في الاحصاء :
# mean = مجموع القيم /عددها
# median = برتب القيم تصاعدي او تنازلي القيمة الي بالوسط هي الميديان ممكن تكون قيمة اذا كان عدد الاعداد فردية و قيميتين اذا زوجي
# Mode = القيمة الاكثر تكرار
#################################################
# Data Cleaning
# Data cleaning means fixing bad data in your data set.

# Bad data could be:

# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

###############
# 1-Empty cells:
# قطرة :   dropna

###########################################
# df = pd.read_json("em.json")
###########################################

#####
# هان بحط الداتا في متغير جديد ما باثر على الاصلي
# neData=df.dropna() هاي كل اشي فيه null بتحذفه
# print(neData.to_string())
#            model   mpg  cyl  disp   hp  drat     wt   qsec  vs  am  gear  carb
# 1      Datsun 710  22.8    4   108   93  3.85  2.320  18.61   1   1     4     1
# 2  Hornet 4 Drive  21.4    6   258  110  3.08  3.215  19.44   1   0     3     14

#####
# هان العملية بتكون على الدات الاصليه
# df.dropna(inplace = True)
# print(df.to_string())
#             model   mpg  cyl  disp   hp  drat     wt   qsec  vs  am  gear  carb
# 1      Datsun 710  22.8    4   108   93  3.85  2.320  18.61   1   1     4     1
# 2  Hornet 4 Drive  21.4    6   258  110  3.08  3.215  19.44   1   0     3     1

#####
# هان بستبدل القيم الفارغة بقيم جديدة
# df.fillna(130, inplace = True)
# print(df.to_string())
#             model    mpg  cyl  disp   hp  drat       wt   qsec  vs  am  gear  carb
# 0       Mazda RX4  130.0    6   160  110  3.90  130.000  16.46   0   1     4     4
# 1      Datsun 710   22.8    4   108   93  3.85    2.320  18.61   1   1     4     1
# 2  Hornet 4 Drive   21.4    6   258  110  3.08    3.215  19.44   1   0     3     1

#####
# هان لعمود مجدد
# df["mpg"].fillna(110, inplace = True)
# print(df.to_string())

#####
# هان لاكثر من عمود
# df.fillna({"mpg": 110, "wt": 150}, inplace=True)
# print(df.to_string())

#####
# هان بستبدل حسب متوسط القيم في المجموعة
# x = df["wt"].mean()
# y=df["mpg"].mean()
# df.fillna({"mpg":y,"wt":x}, inplace = True)
# print(df.to_string())

# +++
# x = df["wt"].median()
# y=df["mpg"].median()
# df.fillna({"mpg":y,"wt":x}, inplace = True)
# print(df.to_string())

# +++
# mode()[0] : يعني القيمة الاولى من القيم المتكررة
# x = df["wt"].mode()[0]
# y=df["mpg"].mode()[0]
# df.fillna({"mpg":y,"wt":x}, inplace = True)
# print(df.to_string())

#########################################################
# 2-Wrong Format
# هان بدنا نعالج مشاكل الفورمات الخطا يعني بده رقم و انا معطيه نص
###########################################
# df = pd.read_json("format_woring.json")
###########################################
# 1 - بدي احول نوع الداتا الموجود ل نوع داتا انا بدي اياه

# columns_to_convert = ['mpg', 'cyl', 'disp', 'hp',
#                       'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
# for col in columns_to_convert:
#     df[col] = df[col].astype(int)
# print(df.to_string())
#         model  mpg  cyl  disp   hp  drat  wt  qsec  vs  am  gear  carb
# 0   Mazda RX4   21    6   160  110     3   2    16   0   1     4     4
# 1  Datsun 710   22    4   108   93     3   2    18   1   0     4     1
# 2     Valiant   18    6   225  105     3   3    20   1   0     3     1


# 2: خذف الصفوف ذات القيم الخاطئة
# df.dropna(subset=['disp'], inplace = True)
# print(df.to_string())

######################################################################
# 3-Wrong Data
# مثلا عندي قيم شاذة او مثلا سرعات بالسالب
###########################################
# df = pd.read_json("woring_data.json")
###########################################
# استبدال القيم السالبة بالقيمة المطلقة
# columns_to_check = ['mpg', 'cyl', 'disp', 'drat', 'wt', 'carb']
# for col in columns_to_check:
#     df[col] = df[col].abs()
# print(df.to_string())


# قيم جديدة :
# for col in columns_to_check:
#     for x in df.index:
#         if df.loc[x, col] < 0:
#             df.loc[x, col] = 120
#                model    mpg  cyl  disp   hp    drat      wt   qsec  vs  am  gear  carb
# 0          Mazda RX4  120.0    6   160  110  120.00    2.62  16.46   0   2     4    10
# 1         Datsun 710  105.0  120   120   93    3.85  120.00  18.61   3   1     7   120
# 2  Hornet Sportabout   18.7    8   360  175    3.15    3.44  17.02   5   6     3     2

# او ممكن نحذفها
# for col in columns_to_check:
#     for x in df.index:
#         if df.loc[x, col] < 0:
#             df.drop(x, inplace=True)
# print(df.to_string())

#                model   mpg  cyl  disp   hp  drat    wt   qsec  vs  am  gear  carb
# 2  Hornet Sportabout  18.7    8   360  175  3.15  3.44  17.02   5   6     3     2


######################################################################
# 3-Removing Duplicates
# بدي قيم متكررة
###########################################
df = pd.read_json("duplicates.json")
###########################################
df.drop_duplicates(inplace=True)
print(df.to_string())
#       model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb
# 0  Mazda RX4  21.0    6  160.0  110  3.90  2.62  16.46   0   1     4     4
# 2  Merc 280C  17.8    6  167.6  123  3.92  3.44  18.90   1   0     4     4