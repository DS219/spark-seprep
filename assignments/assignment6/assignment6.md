### Assignment 6: Data Science 101

#### Title: Exploratory Data Analysis (EDA) and Hypothesis Testing

#### Objective:
The objective of this assignment is to encourage students to explore and analyze datasets, perform Exploratory Data Analysis (EDA), frame hypotheses, and use data visualization to prove or disprove their hypotheses. Students will create a Jupyter notebook for their analysis.

#### Datasets to Choose From:

1. **Student Performance Dataset:**
   - Dataset: [Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/Student+Performance)
   - Description: Includes data on student grades, demographic, social, and school-related features from two Portuguese schools.

2. **Census Income Dataset:**
   - Dataset: [Census Income Dataset](https://archive.ics.uci.edu/ml/datasets/Census+Income)
   - Description: Focuses on predicting whether an individual's income exceeds $50K/yr based on census data.

3. **Wine Dataset:**
   - Dataset: [Wine Dataset](https://archive.ics.uci.edu/ml/datasets/Wine)
   - Description: Results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars.

4. **German Credit Data Dataset:**
   - Dataset: [German Credit Data Dataset](https://archive.ics.uci.edu/ml/datasets/Statlog+(German+Credit+Data))
   - Description: Classifies people described by a set of attributes as good or bad credit risks.

5. **Wine Quality Dataset:**
   - Dataset: [Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality)
   - Description: Contains various physicochemical properties of red and white wine, and quality ratings.

#### Assignment Tasks:

1. **Importing Data and Libraries:**
   - Use Python and Jupyter notebook to import the chosen dataset and necessary libraries (Pandas, NumPy, Matplotlib, Seaborn).

2. **Exploratory Data Analysis (EDA):**
   - Explore the dataset's structure, summary statistics, and distributions.
   - Visualize key features using appropriate plots (scatter plots, histograms, box plots, etc.).
   - Use subplots where appropriate to compare distributions or highlight trends.

3. **Hypothesis Formulation:**
   - Look at the patterns and relationships shown in your visualizations. Think about what the data is telling you. Formulate at least two hypotheses based on what you observe. For example:
     - **Student Performance Dataset:** You might notice students with higher parental education seem to get better grades, so your hypothesis could be, "Parental education level influences student grades."
     - **Census Income Dataset:** If you see older individuals tend to have higher incomes, you could hypothesize, "Age is a significant predictor of income above $50K."
     - **Wine Dataset:** If higher alcohol content seems to align with higher wine quality, you could propose, "There is a correlation between alcohol content and wine quality."

   - Remember, a hypothesis is just an idea you have about the data that you want to test. It should be something that you can measure or check using the data.

4. **Hypothesis Testing:**
   - Use appropriate statistical tests or visualizations to test the hypotheses. Consider:
     - Visualizations that prove or disprove your hypothesis.
     - T-tests or ANOVA for comparing group means.
     - Correlation coefficients (Pearson or Spearman) for relationships.
     - Chi-square test for categorical data.
   - Interpret the results and discuss their implications. Did the data support your hypothesis, or was it disproven?

5. **Documentation and Reporting:**
   - Document the entire analysis process, including code, explanations, and interpretations.
   - Summarize key findings in a clear and concise report. Explain whether the data supports the hypotheses or not.
   - Ensure visualizations are well-labeled and meaningful.

#### Extra Credit (Optional):
- Perform additional analyses, such as using another dataset for comparison, feature engineering, or applying a machine learning algorithm.
- Provide in-depth insights and recommendations based on your findings.

#### Sample Jupyter Notebook Template:

```python
# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importing the dataset
# Replace 'your_dataset_url' with the actual URL or file path
url = 'your_dataset_url'
df = pd.read_csv(url)

# Exploratory Data Analysis (EDA)
# Explore the dataset's structure and summary statistics

# Visualize key features using plots

# Hypothesis Formulation
# Formulate at least two hypotheses based on what you observe in the visuals

# Hypothesis Testing
# Test the formulated hypotheses using statistical tests or visualizations

# Documentation and Reporting
# Document the entire analysis process, including code and explanations
# Summarize key findings in a clear and concise report
```

**Note:** Students should replace `your_dataset_url` with the actual URL or file path of their chosen dataset.

#### How to Submit:

1. Ensure that you are up to date with the upstream Github repository:
    ```bash
    cd <to your github repo path>
    git checkout main
    git fetch upstream
    git rebase upstream/main
    ```

2. Create a new branch called `assignment6` based on the upstream `main` branch:
    ```bash
    git checkout -b assignment6 upstream/main
    ```

3. Head to the directory **assignments/assignment6** and create a directory there with your name in the format **FIRST-LAST**.
The directory should be **assignments/assignment6/[FIRSTNAME-LASTNAME]** so you can add your dataset and Jupyter notebook to this folder.

4. After adding your changes, push the branch and make a pull request to the upstream repository.
