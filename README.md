# Mini-Project
# Iris Dataset Analysis using Python

## Project Title

**Iris Dataset Analysis and Visualization using Python, NumPy, Pandas, Matplotlib, and Plotly**



## Objective

The objective of this project is to perform data analysis on the Iris dataset using Python libraries such as NumPy, Pandas, Matplotlib, and Plotly. The project demonstrates data exploration, statistical analysis, NumPy operations, and both static and interactive visualizations to gain insights into the characteristics of different Iris flower species.


## Dataset

This project uses the built-in Iris dataset available in Plotly Express.

python
import plotly.express as px

df = px.data.iris()


The dataset contains measurements of Iris flowers, including:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
- Species



## Tools Used

### Programming Language

- Python

### Libraries

- NumPy
- Pandas
- Matplotlib
- Plotly Express

### Version Control

- Git
- GitHub

---

## Project Tasks

### Part 1: Dataset Exploration

- Display first 5 records
- Display last 5 records
- Display dataset dimensions
- Display dataset information
- Display column names
- Display data types

### Part 2: Data Analysis

- Calculate average sepal length
- Calculate average petal length
- Find maximum sepal length
- Find minimum petal width
- Count total species
- Count flowers in each species

### Part 3: NumPy Operations

- Convert columns into NumPy arrays
- Calculate mean
- Calculate median
- Find maximum value
- Find minimum value
- Calculate standard deviation

### Part 4: Matplotlib Visualizations

- Line Chart (Sepal Length)
- Bar Chart (Species Count)
- Scatter Plot (Sepal Length vs Petal Length)
- Histogram (Sepal Width Distribution)

### Part 5: Plotly Visualizations

- Interactive Scatter Plot
- Interactive Box Plot
- Histogram
- Pie Chart

### Part 6: Python Fundamentals

- List operations
- Add and remove elements
- Sorting
- Finding highest and lowest values

---

## Key Findings

1. The Iris dataset contains **150 flower samples** and **3 species**:

   - Setosa
   - Versicolor
   - Virginica

2. Each species contains **50 samples**, making the dataset balanced.

3. Petal measurements show greater variation among species compared to sepal measurements.

4. Scatter plots reveal clear separation of species based on petal length and sepal length.

5. The Setosa species is distinctly separated from the other two species in most visualizations.

6. Interactive Plotly charts provide better exploration and comparison of species characteristics.

7. NumPy statistical calculations produce results consistent with Pandas aggregation methods.


## How to Run

1. Clone the repository:


git clone https://github.com/your-username/python-mini-project.git


2 . Install required libraries:

pip install pandas numpy matplotlib plotly




