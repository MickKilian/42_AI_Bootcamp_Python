import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

class MyPlotLib:
    @staticmethod
    def histogram(data, features):
        """
        Plots a histogram for each numerical feature in the list.
        """
        for feature in features:
            plt.figure(figsize=(8, 6))
            sns.histplot(data[feature], kde=False, bins=30)
            plt.title(f"Histogram of {feature}")
            plt.xlabel(feature)
            plt.ylabel("Frequency")
            plt.show()

    @staticmethod
    def density(data, features):
        """
        Plots the density curve (KDE) for each numerical feature in the list.
        """
        for feature in features:
            plt.figure(figsize=(8, 6))
            sns.kdeplot(data[feature], shade=True)
            plt.title(f"Density Curve of {feature}")
            plt.xlabel(feature)
            plt.ylabel("Density")
            plt.show()

    @staticmethod
    def pair_plot(data, features):
        """
        Creates a scatter plot matrix with histograms on the diagonal.
        """
        sns.pairplot(data[features])
        plt.suptitle("Pair Plot of Features", y=1.02)
        plt.show()

    @staticmethod
    def box_plot(data, features):
        """
        Displays a box plot for each numerical feature.
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=data[features])
        plt.title("Box Plot of Features")
        plt.show()
