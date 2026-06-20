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


#PART 4: Visualization using Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("Iris.csv")


#Task 1:
#CHART 1: Line Chart
plt.figure(figsize = (10,8))
plt.plot(df.index, df["SepalLengthCm"], color="Skyblue")
plt.title("Sepal Length by index")
plt.xlabel("Index")
plt.ylabel("Sepal_length")
Line_chart_Path = "Sepal_Lengt_Line_Chart.png"
plt.savefig(Line_chart_Path, bbox_inches = 'tight')
plt.show()
plt.close()

#CHART 2: Bar Chart
plt.figure(figsize = (10,8))
Species_counts = df['Species'].value_counts()
plt.bar(Species_counts.index,Species_counts.values)
plt.xlabel("Species")
plt.ylabel("Count")
bar_chart_path = "Species_count.png"
plt.savefig(bar_chart_path,bbox_inches ='tight')
plt.show()
plt.close()

#CHART 3: Scatter Plot
plt.figure(figsize = (10,8))
plt.scatter(df['SepalLengthCm'], df['PetalLengthCm'],marker ='o', color='Darkblue')
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
scatter_chart_path = "Scatter_chart.png"
plt.savefig(scatter_chart_path,bbox_inches='tight')
plt.show()
plt.close()

#CHART 4 :Histogram
plt.figure(figsize =(10,8))
plt.hist(df['SepalWidthCm'],color="Darkblue") 
nbins = 20
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
histogram_chart_path = "histogram_chart.png"
plt.savefig(histogram_chart_path,bbox_inches='tight')
plt.show()
plt.close()

#Part 5: Visualization using Plotly:
import pandas as pd
import plotly.express as px

iris = px.data.iris()

#CHART 1: Interactive Scatter Plot
fig = px.scatter(
    iris,
    x="sepal_length",
    y="petal_length",
    color="species",
    title="sepal_length scatter vs petal_length scatter"
)

fig.show()

#CHART 2: Interactive Box Plot
fig = px.box(
    iris,
    x="species",
    y="petal_length",
    color="species",
    title="species vs petal_length Box Plot"
)

fig.show()

#CHART 3: Interactive Histogram
fig = px.histogram(
    iris,
    x ="sepal_length",
    nbins=20,
    title="sepal_length Histogram"
)

fig.show()

#CHART 4 :Interactive Pie Chart
Species_count=iris["species"].value_counts().reset_index()
Species_count.columns=["species","count"]
fig = px.pie(
    Species_count,
    names="species",
    values="count",
    title="Pie Chart for species count"

)

fig.show()

#Part 6: Python Fundamentals
#Create a Python list: 
marks = [78, 82, 91, 65, 88] 

#Task 1:
marks.append(90)
marks

#Task 2:
marks.remove(91)
marks

#Task 3:
marks.sort()
marks

#Task 4:
max(marks)

#Task 5:
min(marks)

