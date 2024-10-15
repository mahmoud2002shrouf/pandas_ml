import pandas as pd
df=pd.read_json("mtcars.json")
print(df.info())

#series :data=[1,2,3]
#series :add int index
#series :series(data,index=["x","y"....]) that for add your self index
#series :x= series(data,index=["x","y"....]) => print(x["x"]) =>print 1
#series :x= series(data,index=["x","y"....]) => print(x["x"]) =>print 1

#series :data=["x":1,"y":2,"z":3]
#series:now you are not  compelled(مجبر) to use series bec that add index for data
#series:myvar = pd.Series(data, index = ["x", "y"]) => that print just data for row index x and y


#########################################################################################################

#dataFrame: this method use for print the data in Understandably 
#EX: 
#  data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }


# df = pd.DataFrame(data)


#print(df) : 
#      calories  duration
# 0      420        50
# 1      380        40
# 2      390        45      

 
#print(df.loc[0]):
# calories   420
# duration   50


# print(df.loc[[0, 1]]):
#   calories  duration
# 0  420         50
# 1  380         40


## df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
##         calories  duration
##   day1       420        50
##   day2       380        40
##   day3       390        45

#########################################################################################################
# if i have excel or csv i use this function read_csv(path csv file)
# df=pd.read_csv("california_housing_train.csv")
#print(df) : 
#        longitude  latitude  ...  median_income  median_house_value
# 0        -114.31     34.19  ...         1.4936             66900.0
# 1        -114.47     34.40  ...         1.8200             80100.0
# 2        -114.56     33.69  ...         1.6509             85700.0
# 3        -114.57     33.64  ...         3.1917             73400.0
# 4        -114.57     33.57  ...         1.9250             65500.0
# ...          ...       ...  ...            ...                 ...
# 16995    -124.26     40.58  ...         2.3571            111400.0
# 16996    -124.27     40.69  ...         2.5179             79000.0
# 16997    -124.30     41.84  ...         3.0313            103600.0
# 16998    -124.30     41.80  ...         1.9797             85800.0
# 16999    -124.35     40.54  ...         3.0147             94600.0


#print(df.to_string()) : that print all row(entire in DataFrame) ما تسويها بلاش تحرق الجهاز خليه مسلك
#####################################
# df=pd.read_json("mtcars.json")
# print(df)

#                   model   mpg  cyl   disp   hp  ...   qsec  vs  am  gear  carb
# 0             Mazda RX4  21.0    6  160.0  110  ...  16.46   0   1     4     4
# 1         Mazda RX4 Wag  21.0    6  160.0  110  ...  17.02   0   1     4     4
# 2            Datsun 710  22.8    4  108.0   93  ...  18.61   1   1     4     1
# 3        Hornet 4 Drive  21.4    6  258.0  110  ...  19.44   1   0     3     1
# 4     Hornet Sportabout  18.7    8  360.0  175  ...  17.02   0   0     3     2
# 5               Valiant  18.1    6  225.0  105  ...  20.22   1   0     3     1
# 6            Duster 360  14.3    8  360.0  245  ...  15.84   0   0     3     4
# 7             Merc 240D  24.4    4  146.7   62  ...  20.00   1   0     4     2
# 8              Merc 230  22.8    4  140.8   95  ...  22.90   1   0     4     2
# 9              Merc 280  19.2    6  167.6  123  ...  18.30   1   0     4     4
# 10            Merc 280C  17.8    6  167.6  123  ...  18.90   1   0     4     4
# 11           Merc 450SE  16.4    8  275.8  180  ...  17.40   0   0     3     3
# 12           Merc 450SL  17.3    8  275.8  180  ...  17.60   0   0     3     3
# 13          Merc 450SLC  15.2    8  275.8  180  ...  18.00   0   0     3     3
# 14   Cadillac Fleetwood  10.4    8  472.0  205  ...  17.98   0   0     3     4
# 15  Lincoln Continental  10.4    8  460.0  215  ...  17.82   0   0     3     4
# 16    Chrysler Imperial  14.7    8  440.0  230  ...  17.42   0   0     3     4
# 17             Fiat 128  32.4    4   78.7   66  ...  19.47   1   1     4     1
# 18          Honda Civic  30.4    4   75.7   52  ...  18.52   1   1     4     2
# 19       Toyota Corolla  33.9    4   71.1   65  ...  19.90   1   1     4     1
# 20        Toyota Corona  21.5    4  120.1   97  ...  20.01   1   0     3     1
# 21     Dodge Challenger  15.5    8  318.0  150  ...  16.87   0   0     3     2
# 22          AMC Javelin  15.2    8  304.0  150  ...  17.30   0   0     3     2
# 23           Camaro Z28  13.3    8  350.0  245  ...  15.41   0   0     3     4
# 24     Pontiac Firebird  19.2    8  400.0  175  ...  17.05   0   0     3     2
# 25            Fiat X1-9  27.3    4   79.0   66  ...  18.90   1   1     4     1
# 26        Porsche 914-2  26.0    4  120.3   91  ...  16.70   0   1     5     2
# 27         Lotus Europa  30.4    4   95.1  113  ...  16.90   1   1     5     2
# 28       Ford Pantera L  15.8    8  351.0  264  ...  14.50   0   1     5     4
# 29         Ferrari Dino  19.7    6  145.0  175  ...  15.50   0   1     5     6
# 30        Maserati Bora  15.0    8  301.0  335  ...  14.60   0   1     5     8
# 31           Volvo 142E  21.4    4  121.0  109  ...  18.60   1   1     4     2

#for that or DataFreame we use some founction :
#head : df.head()  => بتطبيع اكم صف 
#EX : 
#                model   mpg  cyl   disp   hp  ...   qsec  vs  am  gear  carb
# 0          Mazda RX4  21.0    6  160.0  110  ...  16.46   0   1     4     4
# 1      Mazda RX4 Wag  21.0    6  160.0  110  ...  17.02   0   1     4     4
# 2         Datsun 710  22.8    4  108.0   93  ...  18.61   1   1     4     1
# 3     Hornet 4 Drive  21.4    6  258.0  110  ...  19.44   1   0     3     1
# 4  Hornet Sportabout  18.7    8  360.0  175  ...  17.02   0   0     3     2



#head : df.head(10)  => بتطبيع 10 صفوف من الداتا
#EX: 
#                model   mpg  cyl   disp   hp  ...   qsec  vs  am  gear  carb
# 0          Mazda RX4  21.0    6  160.0  110  ...  16.46   0   1     4     4
# 1      Mazda RX4 Wag  21.0    6  160.0  110  ...  17.02   0   1     4     4
# 2         Datsun 710  22.8    4  108.0   93  ...  18.61   1   1     4     1
# 3     Hornet 4 Drive  21.4    6  258.0  110  ...  19.44   1   0     3     1
# 4  Hornet Sportabout  18.7    8  360.0  175  ...  17.02   0   0     3     2
# 5            Valiant  18.1    6  225.0  105  ...  20.22   1   0     3     1
# 6         Duster 360  14.3    8  360.0  245  ...  15.84   0   0     3     4
# 7          Merc 240D  24.4    4  146.7   62  ...  20.00   1   0     4     2
# 8           Merc 230  22.8    4  140.8   95  ...  22.90   1   0     4     2
# 9           Merc 280  19.2    6  167.6  123  ...  18.30   1   0     4     4



##########################################

#df.tail() => بطبع عكس HEAD يعني من الاخر بطبع مش من الاول


########################################
# df.info() => بطبع معلومات حول DF : 
#EX : 
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   model   32 non-null     object 
#  1   mpg     32 non-null     float64
#  2   cyl     32 non-null     int64  
#  3   disp    32 non-null     float64
#  4   hp      32 non-null     int64  
#  5   drat    32 non-null     float64
#  6   wt      32 non-null     float64
#  7   qsec    32 non-null     float64
#  8   vs      32 non-null     int64  
#  9   am      32 non-null     int64  
#  10  gear    32 non-null     int64  
#  11  carb    32 non-null     int64  



