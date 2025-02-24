import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class Komparator:
    def __init__(self, data: pd.DataFrame):
        self.data = data
    
    def compare_box_plots(self, categorical_var: str, numerical_var: str):
        """
        Displays box plots to compare how the distribution of the numerical variable
        changes with respect to the categories of the categorical variable.
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=categorical_var, y=numerical_var, data=self.data)
        plt.title(f"Box Plot of {numerical_var} by {categorical_var}")
        plt.show()
    
    def density(self, categorical_var: str, numerical_var: str):
        """
        Displays the density of the numerical variable, with separate curves for each subpopulation.
        """
        plt.figure(figsize=(10, 6))
        sns.kdeplot(data=self.data, x=numerical_var, hue=categorical_var, fill=True, common_norm=False)
        plt.title(f"Density of {numerical_var} by {categorical_var}")
        plt.show()
    
    def compare_histograms(self, categorical_var: str, numerical_var: str):
        """
        Plots histograms for the numerical variable, one for each category of the categorical variable.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.data, x=numerical_var, hue=categorical_var, kde=True, multiple="stack", bins=30)
        plt.title(f"Histogram of {numerical_var} by {categorical_var}")
        plt.show()
    
    def compare_multiple_histograms(self, categorical_var: str, numerical_vars: list):
        """
        For a list of numerical variables, this method will plot a histogram for each.
        """
        for numerical_var in numerical_vars:
            self.compare_histograms(categorical_var, numerical_var)
