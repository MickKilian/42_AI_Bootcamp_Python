class TinyStatistician:
    
    @staticmethod
    def mean(x):
        if len(x) == 0:
            return None
        total = 0
        for value in x:
            total += value
        return total / len(x)

    @staticmethod
    def median(x):
        if len(x) == 0:
            return None
        # First, sort the list
        x_sorted = sorted(x)
        n = len(x_sorted)
        
        # If the length is odd, the median is the middle element
        if n % 2 != 0:
            return float(x_sorted[n // 2])
        
        # If the length is even, the median is the average of the two middle elements
        mid1, mid2 = x_sorted[n // 2 - 1], x_sorted[n // 2]
        return (mid1 + mid2) / 2

    @staticmethod
    def quartiles(x):
        if len(x) == 0:
            return None
        
        # Sort the data first
        x_sorted = sorted(x)
        n = len(x_sorted)
        
        # Calculate Q1 (the 1st quartile) and Q3 (the 3rd quartile)
        mid = n // 2
        if n % 2 == 0:
            lower_half = x_sorted[:mid]
            upper_half = x_sorted[mid:]
        else:
            lower_half = x_sorted[:mid]
            upper_half = x_sorted[mid+1:]
        
        # First quartile: median of the lower half
        q1 = TinyStatistician.median(lower_half)
        
        # Third quartile: median of the upper half
        q3 = TinyStatistician.median(upper_half)
        
        return q1, q3

    @staticmethod
    def var(x):
        if len(x) == 0:
            return None
        mean_value = TinyStatistician.mean(x)
        squared_diff_sum = 0
        for value in x:
            squared_diff_sum += (value - mean_value) ** 2
        return squared_diff_sum / len(x)

# Example of using the class
if __name__ == "__main__":
    ts = TinyStatistician()
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("Mean:", ts.mean(data))
    print("Median:", ts.median(data))
    print("Quartiles:", ts.quartiles(data))
    print("Variance:", ts.var(data))
