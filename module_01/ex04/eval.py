class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        # Check if the lists have the same length
        if len(coefs) != len(words):
            return -1
        
        # Calculate the sum of the lengths of words weighted by coefficients using zip
        total = sum(coef * len(word) for coef, word in zip(coefs, words))
        return total
    
    @staticmethod
    def enumerate_evaluate(coefs, words):
        # Check if the lists have the same length
        if len(coefs) != len(words):
            return -1
        
        # Calculate the sum of the lengths of words weighted by coefficients using enumerate
        total = sum(coefs[i] * len(words[i]) for i, _ in enumerate(words))
        return total

# Example usage:
coefs = [1, 2, 3]
words = ["apple", "banana", "cherry"]

print("Using zip_evaluate:")
print(Evaluator.zip_evaluate(coefs, words))  # Output should be 34

print("\nUsing enumerate_evaluate:")
print(Evaluator.enumerate_evaluate(coefs, words))  # Output should be 34
