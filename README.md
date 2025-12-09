# Iris-EDA-Visualization
Objective:-

The goal of this task is to learn fundamental data exploration techniques using the Iris dataset. This includes loading data with pandas, inspecting its structure, understanding feature distributions, and creating visualizations for relationships and patterns.

Dataset:-

Iris Dataset (loaded using seaborn or from a local CSV file)

Contains 150 samples and 4 numerical features:

sepal_length

sepal_width

petal_length

petal_width

Target column: species

Steps Performed:-
✔ 1. Loaded the dataset using pandas

Loaded directly from seaborn’s built-in dataset.

Fallback option to load from a local iris.csv.

✔ 2. Inspected dataset structure

Printed the following:

Dataset shape

Column names

First rows using .head()

✔ 3. Summary statistics

Used:

.info() → to check data types and missing values

.describe() → statistical summary of numerical columns

✔ 4. Data Visualization

Created multiple plots using matplotlib and seaborn:

Scatter Plot:-

Shows relationship between two features colored by species.

Histograms:-

Visualize feature distributions for:

Sepal length

Sepal width

Petal length

Petal width

Box Plots:-

Identify outliers and distribution spread for numeric features.

Key Insights Noted:-

Species differ significantly in petal measurements.

Setosa is clearly separable from other species.

Histograms show distinct clusters by species.

Box plots reveal potential outliers in sepal width.

Skills Demonstrated:-

Data loading with pandas

Dataset inspection & statistical summaries

Basic Exploratory Data Analysis (EDA)

Creating plots using seaborn and matplotlib

Understanding patterns and differences between classes
