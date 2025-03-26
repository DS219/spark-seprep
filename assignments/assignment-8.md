# Assignment 8: Data Science 101
## Exploratory Data Analysis (EDA) and Hypothesis Testing

### Objective
This assignment aims to deepen students' understanding of Exploratory Data Analysis (EDA), hypothesis formulation, and testing through practical application.

### Datasets to Choose From
1. **Air Quality Dataset:**
   - **Link:** [Air Quality Dataset](https://archive.ics.uci.edu/ml/datasets/Air+quality)
   - **Description:** Contains hourly air pollutants data from multiple Italian cities.

2. **Adult Income Dataset:**
   - **Link:** [Adult Income Dataset](https://archive.ics.uci.edu/ml/datasets/Adult)
   - **Description:** Focuses on predicting whether a person makes over $50K a year based on census data.

3. **Heart Disease Dataset:**
   - **Link:** [Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
   - **Description:** Consists of data from the Cleveland database, with attributes relating to the presence of heart disease.

4. **Online Shoppers Purchasing Intention Dataset:**
   - **Link:** [Online Shoppers Purchasing Intention Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset)
   - **Description:** Data on online shopping sessions intended to predict purchasing intentions.

5. **Solar Flare Dataset:**
   - **Link:** [Solar Flare Dataset](https://archive.ics.uci.edu/ml/datasets/Solar+Flare)
   - **Description:** Aims to predict solar flare activity based on lab measurements.

### Assignment Tasks
1. **Importing Data and Libraries:** Import the dataset and essential libraries like Pandas, NumPy, Matplotlib, and Seaborn using a Jupyter notebook.
2. **Exploratory Data Analysis (EDA):** Examine the dataset’s structure, compute summary statistics, and visualize distributions.
3. **Hypothesis Formulation:** Develop hypotheses based on the observed data patterns and relationships.
4. **Hypothesis Testing:** Employ statistical tests or visual methods to examine your hypotheses and discuss the outcomes.
5. **Documentation and Reporting:** Thoroughly document the analysis process in the Jupyter notebook, including code, visualizations, and interpretations. Summarize and report your findings clearly, stating whether the data supports or refutes your hypotheses.

### GitHub Workflow for Submission
1. **Prepare Your Work Environment:**
   ```bash
   cd <to your github repo path>
   git checkout main
   git fetch upstream
   git rebase upstream/main
   git checkout -b assignment-8-branch
2. **Navigate and Prepare Your Jupyter Notebook:**
   ```bash
   mkdir student-work/assignment-8/FIRSTNAME-LASTNAME
   cd student-work/assignment-8/FIRSTNAME-LASTNAME
   touch assignment8-<yourname>.ipynb
3. **Add, Commit, and Push Your Notebook:**
    ```bash
    git add assignment8-<yourname>.ipynb
    git commit -m "Add Assignment 8 Jupyter Notebook by <yourname>"
    git push origin assignment-8-branch
4. **Open a Pull Request for Review:**
Create a pull request from assignment-8-branch to the main branch for peer and instructor review.

#### Notes
* Replace <yourname> with your actual name formatted as “FirstnameLastname” in the notebook filename.
* Ensure that the Jupyter notebook includes all steps of the EDA, hypothesis testing, and conclusions.

### Grading Rubric

#### 1. Importing Data and Libraries (10 points)
- **0-2 points:** Inadequate or incorrect library imports; major issues with dataset loading.
- **3-5 points:** Adequate library imports but issues with dataset loading.
- **6-8 points:** Proper library imports and successful dataset loading; minor issues.
- **9-10 points:** Correct and efficient imports and dataset loading.

#### 2. Exploratory Data Analysis (EDA) (20 points)
- **0-5 points:** Minimal exploration; inadequate visualizations.
- **6-10 points:** Basic exploration and visualization; lacks depth.
- **11-15 points:** Good exploration and appropriate visualizations.
- **16-20 points:** Comprehensive and insightful EDA.

#### 3. Hypothesis Formulation (15 points)
- **0-5 points:** Poorly formulated or irrelevant hypotheses.
- **6-10 points:** Formulated hypotheses but lack clarity or full relevance.
- **11-13 points:** Clear and relevant hypotheses.
- **14-15 points:** Well-formulated, insightful hypotheses.

#### 4. Hypothesis Testing (25 points)
- **0-8 points:** Incorrect testing methods; major flaws.
- **9-15 points:** Some correct testing but issues with methods or interpretation.
- **16-20 points:** Appropriate methods and clear interpretation.
- **21-25 points:** Rigorous and insightful hypothesis testing.

#### 5. Documentation and Reporting (20 points)
- **0-5 points:** Poorly documented; lacks clarity.
- **6-10 points:** Adequate documentation; some clarity issues.
- **11-15 points:** Good documentation and clear explanations.
- **16-20 points:** Excellent, well-explained documentation.

#### 6. Overall Presentation (10 points)
- **0-3 points:** Poorly organized; major presentation issues.
- **4-6 points:** Adequate organization; some clarity issues.
- **7-9 points:** Well-organized; good clarity.
- **10 points:** Exceptionally clear and well-organized presentation.

#### 7. Extra Credit (up to 20 points)
- **Extra Credit:** Additional analyses, innovative approaches, or deeper insights beyond the assignment scope.

#### 8. GitHub Specific Criteria (20 points)
- **5 points:** No extra packages and files installed.
- **3 points:** Descriptive and clear commit message.
- **3 points:** Only 1 commit in your PR.
- **3 points:** No extra junk files in PR.
- **3 points:** Changes made on the assignment branch, not on main.
- **3 points:** No modifications to other files in the repository.
