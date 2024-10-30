# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Load the dataset
df = pd.read_csv('/Users/stephanmacdougall/github/spark-seprep/assignments/assignment6/stephan-macdougall/student-mat.csv', sep=';')

df['Mjob_teacher'] = df['Mjob'] == 'teacher'
df['Fjob_teacher'] = df['Fjob'] == 'teacher'
#SUMMARY
print("DataFrame Summary:")
print(df.info())  # Summary of the DataFrame structure
print("\nFirst 5 rows of the DataFrame:")
print(df.head())  # Display the first 5 rows of the DataFrame
print("\nDescriptive Statistics:")
print(df.describe())  # Descriptive statistics for numerical columns

# HYPOTHESES
# Having a mother or father whose occupation is teaching affects the grades of the students.
# The level of education of a student's parents will influence whether they want to pursue higher education

# HYPOTHESIS TESTING
# Visualization 1: Box plot for final grades based on whether Mjob or Fjob is 'teacher'
plt.figure(figsize=(12, 6))
sns.boxplot(x='Mjob', y='G3', data=df, hue='Mjob_teacher', dodge=True)
plt.title('Final Grades (G3) Based on Mother\'s Job')
plt.xlabel('Mother\'s Job')
plt.ylabel('Final Grades (G3)')
plt.legend(title='Is Teacher', labels=['No', 'Yes'])
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='Fjob', y='G3', data=df, hue='Fjob_teacher', dodge=True)
plt.title('Final Grades (G3) Based on Father\'s Job')
plt.xlabel('Father\'s Job')
plt.ylabel('Final Grades (G3)')
plt.legend(title='Is Teacher', labels=['No', 'Yes'])
plt.show()

# Visualization 2: Count plot for students' desire for higher education based on parental education levels
plt.figure(figsize=(10, 6))
sns.countplot(x='higher', hue='Medu', data=df)
plt.title('Desire for Higher Education Based on Mother\'s Education Level')
plt.xlabel('Desire for Higher Education')
plt.ylabel('Count')
plt.legend(title='Mother\'s Education Level', labels=['None', '1', '2', '3', '4'])
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='higher', hue='Fedu', data=df)
plt.title('Desire for Higher Education Based on Father\'s Education Level')
plt.xlabel('Desire for Higher Education')
plt.ylabel('Count')
plt.legend(title='Father\'s Education Level', labels=['None', '1', '2', '3', '4'])
plt.show()


# T-test for final grades based on whether the mother is a teacher
teacher_grades = df[df['Mjob_teacher'] == True]['G3']
non_teacher_grades = df[df['Mjob_teacher'] == False]['G3']
t_stat_mother, p_value_mother = stats.ttest_ind(teacher_grades, non_teacher_grades)

# T-test for final grades based on whether the father is a teacher
teacher_grades_father = df[df['Fjob_teacher'] == True]['G3']
non_teacher_grades_father = df[df['Fjob_teacher'] == False]['G3']
t_stat_father, p_value_father = stats.ttest_ind(teacher_grades_father, non_teacher_grades_father)

# ANOVA for final grades based on Father's Job
anova_result = stats.f_oneway(
    df[df['Fjob'] == 'teacher']['G3'],
    df[df['Fjob'] != 'teacher']['G3']
)

point_biserial_corr_med = stats.pointbiserialr(df['higher'].map({'yes': 1, 'no': 0}), df['Medu'])

point_biserial_corr_fed = stats.pointbiserialr(df['higher'].map({'yes': 1, 'no': 0}), df['Fedu'])

contingency_table_mother = pd.crosstab(df['higher'], df['Mjob'])
chi2_stat_mother, p_val_mother, dof_mother, expected_mother = stats.chi2_contingency(contingency_table_mother)

contingency_table_father = pd.crosstab(df['higher'], df['Fjob'])
chi2_stat_father, p_val_father, dof_father, expected_father = stats.chi2_contingency(contingency_table_father)

# Print results
print(f"T-test for Mother's Job as Teacher: t-statistic = {t_stat_mother}, p-value = {p_value_mother}")
print(f"T-test for Father's Job as Teacher: t-statistic = {t_stat_father}, p-value = {p_value_father}")
print(f"ANOVA for Father's Job: F-statistic = {anova_result.statistic}, p-value = {anova_result.pvalue}")
print(f"Point-biserial correlation between Mother's Education and Desire for Higher Education: "
      f"correlation = {point_biserial_corr_med.correlation}, p-value = {point_biserial_corr_med.pvalue}")
print(f"Point-biserial correlation between Father's Education and Desire for Higher Education: "
      f"correlation = {point_biserial_corr_fed.correlation}, p-value = {point_biserial_corr_fed.pvalue}")
print(f"Chi-square test for Mother's Job: chi2-statistic = {chi2_stat_mother}, p-value = {p_val_mother}")
print(f"Chi-square test for Father's Job: chi2-statistic = {chi2_stat_father}, p-value = {p_val_father}")

# Conclusion for Hypotheses

# Hypothesis 1: Having a mother or father whose occupation is teaching affects the grades of the students.
# Conclusion: The analysis did not find strong evidence to support this hypothesis. 
# The t-test for the mother's job as a teacher showed a p-value of 0.252, indicating no significant difference in final grades. 
# The t-test for the father's job as a teacher had a p-value of 0.058, which is marginally significant, suggesting a potential effect, 
# but further investigation is needed to draw definitive conclusions.

# Hypothesis 2: The level of education of a student's parents will influence whether they want to pursue higher education.
# Conclusion: The analysis supports this hypothesis. 
# Both point-biserial correlations for the mother's and father's education levels with the desire for higher education were significant, 
# with p-values of 0.00075 and 0.00049, respectively. This indicates a positive relationship, suggesting that higher parental education levels 
# are associated with a greater desire for students to pursue higher education.