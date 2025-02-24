import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # Number of centroids
        self.max_iter = max_iter  # Number of max iterations
        self.centroids = None  # To store centroid positions
        self.cluster_assignments = None  # To store which cluster each point belongs to

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        Randomly pick n centroids from the dataset.
        Args:
        -----
          X: A numpy.ndarray (m * n), where m is the number of data points, 
              and n is the number of features.
        Return:
        -------
          None.
        """
        # Randomly initialize centroids
        random_indices = random.sample(range(X.shape[0]), self.ncentroid)
        self.centroids = X[random_indices]
        
        for _ in range(self.max_iter):
            # Step 1: Assign points to the nearest centroid
            self.cluster_assignments = self.predict(X)

            # Step 2: Update centroids
            new_centroids = np.zeros_like(self.centroids)
            for i in range(self.ncentroid):
                cluster_points = X[self.cluster_assignments == i]
                if cluster_points.shape[0] > 0:
                    new_centroids[i] = cluster_points.mean(axis=0)
            
            # If centroids don't change, we've converged
            if np.allclose(self.centroids, new_centroids):
                break
            self.centroids = new_centroids

    def predict(self, X):
        """
        Predict the closest cluster for each data point.
        Args:
        -----
          X: A numpy.ndarray (m * n).
        Return:
        -------
          A numpy.ndarray of shape (m,), where each element represents the 
          index of the closest centroid.
        """
        distances = np.zeros((X.shape[0], self.ncentroid))
        
        # Calculate the L1 distance (Manhattan distance) to each centroid
        for i in range(self.ncentroid):
            distances[:, i] = np.abs(X - self.centroids[i]).sum(axis=1)
        
        # Return the index of the closest centroid for each point
        return np.argmin(distances, axis=1)

    def plot(self, X):
        """
        (Optional) Display results on 3 different plots, each showing 2 feature combinations.
        Args:
        -----
          X: A numpy.ndarray (m * 3) for features (height, weight, bone_density).
        """
        feature_combinations = [(0, 1), (0, 2), (1, 2)]  # Feature pairs: (height, weight), (height, density), (weight, density)

        plt.figure(figsize=(18, 6))
        for i, (feature1, feature2) in enumerate(feature_combinations):
            plt.subplot(1, 3, i + 1)
            for j in range(self.ncentroid):
                cluster_points = X[self.cluster_assignments == j]
                plt.scatter(cluster_points[:, feature1], cluster_points[:, feature2], label=f'Cluster {j}')
            plt.xlabel(f'Feature {feature1}')
            plt.ylabel(f'Feature {feature2}')
            plt.title(f'Clustered by Feature {feature1} and {feature2}')
            plt.legend()
        plt.show()


# Helper function to load dataset and convert it into numpy arrays
def load_data(filepath):
    df = pd.read_csv(filepath)
    X = df[['height', 'weight', 'bone_density']].values  # Convert to numpy array
    return X

if __name__ == '__main__':
    import sys

    # Read arguments from command line
    filepath = sys.argv[1] if len(sys.argv) > 1 else '../ressources/solar_system_census.csv'
    ncentroid = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    max_iter = int(sys.argv[3]) if len(sys.argv) > 3 else 30

    # Load data
    X = load_data(filepath)

    # Create and fit the KMeans model
    kmeans = KmeansClustering(max_iter=max_iter, ncentroid=ncentroid)
    kmeans.fit(X)

    # Display centroids and the number of points per cluster
    print(f'Centroids:')
    print(kmeans.centroids)
    print("\nCluster assignments:")
    for i in range(ncentroid):
        print(f'Cluster {i}: {np.sum(kmeans.cluster_assignments == i)} points')

    # (Optional) Visualize the clusters
    kmeans.plot(X)
