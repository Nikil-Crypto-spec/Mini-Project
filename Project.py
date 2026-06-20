import plotly.express as px

df = px.data.iris()
df

#Part 1: Dataset Exploration:
#Task 1:
df.head(5)

#Task 2:
df.tail(5)

#Task 3:
df.shape

#Task 4:
df.info()

#Task 5:
df.columns

#Task 6:
df.dtypes

#Part 2: Data Analysis:
#Task 1:
average = df["sepal_length"].mean()

#Task 2:
average = df["petal_length"].mean()

#Task 3:
maximum = df["sepal_length"].max()

#Task 4:
minimum = df["petal_width"].min()

#Task 5:
len((df['species']).unique())

#Task 6:
df["species"].value_counts()

#Part 3: NumPy Practice:
import numpy as np

#Task 1:
arr = np.array(df["sepal_length"].mean())
arr = np.array(df["petal_length"].mean())


#Task 2:
arr = np.array(df["sepal_length"].median())
arr = np.array(df["petal_length"].median())

#Task 3:
arr = np.array (df["sepal_length"].max())
arr = np.array(df["petal_length"].max())

#Task 4:
arr = np.array(df["sepal_length"].min())
arr = np.array(df["petal_length"].min())

#Task 5 :
arr = np.array(df["sepal_length"].std())
arr = np.array(df["petal_length"].std())