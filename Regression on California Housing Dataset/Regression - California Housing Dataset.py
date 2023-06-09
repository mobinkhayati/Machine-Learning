from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sklearn.metrics as met
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn  as sns

from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

x = housing.data
y = housing.target

df = pd.DataFrame(x, columns=housing.feature_names)

df ['Price'] = y
df

print(housing.keys())

#print(housing.DESCR)
print (housing.feature_names)

plt.subplots(layout="constrained")

plt.subplot(331)
plt.scatter(df.MedInc, df.Price, color='g')
plt.xlabel('MedInc')
plt.ylabel('prices')

plt.subplot(332)
plt.scatter(df.HouseAge, df.Price, color='r')
plt.xlabel('HouseAge')
plt.ylabel('prices')

plt.subplot(333)
plt.scatter(df.AveRooms, df.Price, color='b')
plt.xlabel('AveRooms')
plt.ylabel('prices')

plt.subplot(334)
plt.scatter(df.AveBedrms, df.Price, color='b')
plt.xlabel('AveBedrms')
plt.ylabel('prices')

plt.subplot(335)
plt.scatter(df.Population, df.Price, color='y')
plt.xlabel('Population')
plt.ylabel('prices')

plt.subplot(336)
plt.scatter(df.AveOccup, df.Price, color='g')
plt.xlabel('AveOccup')
plt.ylabel('prices')

plt.subplot(337)
plt.scatter(df.Latitude, df.Price, color='g')
plt.xlabel('Latitude')
plt.ylabel('prices')

plt.subplot(338)
plt.scatter(df.Longitude, df.Price, color='r')
plt.xlabel('Longitude')
plt.ylabel('prices')

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.3,random_state=42)

xtrain.shape

xtest.shape

ytrain.shape

ytest.shape

model = LinearRegression()

model.fit(xtrain , ytrain)

ypred = model.predict(xtest)
ypred.shape

met.mean_squared_error(ytest,ypred)

model.intercept_

model.coef_

plt.scatter(ytest, ypred)
plt.xlabel('prices')
plt.ylabel('predicted prices')

sns.set(style="white")

df_corr= df[:]
corr = df_corr.dropna().corr()
mask = np.zeros_like(corr, dtype=np.bool)
f, ax = plt.subplots(figsize=(30, 10))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, square=True, linewidths=.5, ax=ax);
