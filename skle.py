from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd
df=[[np.nan,2],[6,np.nan],[4,7],[7,8]]
imp=SimpleImputer(missing_values=np.nan,strategy="mean")
data=imp.fit_transform(df)


print(data)
